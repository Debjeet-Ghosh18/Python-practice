import os

def print_directory_contents(directory):
    try:
        # Get the list of all files and directories
        items = os.listdir(directory)
        print(f"Contents of '{directory}':")
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory}'.")

# Example usage:
directory_path = "."  # Current directory
print_directory_contents(directory_path)
