from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from api.router import api_router

app = FastAPI(
    title="Fibonacci Web Calculator",
    description="An API to calculate Fibonacci numbers and sequences.",
    version="1.0.0",
)


# Pydantic 유효성 검사 오류에 대한 전역 핸들러
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )


# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 오리진 허용 (개발용)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def read_root():
    """A simple endpoint to check if the API is running."""
    return {"status": "ok"}


app.include_router(api_router, prefix="/api")

# 정적 파일 서빙
app.mount("/", StaticFiles(directory="../frontend/public", html=True), name="static")
