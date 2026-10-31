import os
from config import *

def get_file_content(working_directory: str, file_path: str) -> str:
    # Check if path is valid
    try:
        abs_working_directory = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_directory, file_path))
        valid_target_file = (
            os.path.commonpath([abs_working_directory, target_file])
            == abs_working_directory
        )
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    except Exception as e:
        return f"Error: {e}"

    # Read file
    try:
        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
    except Exception as e:
        return f"Error: {e}"