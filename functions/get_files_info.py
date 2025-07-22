import os


def get_files_info(working_directory, directory="."):
    abs_path = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, directory))

    if not target_path.startswith(abs_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files_info = []

        for file in os.listdir(target_path):
            file_path = os.path.join(target_path, file)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            files_info.append(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(files_info)
    except OSError as e: 
        return f"Error: {e}"
