import os
from config import MAX_CHARACTERS


def get_file_content(working_directory, file_path):
    abs_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_file_path, "r") as f:
            file_content = f.read(MAX_CHARACTERS)

            if os.path.getsize(abs_file_path) > MAX_CHARACTERS:
                file_content += (f'[...File "{file_path}" truncated at 10000 characters]')

        return file_content
    except OSError as e:
        return f"Error reading file {file_path}: {e}"
