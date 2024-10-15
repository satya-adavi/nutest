import os

def read_input_from_file(file_path):
    if not os.path.exists(file_path):
        print("Please enter the correct path")
        return

    print(f"Reading from file: {os.path.abspath(file_path)}")

    with open(file_path, 'r') as f:
        inputs = [int(line.strip()) for line in f]

    return inputs if inputs else []
