from fastapi import FastAPI, HTTPException
import os
from note import Note, get_file_path

app = FastAPI()

@app.post("/notes/")
def create_note(note: Note):
    try:
        file_path = get_file_path(note.title)
        
        if os.path.exists(file_path):
            raise HTTPException(status_code=400, detail="Note with this title already exists")
        
        with open(file_path, "w") as file:
            file.write(note.content)
        
        return {"message": f"Note '{note.title}' created successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create note")

@app.get("/notes/{title}")
def get_note(title: str):
    try:
        file_path = get_file_path(title)
        
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="Note not found")
        
        with open(file_path, "r") as file:
            content = file.read()
        
        return {"title": title, "content": content}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to read note")

@app.post("/notes/{title}")
def update_note(title: str, note: Note):
    try:
        file_path = get_file_path(title)
        
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="Note not found")
        
        with open(file_path, "w") as file:
            file.write(note.content)
        
        return {"message": f"Note '{title}' updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update note")

@app.delete("/notes/{title}")
def delete_note(title: str):
    try:
        file_path = get_file_path(title)
        
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="Note not found")
        
        os.remove(file_path)
        
        return {"message": f"Note '{title}' deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to delete note")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)