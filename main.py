import shutil
import os
import re

def remove_comments_and_empty_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        # Remove single-line comments
        content = re.sub(r'#.*', '', content)

        # Remove multi-line comments
        content = re.sub(r"(\'\'\'(.*?)\'\'\'|\"\"\"(.*?)\"\"\")", '', content, flags=re.DOTALL)

        # Remove empty lines
        cleaned_lines = (line for line in content.splitlines() if line.strip())
        
        with open(file_path, 'w') as file:
            file.write('\n'.join(cleaned_lines))
    except Exception as e:
        print("Error removing comments and empty lines:", str(e))

def duplicate_file():
    source_path = input("Enter the path to the file you want to duplicate: ")
    
    if not os.path.exists(source_path):
        print("File does not exist.")
        return
    
    file_name = os.path.basename(source_path)
    destination_path = os.path.join("saved", file_name)
    
    if not os.path.exists("saved"):
        os.makedirs("saved")
    
    try:
        shutil.copy2(source_path, destination_path)
        
        remove_comments_and_empty_lines(source_path)
        print("DONE")
    except Exception as e:
        print("Error:", str(e))

duplicate_file()
