import uvicorn
from fastapi import FastAPI
from src.routers import weather

app = FastAPI()
app.include_router(weather.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Weather API!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)