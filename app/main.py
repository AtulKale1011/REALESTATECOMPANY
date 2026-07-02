from fastapi import FastAPI, status

app = FastAPI()

@app.get('/')
def health_check():
    return {"message": "Server is Running..."}, status.HTTP_200_OK