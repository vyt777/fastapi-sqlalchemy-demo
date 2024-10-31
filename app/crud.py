import models
from database import SessionLocal


def get_item(item_id: int):
    db = SessionLocal()
    try:
        item = db.query(models.Item).filter(models.Item.id == item_id).first()
    finally:
        db.close()
    return item


def get_items(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    try:
        items = db.query(models.Item).offset(skip).limit(limit).all()
    finally:
        db.close()
    return items


def create_item(name: str, description: str, price: float, tax: float):
    db = SessionLocal()
    try:
        item = models.Item(name=name, description=description, price=price, tax=tax)
        db.add(item)
        db.commit()
        db.refresh(item)
    finally:
        db.close()
    return item


def update_item(item_id: int, name: str = None, description: str = None, price: float = None, tax: float = None):
    db = SessionLocal()
    try:
        item = db.query(models.Item).filter(models.Item.id == item_id).first()
        if item is None:
            return False
        if name is not None:
            item.name = name
        if description is not None:
            item.description = description
        if price is not None:
            item.price = price
        if tax is not None:
            item.tax = tax
        db.commit()
        db.refresh(item)
    finally:
        db.close()
    return item


def delete_item(item_id: int):
    db = SessionLocal()
    try:
        item = db.query(models.Item).filter(models.Item.id == item_id).first()
        if item is None:
            return False
        db.delete(item)
        db.commit()
    finally:
        db.close()
    return item
