from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

app = FastAPI()

# CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_methods=["*"],
    allow_headers=["*"],
)

shapes = ["Circle", "Square", "Triangle", "Rectangle", "Star"]
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_path = Path(__file__).parent / "templates" / "index.html"
    return html_path.read_text()

@app.get("/api/shapes")
def get_shapes():
    return JSONResponse(content=shapes)

@app.get("/api/colors")
def get_colors():
    return JSONResponse(content=colors)

@app.post("/api/select")
def select_shape_color(shape: str, color: str):
    return JSONResponse(content={"selectedShape": shape, "selectedColor": color})

# Serve static files like HTML
app.mount("/templates", StaticFiles(directory="templates"), name="templates")