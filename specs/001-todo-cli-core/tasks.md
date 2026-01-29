---

description: "Task list for Todo CLI Core feature implementation"
---

# Tasks: Todo CLI Core

**Input**: Design documents from `/specs/001-todo-cli-core/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Constitution-Aligned Infrastructure)

**Purpose**: Project initialization with constitution principles applied

- [x] T001 Create project structure per implementation plan ensuring Specification-First Design
- [x] T002 Initialize Python 3.11 project with argparse and json dependencies
- [x] T003 [P] Configure linting and formatting tools with spec-driven approach
- [x] T004 Create initial directory structure (src/cli/, src/models/, src/services/, src/lib/, tests/)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [x] T005 Setup specification framework with Spec-Driven Development focus
- [x] T006 [P] Implement validation/verification framework for agent instructions
- [x] T007 Setup agent communication protocols with Clear Hierarchy and Responsibility
- [x] T008 Create base todo item model in src/models/todo_item.py with Specification-First Design
- [x] T009 Configure error handling and logging infrastructure
- [x] T010 Setup environment configuration management
- [x] T011 Create data persistence layer in src/lib/storage.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and List Todos (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new todos and list all existing todos

**Independent Test**: Users can add a new todo via CLI command and list all todos to verify they appear in the list

**Acceptance Scenarios**:
1. Given no todos exist, When user runs "todo add 'Buy groceries'", Then the todo should be added successfully
2. Given multiple todos exist, When user runs "todo list", Then all todos should be displayed with their status

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T012 [P] [US1] Contract test for add/list endpoints in tests/contract/test_add_list_contract.py
- [ ] T013 [P] [US1] Integration test for add/list user journey in tests/integration/test_add_list_integration.py

### Implementation for User Story 1

- [x] T014 [P] [US1] Create TodoItem model in src/models/todo_item.py with Specification-First Design
- [x] T015 [US1] Implement TodoService in src/services/todo_service.py (depends on T014)
- [x] T016 [US1] Implement validation service in src/services/validation_service.py with Safe and Predictable Behavior
- [x] T017 [US1] Implement add todo functionality in src/cli/todo_app.py with Instruction-Based Agent Architecture
- [x] T018 [US1] Implement list todos functionality in src/cli/todo_app.py with Instruction-Based Agent Architecture
- [x] T019 [US1] Add validation and error handling following Spec-Driven Development principle
- [x] T020 [US1] Add logging for user story 1 operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Complete/Incomplete Todos (Priority: P2)

**Goal**: Allow users to mark todos as complete or incomplete

**Independent Test**: Users can add a todo, mark it as complete, then mark it as incomplete to verify state transitions work correctly

**Acceptance Scenarios**:
1. Given a todo exists, When user runs "todo complete 1", Then the todo should be marked as completed
2. Given a completed todo exists, When user runs "todo incomplete 1", Then the todo should be marked as not completed

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T021 [P] [US2] Contract test for complete/incomplete endpoints in tests/contract/test_complete_contract.py
- [ ] T022 [P] [US2] Integration test for complete/incomplete user journey in tests/integration/test_complete_integration.py

### Implementation for User Story 2

- [x] T023 [P] [US2] Update TodoItem model in src/models/todo_item.py to support state transitions
- [x] T024 [US2] Implement complete/incomplete functionality in src/services/todo_service.py with Clear Hierarchy and Responsibility
- [x] T025 [US2] Implement complete todo CLI command in src/cli/todo_app.py with Instruction-Based Agent Architecture
- [x] T026 [US2] Implement incomplete todo CLI command in src/cli/todo_app.py with Instruction-Based Agent Architecture
- [x] T027 [US2] Integrate with User Story 1 components (if needed) maintaining Safe and Predictable Behavior

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update and Delete Todos (Priority: P3)

**Goal**: Allow users to update todo titles and delete todos

**Independent Test**: Users can add a todo, update its title, then delete it to verify full CRUD operations work

**Acceptance Scenarios**:
1. Given a todo exists, When user runs "todo update 1 'Updated title'", Then the todo title should be updated
2. Given a todo exists, When user runs "todo delete 1", Then the todo should be removed from the list

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚟️

- [ ] T028 [P] [US3] Contract test for update/delete endpoints in tests/contract/test_update_delete_contract.py
- [ ] T029 [P] [US3] Integration test for update/delete user journey in tests/integration/test_update_delete_integration.py

### Implementation for User Story 3

- [x] T030 [P] [US3] Update TodoItem model in src/models/todo_item.py with Specification-First Design
- [x] T031 [US3] Implement update/delete functionality in src/services/todo_service.py with Spec-Driven Development
- [x] T032 [US3] Implement update todo CLI command in src/cli/todo_app.py with Instruction-Based Agent Architecture
- [x] T033 [US3] Implement delete todo CLI command in src/cli/todo_app.py with Instruction-Based Agent Architecture

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Constitution Compliance & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and ensure constitution compliance

- [x] TXXX [P] Documentation updates in docs/ ensuring Specification-First Design
- [x] TXXX Code cleanup and refactoring following Human-Readable Instructions
- [x] TXXX Performance optimization across all stories
- [ ] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [x] TXXX Security hardening with Safe and Predictable Behavior focus
- [x] TXXX Run quickstart.md validation ensuring Instruction-Based Agent Architecture

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for add/list endpoints in tests/contract/test_add_list_contract.py"
Task: "Integration test for add/list user journey in tests/integration/test_add_list_integration.py"

# Launch all models for User Story 1 together:
Task: "Create TodoItem model in src/models/todo_item.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Constitution Compliance Checklist

- [x] Specification-First Design: All features fully specified before implementation
- [x] Instruction-Based Agent Architecture: Agents defined by markdown instruction files
- [x] Spec-Driven Development: Implementation follows specification exactly
- [x] Clear Hierarchy and Responsibility: Proper agent responsibilities defined
- [x] Safe and Predictable Behavior: Operations are safe and predictable
- [x] Human-Readable Instructions: Components defined with clear documentation

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence