import json
import os

APPLICATIONS_FILE = "applications.json"

def load_applications():
    try:
        if os.path.exists(APPLICATIONS_FILE):
            with open(APPLICATIONS_FILE, "r") as file:
                return json.load(file)
        return []
    except Exception:
        return []

def save_applications(applications):
    try:
        with open(APPLICATIONS_FILE, "w") as file:
            json.dump(applications, file, indent=2)
    except Exception as e:
        raise Exception("Failed to save applications to file")