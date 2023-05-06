from pydantic import BaseModel, StrictStr, Field


class RegistrationModel(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr = Field(default='test_password')

