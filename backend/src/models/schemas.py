from pydantic import BaseModel, Field


class FibonacciRequest(BaseModel):
    """Schema for the request body of the /calculate endpoint."""

    number: int = Field(..., ge=0, le=100, description="The n-th number to calculate.")


class FibonacciResponse(BaseModel):
    """Schema for the response of the /calculate endpoint."""

    result: int = Field(..., description="The calculated Fibonacci number.")
    sequence: list[int] = Field(..., description="The 5 numbers preceding the result.")
