import datetime

from pydantic import BaseModel, field_validator, ConfigDict
from typing import Union

class GoogleCodeValidator(BaseModel):
    error: Union[str, None] = None
    code: Union[str, None] = None

    model_config = ConfigDict(extra='forbid')

    @field_validator('error')
    @classmethod
    def response_contains_error(cls, value: str) -> str:
        if value:
            raise ValueError(f"Parameter 'error' in Google API response: '{value}'")
        return value

    @field_validator('code')
    @classmethod
    def code_must_be_long(cls, value: str) :
        if not 60 <= len(value) <= 85:
            raise ValueError("code 60 <= len(value) <= 85")
        file = open('authorization_codes.txt', 'a+')
        file.write(str(datetime.datetime.now()) + ";" + value + '\n')  # add auth code to authorization_codes.txt for debugging purposes
        file.close()
        return value
