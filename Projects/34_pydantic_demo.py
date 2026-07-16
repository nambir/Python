"""Slide 34 — Pydantic practice. Requires: pip install pydantic"""
from pydantic import BaseModel, Field, ValidationError, field_validator


class CreateUser(BaseModel):
    email: str
    age: int = Field(ge=18, le=120)
    tags: list[str] = []

    @field_validator("email")
    @classmethod
    def normalize_email(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("invalid email")
        return v.lower()


def main() -> None:
    user = CreateUser.model_validate(
        {"email": "Anu@Example.COM", "age": "25"}
    )
    print("valid:", user.model_dump())

    try:
        CreateUser.model_validate({"email": "bad", "age": 10})
    except ValidationError as e:
        print("errors:", e.error_count())


if __name__ == "__main__":
    main()
