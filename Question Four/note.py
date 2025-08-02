from pydantic import BaseModel
import os

class Note(BaseModel):
    title: str
    content: str

NOTES_DIR = "notes"

try:
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)
except Exception:
    pass

def get_file_path(title: str):
    safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
    return os.path.join(NOTES_DIR, f"{safe_title}.txt")