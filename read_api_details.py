import os
#To get url and api key details

def read_detail():
    details=[]
        
        # Get the directory where the script is located
    curr_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the relative path to a file located in the same directory
    fi_path = os.path.join(curr_dir, "data", "Details.txt")
    # Open the file in read mode
    file = open(fi_path, "r")

    # Read the file line by line
    for line in file:
        details.append(line.strip())

    # Close the file
    file.close()
    return details
