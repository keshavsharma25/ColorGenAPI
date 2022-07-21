from fastapi import FastAPI
from route.route import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import responses

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return responses.RedirectResponse("/docs")


app.include_router(router)
