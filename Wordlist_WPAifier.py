import os
from tqdm import tqdm

def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            if len(line.strip()) >= 8:
                output_file.write(line)

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_list = [file_name for file_name in os.listdir(input_folder) if file_name.endswith('.txt')]

    for file_name in tqdm(file_list, desc="Processing files"):
        input_file_path = os.path.join(input_folder, file_name)
        output_file_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}_WPA.txt")
        process_file(input_file_path, output_file_path)

def main():
    input_folder = input("Enter the input folder location: ")
    output_folder = input("Enter the output folder location: ")

    process_folder(input_folder, output_folder)
    print("Processing complete.")

if __name__ == "__main__":
    main()
