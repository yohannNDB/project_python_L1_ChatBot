import os
import shutil

def toLowerCases(files):#take a list with all files path
    cleanedfiles=[]
    for file in files:
        file1 = open(file,'r')
        cleanedfile =[line[:-1] for line in file1]
        for elt in file1:
            if ord(elt)>=ord('A') and ord(elt)<ord('a'):
                elt.replace(elt,chr(ord(elt)+26))
    return 



def addToCleanedSpeeches(file_path):
    # Define the folder name
    folder_name = 'cleanedspeeches'
    
    # Check if the folder exists, create it if not
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    try:        
        file_name = os.path.basename(file_path)# Get the file name from the provided path
        destination_path = os.path.join(folder_name, file_name)# Create the destination path in the 'cleanedspeeches' folder
        
        # Copy the file to the destination folder
        shutil.copyfile(file_path, destination_path)
        
        print(f"File '{file_name}' added to 'cleanedspeeches' folder.")
    except Exception as e:
        print(f"Error: {e}")

def delete_punctation(cleanedfile):
    pass
