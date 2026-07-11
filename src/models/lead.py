from pydantic import BaseModel, EmailStr


class Lead(BaseModel):
    """
    Represents a CRM Lead.
    """

    name: str
    phone: str
    email: EmailStr | None = None
    company: str | None = None
    business_type: str
    city: str
    notes: str | None = None