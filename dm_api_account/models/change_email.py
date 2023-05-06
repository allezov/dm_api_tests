from pydantic import BaseModel, StrictStr


class ChangeEmail(BaseModel):
    login: StrictStr
    password: StrictStr
    email: StrictStr
