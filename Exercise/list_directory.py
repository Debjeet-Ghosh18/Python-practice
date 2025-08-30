import os

def print_directory_contents(directory):
    try:
        # list all files and folders inside given directory
        items = os.listdir(directory)
        print(f"Contents of '{directory}':")
        for item in items:
            print(item)
    except FileNotFoundError:      # if directory path does not exist
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:        # if no permission to access folder
        print(f"Permission denied to access the directory '{directory}'.")

# Example usage
directory_path = "."   # "." means current working directory
print_directory_contents(directory_path)
