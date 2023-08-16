
import json

from fastapi import FastAPI, Request, HTTPException
from pydantic_core import ValidationError
from validators import GoogleCodeValidator

app = FastAPI()

@app.post("/")
async def authentication_handler(request:Request):
    if not request.query_params:
        return {"message": 'what are you doing here? =.='}
    try:
        GoogleCodeValidator.model_validate(dict(request.query_params))
    except ValidationError as e:
        e = json.loads(e.json())
        raise HTTPException(status_code=422,detail=e)
    else:
        return {"message": 'passed'}
