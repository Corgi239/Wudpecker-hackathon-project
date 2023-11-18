"""
This is the main file for the project.
"""

import uvicorn
from fastapi import FastAPI
from src import logic

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/array")
async def array():
    test_arr = logic.example_func()
    print(test_arr)
    return {"message": test_arr.tolist()}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="127.0.0.1")
