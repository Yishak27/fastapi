from fastapi import FastAPI

app = FastAPI()

@app.get("/registerUser")
def main():
    return "Hello fast api"