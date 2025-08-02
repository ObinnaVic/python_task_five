from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import file_handler

app = FastAPI()

class JobApplication(BaseModel):
    name: str
    company: str
    position: str
    status: str

@app.post("/applications/")
def create_application(application: JobApplication):
    try:
        applications = file_handler.load_applications()
        applications.append(application.dict())
        file_handler.save_applications(applications)
        return application
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create application")

@app.get("/applications/")
def get_all_applications():
    try:
        applications = file_handler.load_applications()
        return applications
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve applications")

@app.get("/applications/search")
def search_applications(status: str):
    try:
        applications = file_handler.load_applications()
        filtered_applications = []
        for app in applications:
            if app.get("status", "").lower() == status.lower():
                filtered_applications.append(app)
        return filtered_applications
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to search applications")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)