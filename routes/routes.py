from fastapi import APIRouter
from starlette.responses import JSONResponse

from helper.helper import get_all_pull_request
from models.github_model import GithubCodeAnalyze

router = APIRouter()


@router.post("/analyze-pr", response_model=dict)
async def github_analyze(pr_data: GithubCodeAnalyze):
    data = get_all_pull_request(pr_data)
    return JSONResponse({"pr": data})
