# File Read & Write Challenge

# Read content from an existing file and write modified content to a new file.
def read_and_write_files(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Content from {input_file} has been modified and saved to {output_file}.")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except IOError:
        print("An I/O error occurred while accessing the files.")

# Test the function
read_and_write_files('input.txt', 'output.txt')


# Error Handling Lab

def read_user_file():
    filename = input("Enter the filename: ")
    
    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except IOError as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_user_file()