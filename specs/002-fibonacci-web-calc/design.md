# Design: Fibonacci Web Calculator

## 1. System Architecture

사용자가 웹 브라우저를 통해 요청을 보내면, FastAPI 백엔드가 이를 수신하여 도메인 로직(Calculator)을 통해 계산한 뒤 결과를 반환하는 구조입니다.

### Sequence Diagram (PlantUML)

```plantuml
@startuml
actor User
participant "Web Browser" as Browser
participant "FastAPI App" as API
participant "FibonacciCalculator" as Calc

User -> Browser : Enter n (0-100)
User -> Browser : Click "Calculate"
Browser -> API : POST /api/calculate {n}
API -> API : Validate Input (0 <= n <= 100)
alt valid input
    API -> Calc : calculate(n)
    Calc --> API : result (F(n))
    API -> Calc : get_sequence(n, 5)
    Calc --> API : sequence [F(n-5)...F(n-1)]
    API --> Browser : 200 OK {result, sequence}
    Browser -> User : Display result and sequence
else invalid input
    API --> Browser : 400 Bad Request {error_message}
    Browser -> User : Show error message
end
@enduml
```

## 2. Class Design

객체지향 원칙을 준수하여 계산 로직을 캡슐화합니다.

### Class Diagram (PlantUML)

```plantuml
@startuml
class FibonacciCalculator {
    + calculate(n: int) : int
    + get_sequence(n: int, count: int) : List[int]
}

class FibonacciAPI {
    - calculator : FibonacciCalculator
    + calculate_endpoint(request: FibonacciRequest) : FibonacciResponse
}

class FibonacciRequest {
    + n : int
}

class FibonacciResponse {
    + requested_n : int
    + result : string
    + sequence : List[string]
    + timestamp : datetime
}

FibonacciAPI o-- FibonacciCalculator : uses
FibonacciAPI ..> FibonacciRequest : accepts
FibonacciAPI ..> FibonacciResponse : returns
@enduml
```

## 3. UI Layout Sketch

- **Header**: "Fibonacci Web Calculator"
- **Input Section**: 
  - Label: "Enter a number (0-100):"
  - Input: `[ Number Input ]`
  - Button: `[ Calculate ]`
- **Result Section**:
  - Main Display: "Result: F(n) = {result}"
  - Sequence Display: "Previous numbers: {F(n-5), ..., F(n-1)}"
- **Error Display**: Red text below input field for validation errors.
