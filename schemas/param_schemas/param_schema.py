


from pydantic import BaseModel, Field

class ParamObj(BaseModel):
    name: str = Field(..., min_length=3, max_length=15)
    password: int = Field(..., ge=10000)
    