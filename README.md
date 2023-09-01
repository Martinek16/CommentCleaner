# Comment and Empty Line Remover

## Introduction

This is a Python script that removes comments and empty lines from a source code file. It can be helpful when you want to clean up your code and remove unnecessary comments or whitespace. This script takes a source code file as input, duplicates it, removes comments and empty lines from the original file, and saves the cleaned code in the destination file.

## How to Use

Follow these steps to use the script:

### Prerequisites

- Python 3.x installed on your system.

### Steps

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where you have the script.

4. Run the script by executing the following command:

    ```bash
    python script.py
    ```

5. You will be prompted to enter the path to the file you want to duplicate and clean. Please provide the full path to the file, including its extension.

6. If the file exists, the script will duplicate it and save the duplicate in a "saved" folder (creating the folder if it doesn't exist).

7. The original file will be cleaned by removing comments and empty lines, and the cleaned code will replace the content of the original file.

8. Once the script finishes processing, you will see the message "DONE," indicating that the operation was successful.

### Example

Suppose you have a Python file named example.py with the following content:

```python
    # This is a comment
    def hello_world():
        print("Hello, World!")
    
    ''' This is a multi-line comment. It spans multiple lines. '''
    
    print("Another line")

# This is another comment
```



Running the script on this file will result in the following content in example.py:

```python
def hello_world():
    print("Hello, World!")

print("Another line")
```

###### NOTE:   Make sure to back up your code before using this script, as it will replace the content of the original file with the cleaned code.
