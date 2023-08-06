## About project

FastAPI server, provides asynchronous methods to handle GitHub events (for now):
- push
- pull request (also with ```merged``` action)
- star

When in your repository occurs one of these events you get message in your own Telegram bot, of course you need to create it or use another one.

## How to use

Create [webhook](https://docs.github.com/en/webhooks-and-events/webhooks/about-webhooks) in your repository, start the server (in virtual environment) ```uvicorn main:app --port <port>```, make sure GitHub can send request to your IP address, for example, you can use [ngrok](https://ngrok.com/download) for testing ```ngrok http <port>```.