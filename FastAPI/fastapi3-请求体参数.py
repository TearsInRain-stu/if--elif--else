"""
书名：不能为空，长度2——20
作者：长度：2——10
出版社：默认值“黑马出版社
售价：不能为空；价格大于0元
"""


from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class Book(BaseModel):
    title: str = Field(...,min_length=2,max_length=20,description="用户名，长度要求在2~20") # Field(默认参数,校检)
    author: str = Field(...,min_length=2,max_length=10)
    publisher: str = Field("黑马程序员")
    price: int = Field(...,ge=0)


@app.get("/")
async def read_root():
    return {"Hello":"World"}

@app.post("/book")
async def new_book(book:Book):
    return book





