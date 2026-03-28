import os
import json
import logging
from datetime import datetime
from pathlib import Path

def setup_logger(log_file_path):
    """Configures logging to the daily markdown file."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        handlers=[logging.FileHandler(log_file_path, mode='a')]
    )

def get_config(config_path="config.json"):
    """Loads configuration from a JSON file."""
    if not os.path.exists(config_path):
        default_config = {
            "watch_directories": ["./src"],
            "tracked_extensions": [".py", ".md", ".txt"],
            "log_file": "activity_log.md"
        }
        with open(config_path, 'w') as f:
            json.dump(default_config, f, indent=4)
        return default_config
    
    with open(config_path, 'r') as f:
        return json.load(f)

def format_log_entry(file_path, event_type):
    """Formats the file system event into a markdown string."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"## {timestamp}\n- **Action:** {event_type.upper()}\n- **File:** `{file_path}`\n"

def append_to_log(log_path, content):
    """Appends content to the specified markdown log file."""
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(content + "\n")
    except IOError as e:
        print(f"Error writing to log file: {e}")

def validate_path(path_str):
    """Checks if a directory path exists."""
    path = Path(path_str)
    return path.exists() and path.is_dir()