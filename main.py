from fastapi import FastAPI


app = FastAPI(title="TestAPI");
@app.get("/")
def root():
    return {"message": "API is running"}