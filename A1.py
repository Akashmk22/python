import zipfile
import os

def zip_folder(folder_path, output_path):
    # Get the directory name and the name for the output zip file
    directory_name = os.path.basename(folder_path)
    zip_file_name = directory_name + '.zip'

    # Create a ZipFile object with the output path and the zip file name
    with zipfile.ZipFile(output_path + '\\' + zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the directory and add all files and directories to the zip file
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file))

if __name__ == '__main__':
    folder_path = 'output'
    output_path = 'C:/Users/Akash M K/Desktop/output22' # Change this to the directory where you want to save the zip file
    zip_folder(folder_path, output_path)
