import os
from config import MAX_CHARS    
def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        if os.path.abspath(working_directory) not in os.path.abspath(full_path):
                return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
                return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(full_path, "r") as f:
            print("Reading file:", full_path)
            file_content_string = f.read()
            print(f"File content length: {len(file_content_string)} characters")
            return_string = file_content_string[:MAX_CHARS] + f'\n[...File "{file_path}" truncated at 10000 characters]' if len(file_content_string) > MAX_CHARS else file_content_string
            return return_string
    except Exception as e:
        return f'Error: {str(e)}'