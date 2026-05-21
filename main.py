from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import shutil
import os
from model import model

app = FastAPI()

# Create uploads folder
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Serve frontend
@app.get("/")
def home():
    return FileResponse("static/index.html")

# 🔥 VERY IMPORTANT (serve YOLO output images)
app.mount("/results", StaticFiles(directory="runs/detect"), name="results")


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded image
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run YOLO prediction
    results = model(file_path, save=True)

    save_dir = str(results[0].save_dir)
    filename = os.path.basename(file_path)

    # Get last folder name (predict, predict2, etc.)
    folder_name = os.path.basename(save_dir)

    output_url = f"/results/{folder_name}/{filename}"

    return {"output_image": output_url}