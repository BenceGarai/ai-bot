import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    # kinda repeated code to please the cli test
    try:
        abs_working_directory = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_directory, file_path))
        valid_target_file = (
            os.path.commonpath([abs_working_directory, target_file])
            == abs_working_directory
        )
        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
    except Exception as e:
        return f"Error: {e}"


    try: 
        command = ["python", target_file]
        if args is not None:
           command.extend(args) 
        
        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30)
        
        output = ""
        if completed_process.returncode != 0:
            output +=  f"Process exited with code {completed_process.returncode}"
        if not completed_process.stdout or completed_process.stderr:
            output += "No output provided"
        else:
            if completed_process.stdout:
                output += f"STDOUT: {completed_process.stdout}"
            if completed_process.stdout:
                output += f"STDERR: {completed_process.stderr}"
        return output
    except Exception as e:
       return f"Error: executing Python file: {e}"