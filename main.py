import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes import router

app = FastAPI()
app.include_router(router)

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    except KeyboardInterrupt:
        print("Application shutdown gracefully")