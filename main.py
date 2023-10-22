from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, schema
import uvicorn 
from sqlalchemy import create_engine
from app.database import Base, SQLALCHEMY_DATABASE_URL
import os
import random
app = FastAPI()
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(bind=engine)




# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI MySQL App!"}


# Define API endpoints
@app.post("/items/")
def create_item(item: schema.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# New endpoint to get all items from the database
@app.get("/items_all/", response_model=list)
def get_all_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

@app.post("/generate_random_items/")
def generate_random_items(db: Session = Depends(get_db)):
    # Generate and insert a thousand random items
    for _ in range(1000):
        random_name = f"Item {random.randint(1, 1000)}"
        random_description = f"Description {random.randint(1, 1000)}"
        item = schema.ItemCreate(name=random_name, description=random_description)
        db_item = models.Item(**item.dict())
        db.add(db_item)
    db.commit()
    return {"message": "Thousand random items added to the database"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)