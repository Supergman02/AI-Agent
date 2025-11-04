import os
def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        print(f"Results for listing files in: {full_path}")
        if os.path.abspath(working_directory) not in os.path.abspath(full_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        directory_contents = os.listdir(full_path)
        return_string = ""
        for item in directory_contents:
            return_string += f"- {item}: file_size{os.path.getsize(os.path.join(full_path, item))}, is_dir={os.path.isdir(os.path.join(full_path, item))}\n"
        return return_string
    except Exception as e:
        return f"Error: {str(e)}"

