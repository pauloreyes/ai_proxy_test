from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os

app = FastAPI(title="Zscaler Test API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API v1 Router
v1_router = APIRouter(prefix="/api/v1")

@v1_router.get("/chat")
async def chat_test():
    return {
        "status": "success",
        "message": "Connected to API v1 successfully!",
        "version": "v1",
        "zscaler_test": "passed"
    }

@v1_router.post("/chat")
async def chat_post_test(payload: dict):
    return {
        "status": "success",
        "received_payload": payload,
        "message": "Payload delivered successfully!"
    }

# Include routers
app.include_router(v1_router)

@app.get("/")
async def root():
    return FileResponse("index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
