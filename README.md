# Python Automation Tool

## Description
This project is a Python automation tool that organizes files automatically based on their file type.

## How It Works
1. The program checks the `input_files` folder.
2. It identifies the file type using the file extension.
3. It creates separate folders inside `processed_files`.
4. It moves each file into the appropriate folder.
5. This reduces repetitive manual file organization.

## How to Run

1. Make sure Python is installed.
2. Keep `automation_tool.py` in the project folder.
3. Run the following command:

python automation_tool.py

4. Place files that you want to organize inside the `input_files` folder.
5. Run the program again.
6. The organized files will appear inside the `processed_files` folder.

## Example

Input:
- photo.jpg
- document.pdf
- notes.txt

Output:
- processed_files/jpg_files/photo.jpg
- processed_files/pdf_files/document.pdf
- processed_files/txt_files/notes.txt

## Technologies Used
- Python
- os module
- shutil module

## Author
Keerthana