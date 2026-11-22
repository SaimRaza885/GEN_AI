# Codi — AI-Powered Coding Agent

## 1. Project Overview

Codi is an AI-powered coding agent designed to work as a personal vibe-coding assistant, similar to Cursor.

Its goal is to help users build, modify, debug, and manage software projects using natural-language instructions.

Codi should not just generate code. It should understand requirements, plan implementations, interact with the local development environment, execute commands, and verify its work.

## 2. Core Workflow

Codi should follow a structured workflow:

1. **Understand:** Analyze the user's request and identify the task type.
2. **Clarify:** Identify missing requirements and ask relevant questions.
3. **Analyze:** Inspect the existing project, files, technologies, and dependencies.
4. **Plan:** Create a short implementation summary and ask the user for approval.
5. **Detailed Planning:** After approval, create a `plan.md` file containing implementation steps and project requirements.
6. **Execute:** Follow `plan.md` to build or modify the application.
7. **Verify:** Run the application, test functionality, and fix errors.
8. **Deliver:** Summarize completed work and explain how to run the application.

## 3. Example: Creating a Todo App

User: Create a Todo App.

Codi identifies missing requirements and asks questions:

- What features do you need?
- Which technologies should be used?
- Where should tasks be stored?

User: HTML, CSS, JavaScript, CRUD functionality, and localStorage.

Codi then:

1. Creates a short project summary.
2. Asks the user to approve it.
3. Creates a detailed `plan.md`.
4. Builds the application using the plan.
5. Tests the functionality.
6. Explains what was built and how to run it.

## 4. Debugging and Existing Projects

Codi should not immediately modify code when a user reports a problem.

It should:

1. Understand the issue.
2. Ask clarifying questions if necessary.
3. Inspect relevant files.
4. Identify the root cause.
5. Apply the appropriate fix.
6. Verify the fix.
7. Explain what was wrong and how it was resolved.

Codi should also support modifying existing projects, adding features, refactoring code, and improving UI.

## 5. Tools and Capabilities

Codi should be able to interact with the local development environment.

**File Operations:**
- List, read, create, edit, and delete files.
- Search files and inspect project structure.

**Terminal Operations:**
- Execute commands such as `npm install`, `npm run dev`, and `npm run build`.
- Install dependencies.
- Run applications and tests.
- Read terminal output and diagnose errors.

All operations should follow appropriate workspace restrictions and user permission controls.

## 6. Proposed Technology Stack

| Component | Technology |
|---|---|
| Language | Pyhton |
| AI Model | OpenAI API |
| AI Communication | Tool Calling |
| Frontend (later) | streamlit |

## 7. Future Features

These capabilities are planned for later versions:

- **Documentation Search:** Search and read official documentation for libraries, frameworks, and APIs.
- **Real-Time Documentation:** Retrieve up-to-date, version-specific documentation and identify deprecated methods.
- **Browser Access:** Search the web, visit websites, research solutions, and inspect online resources.
- **Browser Testing:** Open local applications, interact with UI elements, and identify visual or functional issues.
- **Git Integration:** Review changes, create branches, commit code, and revert modifications.
- **Project Memory:** Maintain project architecture, decisions, coding conventions, and previous work across sessions.
- **Advanced Coding:** Multi-file refactoring, code reviews, test generation, optimization, and security analysis.

## 8. Development Roadmap

1. **Phase 1 — Core Agent:** OpenAI connection, conversation history, request analysis, clarification, planning, and approval.
2. **Phase 2 — File Operations:** Read, write, edit, delete, and search project files.
3. **Phase 3 — Coding Agent:** Tool calling, terminal execution, dependency installation, and application building.
4. **Phase 4 — Debugging:** Error diagnosis, code modification, testing, and verification.
5. **Phase 5 — User Interface:** React-based interface, file explorer, integrated terminal, and code review.
6. **Phase 6 — Advanced Features:** Documentation search, browser access, Git integration, and persistent project memory.


---

**Final Goal:** Build Codi into a reliable AI coding agent that can understand an idea, plan it, build it, test it, debug it, and help manage the entire development process.