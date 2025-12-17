from fastapi import FastAPI

app = FastAPI()

@app.get("/news")
async def get_news():
    return {"message": "Hello, News World!"}