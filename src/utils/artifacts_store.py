import os

def get_logs_path():
    logs_dir = os.path.join('C:', 'Users', 'seerl', 'OneDrive', 'Desktop', 'project-1', 'src', 'utils')
    
    # Create the directory if it doesn't exist
    os.makedirs(logs_dir, exist_ok=True)
    
    # Define the log file path
    logs_path = os.path.join(logs_dir, 'logs.txt')
    
    # Create the log file if it doesn't exist
    if not os.path.exists(logs_path):
        open(logs_path, 'w').close()  # Create an empty log file
    
    return logs_path
