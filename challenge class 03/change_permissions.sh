#!/bin/bash

# Prompts user for input directory path
read -p "Enter the directory path: " dir_path

# Prompts user for input permissions number
read -p "Enter the permissions number: " permissions

# Change permissions for all files in the directory
find "$dir_path" -type f -exec chmod "$permissions" {} \;

# Print the directory contents and respective permissions
echo "Directory contents:"
ls -l "$dir_path"