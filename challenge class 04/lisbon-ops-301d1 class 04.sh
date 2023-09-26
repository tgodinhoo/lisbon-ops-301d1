#!/bin/bash

while true; do
    clear  # Clear the screen for a clean menu display

    # Display the options
    echo "1. Hello world (prints 'Hello world!' to the screen)"
    echo "2. Ping self (pings this computer's loopback address)"
    echo "3. IP info (print the network adapter information for this computer)"
    echo "4. Exit"

    # Prompt the user for their choice
    read -p "Enter your choice (1/2/3/4): " choice

    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1  # Ping the loopback address
            ;;
        3)
            ifconfig  # Display network adapter information
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a valid option (1/2/3/4)."
            ;;
    esac

    # Pause to allow the user to read the output before clearing the screen
    read -p "Press Enter to continue..."
done
