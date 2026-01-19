# Fast API
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return{"status":"Fast Api is live"}
# on a local machine
# python.exe -m uvicorn main:app --reload // Start api on desktop
# git init
# git add .
# git commit -m "first fastapi test"
# git branch -M main
# git remote add origin https://github.com/YOUR_USERNAME/insurance_api.git
# git push -u origin main
