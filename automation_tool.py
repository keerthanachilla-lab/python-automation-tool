
import os
import shutil

SOURCE_FOLDER = "input_files"
OUTPUT_FOLDER = "processed_files"


def organize_files():
    os.makedirs(SOURCE_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    files = os.listdir(SOURCE_FOLDER)

    if not files:
        print("No files found in the input folder.")
        return

    for file_name in files:
        source_path = os.path.join(SOURCE_FOLDER, file_name)

        if os.path.isfile(source_path):
            extension = os.path.splitext(file_name)[1].lower()

            if extension:
                folder_name = extension[1:] + "_files"
            else:
                folder_name = "other_files"

            destination_folder = os.path.join(OUTPUT_FOLDER, folder_name)
            os.makedirs(destination_folder, exist_ok=True)

            shutil.move(
                source_path,
                os.path.join(destination_folder, file_name)
            )

            print(f"Moved: {file_name} -> {folder_name}")

    print("Automation completed successfully!")


if __name__ == "__main__":
    organize_files()