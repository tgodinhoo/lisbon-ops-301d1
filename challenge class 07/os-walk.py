#!/usr/bin/python3

# Import libraries
import os

### Declare a function here
def dir_structure(directory_path):
    for (root, dirs, files) in os.walk(directory_path):
        print(f"==root==")
        print(root)
        print(f"==dirs==")
        print(dirs)
        print(f"==files==")
        print(files)

# Main
def main():
    user_input = input("Enter a directory path: ")
    dir_structure(user_input)

main()
