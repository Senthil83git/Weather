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