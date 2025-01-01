from pydantic import BaseModel, HttpUrl


class GithubCodeAnalyze(BaseModel):
    repo_url: HttpUrl = "https://github.com/{OWNER}/{repo}"  # Placeholder URL
    pr_number: int
    github_token: str
