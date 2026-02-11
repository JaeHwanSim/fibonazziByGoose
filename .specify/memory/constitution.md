<!--
Sync Impact Report
- Version change: N/A → 1.0.0
- List of modified principles:
  - Added: I. Object-Oriented Programming (OOP)
  - Added: II. Python as Primary Language
  - Added: III. Test-Driven Development (TDD)
  - Added: IV. Automated Test Execution & Feedback Loop
  - Added: V. Clean Code & Documentation
- Added sections: Technology Stack, Development Workflow
- Removed sections: None
- Templates requiring updates:
  - .specify/templates/plan-template.md (✅ updated)
  - .specify/templates/spec-template.md (✅ updated)
  - .specify/templates/tasks-template.md (✅ updated)
- Follow-up TODOs: None
-->

# Fibonazi Constitution

## Core Principles

### I. Object-Oriented Programming (OOP)
모든 코드는 객체지향 원칙을 준수하여 작성해야 합니다. SOLID 원칙을 철저히 따르며, 재사용성과 유지보수성이 높은 구조를 지향합니다. 데이터와 행동을 적절히 캡슐화하고, 상속보다는 합성을 우선적으로 고려합니다.

### II. Python as Primary Language
프로젝트의 모든 핵심 로직과 스크립트는 Python 언어를 사용하여 개발합니다. Pythonic한 코드를 작성하며, 코드의 명확성과 타입 안전성을 위해 타입 힌팅(Type Hinting)을 적극적으로 활용합니다.

### III. Test-Driven Development (TDD)
모든 기능 구현은 TDD(Test-Driven Development) 방식을 따릅니다. 실제 기능을 구현하기 전에 반드시 단위 테스트(Unit Test)를 먼저 작성해야 합니다. Red-Green-Refactor 사이클을 엄격히 준수합니다.

### IV. Automated Test Execution & Feedback Loop
코드 생성이 완료된 후에는 반드시 단위 테스트를 자동으로 실행해야 합니다. 테스트 결과에서 실패가 발생할 경우, 즉시 원인을 분석하고 코드를 수정하여 모든 테스트가 통과될 때까지 반복합니다. 테스트 결과는 개발 단계의 최종 관문입니다.

### V. Clean Code & Documentation
가독성이 높고 깔끔한 코드를 유지합니다. 변수 및 함수 이름은 의도를 명확히 드러내야 하며, 주요 클래스와 함수에는 Docstring을 포함하여 문서화합니다. 복잡한 로직에는 '왜' 그렇게 작성했는지에 대한 주석을 남깁니다.

### VI. Document Language
모든 문서는 한글로 작성하는 것을 원칙으로 합니다. 이는 요구사항 정의서(spec.md), 개발 계획서(plan.md), 작업 목록(tasks.md) 등을 포함한 프로젝트 내의 모든 산출물에 적용됩니다. 단, 소스 코드 내의 식별자나 기술적 용어는 예외로 할 수 있습니다.

## Technology Stack

- **Language**: Python 3.x
- **Testing Framework**: `pytest` (기본 권장) 또는 `unittest`
- **Linting/Formatting**: `flake8`, `black`, `isort` 권장

## Development Workflow

1. **요구사항 분석**: `spec.md`를 통해 기능 및 인수 조건 정의
2. **테스트 설계**: 요구사항을 충족하는 단위 테스트 코드 작성 (Red)
3. **기능 구현**: 테스트를 통과하기 위한 최소한의 코드 작성 (Green)
4. **테스트 실행**: 자동화된 도구로 테스트 수행 및 검증
5. **수정 및 리팩토링**: 테스트 결과에 따른 버그 수정 및 코드 구조 개선 (Refactor)

## Governance

이 헌장은 Fibonazi 프로젝트의 모든 개발 활동의 최상위 기준이 됩니다. 모든 코드 변경 및 PR(Pull Request)은 본 헌장에 명시된 원칙을 준수해야 합니다. 헌장의 변경은 프로젝트 유지관리자의 승인이 필요하며, 의미 있는 변경 시 버전 번호를 업데이트합니다.

**Version**: 1.0.0 | **Ratified**: 2026-02-09 | **Last Amended**: 2026-02-09