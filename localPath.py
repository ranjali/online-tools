import os
import sys

def replace_string_in_files(folder_path, search_string, replacement_string):
    # Iterate through all files and subfolders in the provided directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            try:
                # Open the file and read its content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace the old string with the new one
                new_content = content.replace(search_string, replacement_string)
                
                # If content has changed, write the new content back to the file
                if content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")
            except Exception as e:
                # Print error message but continue with the next file
                print(f"Error processing {file_path}: {e}")

def find_index_html(start_folder, replacement_string):
    """
    Traverse the given folder and its subfolders to find `index.html`.
    Print the relative path from the start folder to the folder containing `index.html`.

    :param start_folder: The starting folder to parse.
    """
    start_folder = os.path.abspath(start_folder)
    for root, dirs, files in os.walk(start_folder):
        if 'index.html' in files:
            relative_path = os.path.relpath(root, start_folder)
            if relative_path != ".":
                print(relative_path)
                replace_in_files(start_folder, 'href="' + relative_path + '/"', 'href="' + replacement_string + '/' + relative_path + '/index.html"')
                replace_in_files(start_folder, "href = '/online-tools/" + relative_path + "/'", "href = '" + replacement_string + '/' + relative_path + "/index.html'")
                replace_in_files(start_folder, 'url=/online-tools/' + relative_path + '/"', 'url="' + replacement_string + '/' + relative_path + '/index.html"')
                # return

def replace_in_files(start_folder, search_string, replacement_string):
    # Traverse through the folder and its subfolders
    print(f"search_string: {search_string}")
    print(f"replacement_string: {replacement_string}")
    for root, dirs, files in os.walk(start_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                # Open file and read its content
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Replace search_string with replacement_string
                if search_string in content:
                    new_content = content.replace(search_string, replacement_string)
                    
                    # Write the modified content back to the file
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    print(f"Replaced content in file: {file_path}")
                    # return
            
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_index_html.py <folder>")
        sys.exit(1)

    start_folder = sys.argv[1]
    replacement_string = sys.argv[1]

    if not os.path.isdir(start_folder):
        print(f"Error: {start_folder} is not a valid folder.")
        sys.exit(1)

    replace_string_in_files(start_folder, "https://emn178.github.io/online-tools", "file:///Users/hranjali/proj/online-tools")
    replace_string_in_files(start_folder, 'img src="images', 'img src="img src="file:///Users/hranjali/proj/online-tools/images')
    replace_string_in_files(start_folder, "'js/", "'file:///Users/hranjali/proj/online-tools/js/")
    replace_string_in_files(start_folder, 'href="css', 'href="file:///Users/hranjali/proj/online-tools/css')
    replace_string_in_files(start_folder, 'href="/online-tools', 'href="file:///Users/hranjali/proj/online-tools')

    # comment out long processing
    # find_index_html(start_folder, replacement_string)
