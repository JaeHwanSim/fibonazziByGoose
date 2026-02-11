from fastapi import APIRouter, Body
from models.schemas import FibonacciRequest, FibonacciResponse
from core.calculator import FibonacciCalculator

router = APIRouter()
calculator = FibonacciCalculator()


@router.post("/calculate", response_model=FibonacciResponse)
def calculate_fibonacci(
    request: FibonacciRequest = Body(..., description="The number to calculate.")
):
    """
    Calculates the n-th Fibonacci number and its preceding sequence.
    """
    result = calculator.calculate(request.number)
    sequence = calculator.get_sequence(request.number)
    return FibonacciResponse(result=result, sequence=sequence)
