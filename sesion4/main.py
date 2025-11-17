from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
from enum import Enum

#instanciamos la clase FastAPI
app = FastAPI()


#creamos nuestro primer modelo, reflejo de una tabla de la base de datos
class Post(BaseModel):
    author: str
    title: str
    content: str
class Role(str, Enum):
    admin = "admin"
    user = "user"
class User(BaseModel):
    id: Optional[UUID]=uuid4()
    first_name: str
    last_name: str
    city: str
    roles: List[Role]


@app.get("/")
async def root():
    return {"name": "Carlos Balvin Alvarez"}

@app.get("/posts/{id}")
async def getPost(id):
    return {"data": id}

@app.post('/posts')
async def viewPost(post: Post):
    return {"alert": f"El post de {post.title} ha sido agregado a la biblioteca"}

@app.post("/api/v1/add_user")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.get("/api/v1/users")    # para usarlo en el navegador
def get_all_users():
    return db

@app.delete("/api/v1/users/{id}")
def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": f"El usuario {user.first_name} ha sido eliminado"}

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Alan",
        last_name="Garcia",
        city="Lima",
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Alejandro",
        last_name="Toledo",
        city="Cabana",
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Ollanta",
        last_name="Humala",
        city="Tingo Maria",
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Pedro",
        last_name="Castillo",
        city="Cajamarca",
        roles=[Role.user, Role.admin]
    ),

]