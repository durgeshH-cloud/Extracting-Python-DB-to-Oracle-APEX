from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API is running!"}

# Create item
# @app.post("/items", response_model=schemas.ItemResponse)
@app.post("/items")
#def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
def create_item(name: str, category: str, db: Session = Depends(get_db)):
#    db_item = models.Item(**item.dict())
    item = models.Item(name=name, category=category)
#    db.add(db_item)
    db.add(item)
    db.commit()
#    db.refresh(db_item)
    db.refresh(item)
#    return db_item
    return item

# Get all items
@app.get("/items")
def get_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()

# Get item by ID
# @app.get("/items/{item_id}")
# def get_item(item_id: int, db: Session = Depends(get_db)):
   # return db.query(models.Item).filter(models.Item.id == item_id).first()