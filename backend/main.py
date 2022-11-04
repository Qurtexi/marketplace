from fastapi import FastAPI

from os import environ
import databases
from sqlalchemy import desc, select

from models.database import database
from models.posts import posts_table
from models.users import users_table
from routers import users, posts


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def read_root():
    query = (
        select(
            [
                posts_table.c.id,
                posts_table.c.created_at,
                posts_table.c.title,
                posts_table.c.content,
                posts_table.c.user_id,
                users_table.c.name.label("user_name"),
            ]
        )
        .select_from(posts_table.join(users_table))
        .order_by(desc(posts_table.c.created_at))
    )
    return await database.fetch_all(query)

app.include_router(users.router)
app.include_router(posts.router)
