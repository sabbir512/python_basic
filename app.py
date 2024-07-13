from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {'data': 'Welcome to the home page'}

@app.get("/contact")
def contact():
    return {'contact': '+91 63527 2343'}


uvicorn.run(app)
