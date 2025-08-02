from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

class Contact(BaseModel):
    name: str
    phone: str
    email: str

contacts_db: Dict[str, Contact] = {}

@app.post("/contacts/")
def create_contact(contact: Contact):
    try:
        if contact.name in contacts_db:
            raise HTTPException(status_code=400, detail="Contact already exists")
        
        contacts_db[contact.name] = contact
        return {"message": f"Contact '{contact.name}' created successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create contact")

@app.get("/contacts/")
def get_contacts(name: Optional[str] = Query(None)):
    try:
        if name:
            if name not in contacts_db:
                raise HTTPException(status_code=404, detail="Contact not found")
            return contacts_db[name]
        else:
            return list(contacts_db.values())
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve contacts")

@app.post("/contacts/{name}")
def update_contact(name: str, contact: Contact):
    try:
        if name not in contacts_db:
            raise HTTPException(status_code=404, detail="Contact not found")
        
        contacts_db[name] = contact
        return {"message": f"Contact '{name}' updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update contact")

@app.delete("/contacts/{name}")
def delete_contact(name: str):
    try:
        if name not in contacts_db:
            raise HTTPException(status_code=404, detail="Contact not found")
        
        del contacts_db[name]
        return {"message": f"Contact '{name}' deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to delete contact")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)