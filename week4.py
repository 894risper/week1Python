def file_read_write():
    try:
        # Ask user for the input file name
        input_file = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"Modified content written to '{output_file}'")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename.")
    except IOError:
        print("Error: Unable to read or write the file.")


# Run the program
file_read_write()
