#!/usr/bin/python3

#Import libraries
import os
import subprocess

###Declare a function here
#Print directory structure
def dir_structure_print(directory_path):
    for (root, dirs, files) in os.walk(directory_path):
        print(f"==root==")
        print(root)
        print(f"==dirs==")
        print(dirs)
        print(f"==files==")
        print(files)

#Create and open dir_structure.txt file
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

#Create test directory
def create_test_dir_structure(base_path, dirname):
    test_directory = os.path.join(base_path, dirname)
    os.makedirs(test_directory)

    for i in range(1, 4):
        subdirectory_name = f"{dirname}_{i}"
        subdirectory_path = os.path.join(test_directory, subdirectory_name)
        os.makedirs(subdirectory_path)

#Main
def main():
    user_input = input("Enter a directory path: ")
    dir_structure_print(user_input)
    dir_structure_output(user_input)
    test_dir_name = input("Enter a name for the test directory: ")
    create_test_dir_structure(user_input, test_dir_name)
    print(f"Your {test_dir_name} folders have been created!")

main()
