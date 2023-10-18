#!/usr/bin/python3

# Import libraries
import os
import subprocess

### Declare a function here
def dir_structure_print(directory_path):
    for (root, dirs, files) in os.walk(directory_path):
        print(f"==root==")
        print(root)
        print(f"==dirs==")
        print(dirs)
        print(f"==files==")
        print(files)

def dir_structure_output(directory_path):
    with open("dir_structure.txt", "w") as output_file:
        for (root, dirs, files) in os.walk(directory_path):
            output_file.write("==root==\n")
            output_file.write(root + "\n")
            output_file.write("==dirs==\n")
            output_file.write(", ".join(dirs) + "\n")
            output_file.write("==files==\n")
            output_file.write(", ".join(files) + "\n")
    print("Directory structure saved to 'dir_structure.txt'")
    # Open the text file with LibreOffice Writer
    subprocess.Popen(["libreoffice", "--writer", "dir_structure.txt"])

# Main
def main():
    user_input = input("Enter a directory path: ")
    dir_structure_print(user_input)
    dir_structure_output(user_input)

main()
