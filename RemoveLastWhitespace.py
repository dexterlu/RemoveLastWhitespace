import os

# Function to remove the last whitespace character from each line of a specified file
def remove_last_whitespace(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return

    # Open the input file for reading and an output file for writing
    with open(file_path, 'r', encoding='utf-8') as f_in, open('output.txt', 'w', encoding='utf-8') as f_out:
        # Read all lines from the input file
        lines = f_in.readlines()
        
        # Iterate through each line
        for line in lines:
            # Strip the line of trailing whitespace and write to the output file
            f_out.write(line.rstrip() + '\n')

# Ask user for the file path
input_file = input("Please enter the path of the file: ")
remove_last_whitespace(input_file)