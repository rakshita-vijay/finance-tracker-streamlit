import os

def get_user_file(username, suffix):
    """Returns the full path for a user's file with the given suffix."""
    return os.path.join("saved_files", username, f"{username}_{suffix}")

def ensure_user_dir(username):
    os.makedirs(os.path.join("saved_files", username), exist_ok=True)
