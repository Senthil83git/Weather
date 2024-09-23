import tkinter as tk
from tkinter import messagebox, PhotoImage
import requests as req
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from read_api_details import read_detail
from format_API_output import get_detail
import os

def get_city_details(button):
    
    delete_previous_content()
    
    api_key,base_url=read_detail()  
    
    city = city_entry.get()
    
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "key=" + api_key + "&q=" + city + "&days=5&aqi=yes&alerts=no"
    response = req.get(complete_url)
    x=response.json()
   
    if(response.status_code==200):
        tempC,tempF,country,state,condition,bg,date_list, max_temp_list,min_temp_list=get_detail(x)
        if (button['text']=="Get Current Details"):
            result_labelc.config(text=f"Temperature in Celcius: {str(tempC)}°C",background=bg,foreground="black",relief="flat",font=("Helvetica", 12, "bold italic"))
            result_labelf.config(text=f"Temperature in Fahrenheat: {str(tempF)} F",background=bg,foreground="black",relief="flat",font=("Helvetica", 12, "bold italic"))
            result_labelcond.config(text=f"Condition is: {condition}",background=bg,foreground="black",relief="flat",font=("Helvetica", 12, "bold italic"))
            result_labelcont.config(text=f"Located in Country: {country}",background=bg,foreground="black",relief="flat",font=("Helvetica", 12, "bold italic"))
            result_labels.config(text=f"        in State: {state}",background=bg,foreground="black",relief="flat",font=("Helvetica", 12, "bold italic"))
        else:
            get_temparture_trend_chart(date_list,max_temp_list,min_temp_list)
    else:
        messagebox.showwarning("Input Error", x['error']['message'])

    
# Create a function to handle the Clear button click
def clear_fields():
    
    delete_previous_content()
    city_entry.delete(0, tk.END)

#to exit app
def exit_app():
    window.quit()


#To get 5 days forecast in trend chart
def get_temparture_trend_chart(date_list,max_temp_list,min_temp_list):
    
    # Create a Matplotlib figure and axis
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)

    # Plot the trend line
    ax.plot(date_list, max_temp_list, marker="^", linestyle="solid", color="orange", label="Max Temperature Trend")
    ax.plot(date_list, min_temp_list, marker="v", linestyle="dashed", color="blue", label="Min Temperature Trend")

    # Set chart title and labels
    ax.set_title("Temperature Trend Over 5 Days")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature in Fahrenheat")

    # Add data labels for max temperatures
    for i, temp in enumerate(max_temp_list):
        ax.text(i, temp + 1, f"{temp}F", ha='center', color='black', fontsize=10)  # Offset label slightly above

    # Add data labels for min temperatures
    for i, temp in enumerate(min_temp_list):
        ax.text(i, temp - 1, f"{temp}F", ha='center', color='black', fontsize=10)

    # Add a grid for better visualization
    ax.grid(True)
    ax.legend(loc="upper right")
    # Embed the figure in the Tkinter window
    canvas_chart = FigureCanvasTkAgg(fig, master=canvas)
    canvas_chart.draw()

    # Display the canvas in the window
    chart_window = canvas.create_window(700, 50, anchor="nw", window=canvas_chart.get_tk_widget())

#This is to clear previous content from the page
def delete_previous_content():
     # Clear previous chart
    for widget in canvas.winfo_children():
        widget.destroy()
    
    result_labelc.config(text="",relief="flat",background="SystemButtonFace")
    result_labelf.config(text="",relief="flat",background="SystemButtonFace")
    result_labelcont.config(text="",relief="flat",background="SystemButtonFace")
    result_labelcond.config(text="",relief="flat",background="SystemButtonFace")
    result_labels.config(text="",relief="flat",background="SystemButtonFace")


# Create the main application window
window = tk.Tk()
window.title("Weather Forecast")

# Set window size to 500x300
window.geometry("500x500")

# Get the directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the relative path to a file located in the same directory
image_file_path = os.path.join(current_dir, "data", "nature-ucp.png")

# Load the background image
background_image = PhotoImage(file=image_file_path)  # Replace with your image file path

# Create a canvas to hold the image
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack(fill="both", expand=True)

# Display the background image on the canvas
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Create the "Enter City" label
city_label = tk.Label(window, text="Enter City:",background="silver",foreground="black",relief="solid",font=("Helvetica", 12, "bold"))
city_label_window = canvas.create_window(50, 50, anchor="nw", window=city_label)

# Create the text box (Entry widget) for city input
city_entry = tk.Entry(window, width=30,background="white",foreground="black",relief="solid",font=("Helvetica", 14, "bold"))
city_entry_window = canvas.create_window(250, 50, anchor="nw", window=city_entry)

# Create the "Get Current" button
current_forecast_button = tk.Button(window, text="Get Current Details", command=lambda: get_city_details(current_forecast_button), background="aqua",foreground="black",relief="sunken",font=("Helvetica", 12, "bold"))
current_forecast_button_window = canvas.create_window(50, 120, anchor="nw", window=current_forecast_button)

# Create the "Clear" button
clear_button = tk.Button(window, text="Clear", command=clear_fields, background="aqua",foreground="black",relief="sunken",font=("Helvetica", 12, "bold"))
clear_button_window=canvas.create_window(460, 120, anchor="nw", window=clear_button)

# Create the "Exit" button
exit_button = tk.Button(window, text="Exit", command=exit_app, background="aqua",foreground="black",relief="sunken",font=("Helvetica", 12, "bold"))
exit_button_window=canvas.create_window(550, 120, anchor="nw", window=exit_button)

# Create the "Get Current" button
future_forecast_button = tk.Button(window, text="Get Forecast of 5 days", command=lambda: get_city_details(future_forecast_button), background="aqua",foreground="black",relief="sunken",font=("Helvetica", 12, "bold"))
future_forecast_button_window = canvas.create_window(245, 120, anchor="nw", window=future_forecast_button)

result_labelc = tk.Label(window, text="")
result_labelc_window = canvas.create_window(50, 180, anchor="nw", window=result_labelc)

result_labelf = tk.Label(window, text="")
result_labelf_window = canvas.create_window(50, 220, anchor="nw", window=result_labelf)

result_labelcont = tk.Label(window, text="")
result_labelcont_window = canvas.create_window(350, 180, anchor="nw", window=result_labelcont)

result_labels = tk.Label(window, text="")
result_labels_window = canvas.create_window(350, 220, anchor="nw", window=result_labels)

result_labelcond = tk.Label(window, text="")
result_labelcond_window = canvas.create_window(50, 260, anchor="nw", window=result_labelcond)


window.state('zoomed') 

# Start the Tkinter event loop
window.mainloop()