# Data Model: Fibonacci Web Calculator

## Entities

### FibonacciRequest (Pydantic Model)
- **Description**: 사용자의 계산 요청 데이터
- **Fields**:
  - `n` (Integer): 계산하고자 하는 순번.
- **Validation**:
  - `0 <= n <= 100`

### FibonacciResponse (Pydantic Model)
- **Description**: 계산 결과 데이터
- **Fields**:
  - `requested_n` (Integer): 요청받은 $n$
  - `result` (String): $F(n)$의 값. (매우 클 수 있으므로 String으로 전달 권장)
  - `sequence` (List[String]): $[F(n-5), \dots, F(n-1)]$ 순열.
  - `timestamp` (DateTime): 계산 완료 시각.

### ErrorResponse (Pydantic Model)
- **Description**: 오류 발생 시 반환되는 데이터
- **Fields**:
  - `error_code` (String): 오류 유형 (예: `INVALID_INPUT`, `OUT_OF_RANGE`)
  - `message` (String): 사용자 친화적인 오류 메시지.

## Logic Classes

### FibonacciCalculator (Domain Service)
- **Responsibility**: 피보나치 수열 계산 알고리즘 구현.
- **Methods**:
  - `calculate(n: int) -> int`: 단일 값 계산.
  - `get_sequence(n: int, count: int) -> List[int]`: 특정 범위의 수열 계산.
