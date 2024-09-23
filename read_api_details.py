#To get url and api key details
def read_detail():
    details=[]
    # Open the file in read mode
    file = open("C:\\Users\\sendh\\Python\\VS Code Python\\Weather\\Details.txt", "r")

    # Read the file line by line
    for line in file:
        details.append(line.strip())

    # Close the file
    file.close()
    return details
