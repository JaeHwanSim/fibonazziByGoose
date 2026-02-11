# Research: Fibonacci Web Calculator

## 1. Web Framework & Static File Serving

- **Decision**: `FastAPI` + `StaticFiles` mount
- **Rationale**: FastAPI는 고성능 비동기 처리를 지원하며, `fastapi.staticfiles`를 통해 HTML/JS 파일을 간편하게 서빙할 수 있음. 별도의 웹 서버(Nginx 등) 없이 단일 Python 프로세스로 프로토타입 구현 가능.
- **Alternatives**:
  - **Flask**: 간단하지만 비동기 처리가 기본이 아니며 최신 표준(Pydantic) 활용도가 낮음.
  - **Streamlit**: 매우 빠르지만 커스텀 UI/UX 구현에 제약이 있음.

## 2. Fibonacci Algorithm for n=100

- **Decision**: 반복문(Iterative) 방식 또는 메모이제이션(Memoization)을 사용한 계산.
- **Rationale**: 
  - 단순 재귀(Naive Recursion)는 $O(2^n)$의 시간 복잡도를 가지므로 n=100 계산 불가. 
  - 반복문은 $O(n)$으로 즉시 계산 가능.
  - Python은 임의 정밀도 산술(Arbitrary-precision arithmetic)을 지원하므로 n=100 결과값($354,224,848,179,261,915,075$)을 오버플로 없이 정확히 처리할 수 있음.
- **Alternatives**:
  - **Matrix Exponentiation**: $O(\log n)$으로 더 빠르지만 n=100 수준에서는 구현 복잡도 대비 이득이 크지 않음.

## 3. UI/UX Design Patterns

- **Decision**: Fetch API를 사용한 Single Page Application (SPA) 스타일.
- **Rationale**: 페이지 새로고침 없이 사용자 입력을 서버로 전송하고 결과를 즉시 반영하여 매끄러운 경험 제공.
- **Result Format**: 
  - 메인 결과: $F(n)$
  - 컨텍스트: $[F(n-5), F(n-4), F(n-3), F(n-2), F(n-1)]$
