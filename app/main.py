from fastapi import FastAPI, Request
import httpx
import os
from services import GitHubEventHandler

app = FastAPI()
event_handler = GitHubEventHandler()


@app.post("/hook")
async def receive_web_hook_from_github(request: Request):
    github_event = request.headers.get("X-Github-Event")
    if github_event == "star":
        await event_handler.handle_star_event(request)
    if github_event == "pull_request":
        await event_handler.handle_pull_request_event(request)
    if github_event == "push":
        await event_handler.handle_push_event(request)