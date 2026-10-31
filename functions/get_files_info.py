import os


def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        abs_working_directory = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_directory, directory))
        valid_target_dir = (
            os.path.commonpath([abs_working_directory, target_dir])
            == abs_working_directory
        )
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
    except Exception as e:
        return f"Error: {e}"
    
    # Iterate over items in the directory
    directory_items = os.listdir(target_dir)
    item_info = []
    try:
        for item in directory_items:
            item_info.append(f'- {item}: file_size={os.path.getsize(os.path.join(target_dir, item))} bytes, is_dir={os.path.isdir(os.path.join(target_dir, item))}')
    except Exception as e:
        return f"Error listing files: {e}"
    return " ".join(item_info)
