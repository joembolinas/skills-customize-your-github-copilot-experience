# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Implement a simple REST API using the FastAPI framework, practicing routing, request/response models, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Basics: Routes & Models

#### Description
Set up a FastAPI application with core endpoints and Pydantic models for structured requests and responses.

#### Requirements
Completed program should:

- Create an app in `main.py` using FastAPI
- Add a health check route: `GET /health` returning `{ "status": "ok" }`
- Define a `Item` Pydantic model with fields: `id: int`, `name: str`, `price: float`, `in_stock: bool = True`
- Implement `GET /items` to list all items
- Implement `GET /items/{id}` to get a single item by id (404 if missing)


### 🛠️ CRUD: Create, Update, Delete

#### Description
Implement data mutations with proper validation and responses. Use an in-memory list/dict for storage.

#### Requirements
Completed program should:

- Implement `POST /items` to create an item (auto assign id, return created item)
- Implement `PUT /items/{id}` to update an item (return updated item)
- Implement `DELETE /items/{id}` to delete an item (return `{ "deleted": id }`)
- Validate inputs and return appropriate status codes (201, 200, 404, 422)
- Optional: Add pagination to `GET /items` (query params `skip`, `limit`)
