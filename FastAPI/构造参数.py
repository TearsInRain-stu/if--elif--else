# 构造URL
from fastapi import FastAPI,Path

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "welcome to my website"}

@app.get("/id/{id}")
async def get(id: int = Path(...,ge=1,le=100,description="新闻分类id")):# Path(...,校检)
    return {"news_id":id}

@app.get("/name/{name}")
async def get(name: str = Path(...,min_length=2,max_length=10,description="新闻分类名称")):
    return {"news_name":f"{name}"}
