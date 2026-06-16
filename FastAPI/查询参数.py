# 对资源过滤，查找与分页
from fastapi import FastAPI,Query

app1 = FastAPI()

@app1.get("/")
async def main():
    return {"message" : "welcome to my website"}

@app1.get("/book_list") # 声名的参数不是路径参数，会自动转化为查询参数
async def get_book_list(
        book_list=Query("python project",max_length=255,min_length=5),
        # 类型注释Query(...or默认函数，校检)

        price: int=Query(...,le=100,ge=50)):
    return {"book_list":book_list,"price":price}
