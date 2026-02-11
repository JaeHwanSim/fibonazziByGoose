# Tasks: Fibonacci Web Calculator

**Input**: Design documents from `/specs/002-fibonacci-web-calc/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/openapi.yaml, design.md

**Tests**: Unit tests are MANDATORY as per the project constitution (TDD). Every implementation task must be preceded by a test task.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story. Follow the Red-Green-Refactor cycle strictly.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create backend and frontend project structure per plan.md
- [ ] T002 Initialize Python environment and install dependencies (FastAPI, uvicorn, pytest)
- [ ] T003 [P] Configure pytest and linting tools (black, flake8) in backend/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [ ] T004 Setup FastAPI application entry point in `backend/src/main.py`
- [ ] T005 [P] Implement base API routing structure in `backend/src/api/router.py`
- [ ] T006 [P] Configure static file serving for frontend in `backend/src/main.py`
- [ ] T007 Setup global error handling and Pydantic validation error mapping in `backend/src/main.py`
- [ ] T008 [P] Create initial frontend structure (index.html, style.css) in `frontend/public/`

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Calculate N-th Fibonacci Number (Priority: P1) 🎯 MVP

**Goal**: 사용자가 0-100 사이의 숫자를 입력하면 N번째 피보나치 수를 계산하여 표시함.

**Independent Test**: `backend/tests/unit/test_calculator.py`를 실행하여 0, 1, 5, 10에 대한 계산값이 정확한지 확인.

### Tests for User Story 1 (MANDATORY - TDD) ⚠️

- [ ] T009 [P] [US1] Create unit tests for Fibonacci calculation logic in `backend/tests/unit/test_calculator.py`
- [ ] T010 [P] [US1] Create contract test for `/api/calculate` endpoint in `backend/tests/integration/test_api.py`

### Implementation for User Story 1

- [ ] T011 [P] [US1] Define `FibonacciRequest` and `FibonacciResponse` schemas in `backend/src/models/schemas.py`
- [ ] T012 [US1] Implement `FibonacciCalculator` class with iterative algorithm in `backend/src/core/calculator.py`
- [ ] T013 [US1] Implement POST `/api/calculate` endpoint in `backend/src/api/endpoints.py`
- [ ] T014 [US1] Create basic UI form for input and result display in `frontend/public/index.html`
- [ ] T015 [US1] Implement API call logic using Fetch API in `frontend/public/script.js`
- [ ] T016 [US1] Display calculation result and current timestamp on the web page

**Checkpoint**: User Story 1 is functional. Users can calculate and see the N-th Fibonacci number.

---

## Phase 4: User Story 2 - Input Validation and Context Sequence (Priority: P2)

**Goal**: 입력값 유효성 검사 및 결과와 함께 직전 5개의 수열을 표시함.

**Independent Test**: 브라우저에서 "-1" 또는 "101" 입력 시 오류 메시지가 나오는지 확인하고, "10" 입력 시 [5, 8, 13, 21, 34] 수열이 함께 나오는지 확인.

### Tests for User Story 2 (MANDATORY - TDD) ⚠️

- [ ] T017 [P] [US2] Add unit tests for `get_sequence` method in `backend/tests/unit/test_calculator.py`
- [ ] T018 [P] [US2] Add integration tests for invalid inputs (negative, >100, non-integer) in `backend/tests/integration/test_api.py`

### Implementation for User Story 2

- [ ] T019 [US2] Update `FibonacciCalculator` to include `get_sequence` method in `backend/src/core/calculator.py`
- [ ] T020 [US2] Update API endpoint to include context sequence in the response in `backend/src/api/endpoints.py`
- [ ] T021 [US2] Implement frontend validation for 0-100 range in `frontend/public/script.js`
- [ ] T022 [US2] Update UI to display the "Previous numbers" sequence in `frontend/public/index.html`
- [ ] T023 [US2] Implement user-friendly error message display in the UI

**Checkpoint**: User Story 2 is functional. Validation and context sequence are provided.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T024 [P] Apply CSS styling for a modern look in `frontend/public/style.css`
- [ ] T025 Add Docstrings and Type Hints across all Python files for documentation
- [ ] T026 [P] Final validation of `quickstart.md` steps
- [ ] T027 Final run of all tests using `pytest` to ensure 100% pass rate

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)** -> **Foundational (Phase 2)** -> **User Story 1 (Phase 3)** -> **User Story 2 (Phase 4)** -> **Polish (Phase 5)**

### Parallel Opportunities

- T003 (Backend config) and T008 (Frontend basic UI) can run in parallel.
- T009 and T010 (Tests for US1) can run in parallel.
- T011 (Schemas) can be done in parallel with Calculator logic (T012) initially, but T013 (Endpoint) depends on both.
- T017 and T018 (Tests for US2) can run in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Setup structure and FastAPI foundation.
2. Implement core Fibonacci calculation (P1).
3. Connect simple UI to API.
4. **Validate**: N-th number calculation works.

### Incremental Delivery

1. Once US1 is stable, add the context sequence logic.
2. Enhance UI for error handling and sequence display.
3. Apply final styling.
