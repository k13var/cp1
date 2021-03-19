# Sentiment analysis application for restaurant reviews

This project is part of the *Case study no. 1 (ref. E2):  Artificial Intelligence application assessment* for the Data Science and Artificial Intelligence professional training.

## Installation

Clone this repo `git clone https://github.com/k13var/cp1.git`

Install the dependencies `pip install -r requirements.txt`

The project was made with python 3.8.5

## Run the FastAPI application

1. Open a terminal at root folder and type `uvicorn app:app` to run the live server


2. Open the browser at `http://127.0.0.1:8000/docs` where the app is being served, in the local machine


3. To test the application:
    * copy and paste `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9` in the `token` field
    * copy and paste `{"text": "très bien"}` in the `Request body`
    

4. The response should be `{"text": "très bien", "sentiment": "Positif"}`

