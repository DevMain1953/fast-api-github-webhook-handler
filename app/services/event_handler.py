from email import message
from fastapi import Request
from .message_sender import MessageSender


class GitHubEventHandler:
    def __init__(self):
        self.__message_sender = MessageSender()

    async def handle_push_event(self, request: Request):
        request_body = await request.json()

        pusher = request_body["sender"]["login"]
        pusher_url = request_body["sender"]["html_url"]
        repository_name = request_body["repository"]["name"]
        repository_url = request_body["repository"]["html_url"]
        commit_message = request_body["head_commit"]["message"]

        message = f"Push was executed by [{pusher}]({pusher_url}) to [{repository_name}]({repository_url}). \
            \n\n Commit message: {commit_message}."
        await self.__message_sender.send_message_to_telegram(message)
    
    async def handle_pull_request_event(self, request: Request):
        request_body = await request.json()

        pull_request_number = request_body["number"]
        if request_body["pull_request"]["merged"] == True:
            pull_request_action = "merged"
        pull_request_action = request_body["action"]
        pull_request_title = request_body["pull_request"]["title"]
        pull_request_description = request_body["pull_request"]["body"]
        pull_request_creator = request_body["sender"]["login"]
        pull_request_creator_url = request_body["sender"]["html_url"]
        pull_request_url = request_body["pull_request"]["html_url"]

        message = f"Pull Request [{pull_request_number}]({pull_request_url}) {pull_request_action} by [{pull_request_creator}]({pull_request_creator_url}). \
            \n\n Title: *{pull_request_title}* \n\n Description: **{pull_request_description}**"
        await self.__message_sender.send_message_to_telegram(message)

    async def handle_star_event(self, request: Request):
        request_body = await request.json()

        number_of_stars = request_body["repository"]["stargazers_count"]
        star_sender_username = request_body["sender"]["login"]
        repository_url = request_body["repository"]["html_url"]
        repository_name = request_body["repository"]["name"]

        message = f"{star_sender_username} has starred the [{repository_name}]({repository_url}). \n\n The Total Stars are {number_of_stars}"
        await self.__message_sender.send_message_to_telegram(message)