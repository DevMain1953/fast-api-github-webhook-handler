import httpx
import os


class MessageSender:
    def __init__(self):
        self.__token = os.getenv("TOKEN")
        self.__chat_id = os.getenv("CHAT_ID")
    
    async def send_message_to_telegram(self, message: str):
            message_for_telegram_bot = {"chat_id": self.__chat_id, "text": message, "parse_mode": "Markdown"}
            url_to_telegram_send_message_endpoint = f"https://api.telegram.org/bot{self.__token}/sendMessage"
            async with httpx.AsyncClient() as client:
                await client.post(url_to_telegram_send_message_endpoint, json=message_for_telegram_bot)