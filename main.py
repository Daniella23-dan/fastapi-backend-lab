 from fastapi import FASTAPI

app = FastAPI()


@app.get("/")
def read_root():
   return {"meassage": "Welcome to the Student API"}



@app.get("/health")
def health_check():
     return {"status": "ok"}
