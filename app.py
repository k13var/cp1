from fastapi import FastAPI, Depends, HTTPException, Header, Query
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from classifier.model import Model, get_model

app = FastAPI()


class SentimentRequest(BaseModel):
    text: str = Query(None, min_length=1)


class SentimentResponse(BaseModel):
    text: str
    sentiment: str


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: SentimentRequest, exc: RequestValidationError):
    return PlainTextResponse(str("Texte manquant"), status_code=HTTP_400_BAD_REQUEST)


@app.get("/welcome", status_code=HTTP_200_OK)
def welcome():
    result = {"Message": "Bonjour, ceci est la beta d'un algorithme d'analyse de sentiment"}
    return result


@app.post("/sentiment", response_model=SentimentResponse, status_code=HTTP_200_OK)
def sentiment(request: SentimentRequest, token: str = Header(...), model: Model = Depends(get_model)):
    if token != "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9":
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Token invalide!")

    text, prediction = model.predict(request.text)
    return SentimentResponse(text=text, sentiment=prediction)


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)
