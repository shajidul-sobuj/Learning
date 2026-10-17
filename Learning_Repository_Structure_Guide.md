# Learning Repository --- Structure & Implementation Guide

A practical GitHub repository for organizing learning notes, code
examples, exercises, computer science fundamentals, and project-based
practice across Python, Java, and backend frameworks.

> **Recommended approach:** Start with the top-level structure and add
> folders as you need them. Empty folders are not tracked by Git, so
> create a folder when it contains a file or add a small `README.md`
> where a folder needs documentation.

------------------------------------------------------------------------

## 1. Repository Structure

``` text
Learning/
├── README.md
├── ROADMAP.md
├── .gitignore
│
├── Python/
│   ├── README.md
│   ├── 01-Python-Basics/
│   │   ├── README.md
│   │   ├── notes/
│   │   ├── examples/
│   │   └── exercises/
│   ├── 02-OOP/
│   │   ├── notes/
│   │   ├── examples/
│   │   └── exercises/
│   ├── 03-Modules-and-Packages/
│   │   ├── notes/
│   │   ├── examples/
│   │   └── exercises/
│   ├── 04-File-Handling/
│   │   ├── notes/
│   │   ├── examples/
│   │   └── exercises/
│   ├── 05-Exception-Handling/
│   │   ├── notes/
│   │   ├── examples/
│   │   └── exercises/
│   ├── 06-Advanced-Python/
│   │   ├── notes/
│   │   ├── examples/
│   │   └── practice/
│   ├── 07-Pandas/
│   │   ├── README.md
│   │   ├── notes/
│   │   ├── examples/
│   │   ├── practice/
│   │   └── notebooks/
│   └── 08-FastAPI/
│       ├── README.md
│       ├── notes/
│       │   ├── routing.md
│       │   ├── request-response.md
│       │   ├── pydantic.md
│       │   ├── dependency-injection.md
│       │   ├── authentication.md
│       │   └── error-handling.md
│       ├── examples/
│       │   ├── hello_api/
│       │   │   ├── README.md
│       │   │   └── main.py
│       │   └── crud_api/
│       │       ├── README.md
│       │       └── main.py
│       └── mini-projects/
│           └── todo-api/
│               ├── README.md
│               ├── app/
│               │   ├── main.py
│               │   ├── routes/
│               │   ├── schemas/
│               │   ├── models/
│               │   └── services/
│               ├── tests/
│               ├── requirements.txt
│               └── .env.example
│
├── Java/
│   ├── README.md
│   ├── 01-Java-Basics/
│   │   ├── README.md
│   │   ├── notes/
│   │   ├── examples/
│   │   └── exercises/
│   ├── 02-OOP/
│   │   ├── notes/
│   │   ├── examples/
│   │   └── exercises/
│   ├── 03-Arrays-and-Strings/
│   │   ├── notes/
│   │   ├── examples/
│   │   └── exercises/
│   ├── 04-Collections-Framework/
│   │   ├── notes/
│   │   ├── examples/
│   │   └── practice/
│   ├── 05-Exception-Handling/
│   │   ├── notes/
│   │   ├── examples/
│   │   └── exercises/
│   ├── 06-File-Handling/
│   │   ├── notes/
│   │   └── practice/
│   ├── 07-GUI/
│   │   ├── README.md
│   │   ├── notes/
│   │   ├── examples/
│   │   └── practice/
│   └── 08-Spring-Boot/
│       ├── README.md
│       ├── notes/
│       │   ├── dependency-injection.md
│       │   ├── controllers.md
│       │   ├── services.md
│       │   ├── repositories.md
│       │   ├── spring-data-jpa.md
│       │   └── exception-handling.md
│       ├── examples/
│       │   ├── hello-spring/
│       │   └── rest-api/
│       └── practice/
│           ├── student-api/
│           └── employee-api/
│
├── Computer-Science/
│   ├── README.md
│   ├── 01-DSA/
│   │   ├── notes/
│   │   ├── algorithms/
│   │   └── practice/
│   ├── 02-DBMS/
│   │   ├── notes/
│   │   └── diagrams/
│   ├── 03-SQL/
│   │   ├── notes/
│   │   ├── queries/
│   │   └── practice/
│   ├── 04-Operating-Systems/
│   │   └── notes/
│   ├── 05-Computer-Networks/
│   │   └── notes/
│   └── 06-Software-Engineering/
│       └── notes/
│
├── Git-GitHub/
│   ├── README.md
│   ├── git-commands.md
│   └── github-workflow.md
│
└── Projects/
    ├── README.md
    ├── project-ideas.md
    └── mini-projects/
```

------------------------------------------------------------------------

## 2. Folder Naming Conventions

  Folder             Purpose
  ------------------ -------------------------------------------------
  `notes/`           Concepts, theory, definitions, and explanations
  `examples/`        Small, focused code examples
  `exercises/`       Exercises and their solutions
  `practice/`        Topic-based experiments and applied practice
  `notebooks/`       Jupyter notebooks, especially for data analysis
  `algorithms/`      Algorithm implementations
  `queries/`         SQL query examples
  `diagrams/`        Architecture, workflow, and concept diagrams
  `mini-projects/`   Small applications built to practise a skill
  `tests/`           Automated tests
  `app/`             Application source code

**Do not create every folder for every topic by default.** Add only the
folders that are useful for that topic. Git does not track empty
directories, so place files inside them before committing.

------------------------------------------------------------------------

## 3. Python and FastAPI Project Structure

Keep short demonstrations in `examples/`. Put applications with multiple
features in `mini-projects/`.

``` text
08-FastAPI/
├── README.md
├── notes/
├── examples/
│   ├── hello_api/
│   │   ├── README.md
│   │   └── main.py
│   └── crud_api/
│       ├── README.md
│       └── main.py
└── mini-projects/
    └── todo-api/
        ├── README.md
        ├── app/
        │   ├── main.py
        │   ├── routes/
        │   ├── schemas/
        │   ├── models/
        │   └── services/
        ├── tests/
        ├── requirements.txt
        └── .env.example
```

### What each part does

-   `routes/` --- API endpoints and route definitions.
-   `schemas/` --- Pydantic models for request and response validation.
-   `models/` --- database models, if the project uses a database.
-   `services/` --- business logic separated from route handlers.
-   `tests/` --- automated tests.
-   `requirements.txt` --- Python dependencies for the project.
-   `.env.example` --- example environment-variable names without real
    secrets.

Add database, authentication, and other layers when the project actually
needs them. For a small first API, a single `main.py` can be enough.

------------------------------------------------------------------------

## 4. Java and Spring Boot Project Structure

Keep framework notes separate from runnable Spring Boot applications.
Each application should have its own build configuration and source
tree.

``` text
08-Spring-Boot/
├── README.md
├── notes/
│   ├── dependency-injection.md
│   ├── controllers.md
│   ├── services.md
│   ├── repositories.md
│   ├── spring-data-jpa.md
│   └── exception-handling.md
├── examples/
│   ├── hello-spring/
│   └── rest-api/
└── practice/
    ├── student-api/
    └── employee-api/
```

Example structure for `student-api/`:

``` text
student-api/
├── README.md
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/
│   │   └── resources/
│   └── test/
└── .gitignore
```

-   Use `pom.xml` for Maven projects.
-   Use `build.gradle` or `build.gradle.kts` for Gradle projects.
-   Keep each application independently runnable and document its setup
    in its own `README.md`.

------------------------------------------------------------------------

## 5. README Template

Use this template for a language, framework, or major topic directory.
Smaller topic folders can use a shorter README.

``` markdown
# Topic Name

## Overview
What I am learning and why.

## Learning Objectives
- Concept 1
- Concept 2
- Concept 3

## Notes
- [Concept notes](notes/example.md)

## Examples
- [Example name](examples/example.py)

## Practice
Exercises completed and key lessons learned.

## Projects
Projects built while learning.

## Progress
- [ ] Fundamentals
- [ ] Intermediate concepts
- [ ] Advanced concepts
- [ ] Build a project

## References
- Official documentation
- Useful learning resources
```

Update links and file extensions to match the actual contents of each
directory.

------------------------------------------------------------------------

## 6. Git Workflow

After a focused learning session, review and commit the relevant
changes:

``` bash
git status
git add .
git commit -m "Add FastAPI routing examples"
git push
```

  -----------------------------------------------------------------------
  Command                             Purpose
  ----------------------------------- -----------------------------------
  `git status`                        Review changed and untracked files

  `git add .`                         Stage changes in the current
                                      directory and its descendants

  `git commit -m "message"`           Save a local checkpoint

  `git push`                          Upload committed changes to the
                                      remote repository
  -----------------------------------------------------------------------

Use meaningful commit messages, for example:

-   `Add Python exception handling notes`
-   `Solve array and string exercises`
-   `Build initial student REST API`
-   `Update Java OOP learning progress`

### Security checklist

-   Never commit `.env` files containing real credentials.
-   Never commit API keys, passwords, access tokens, or private keys.
-   Keep `.env.example` free of secret values.
-   Configure `.gitignore` for Python caches, virtual environments, IDE
    files, build output, and generated files.
-   If a secret is committed accidentally, revoke or rotate it. Removing
    it in a later commit does not erase it from Git history.

------------------------------------------------------------------------

## 7. Recommended Learning Workflow

``` text
Learn
  ↓
Write Notes
  ↓
Create Small Examples
  ↓
Solve Exercises
  ↓
Build a Mini-project
  ↓
Review and Refactor
  ↓
Commit and Push
```

The goal is not to create the largest repository. The goal is to build a
searchable knowledge base that records what you learned and demonstrates
that you can apply it.

------------------------------------------------------------------------

## 8. Suggested Top-Level README

Your root `README.md` can briefly explain the repository:

``` markdown
# Learning

My personal learning repository for programming, computer science,
backend development, and project-based practice.

## Learning Tracks
- [Python](Python/README.md)
- [Java](Java/README.md)
- [Computer Science](Computer-Science/README.md)
- [Git and GitHub](Git-GitHub/README.md)
- [Projects](Projects/README.md)

## Learning Principles
1. Learn concepts before relying on copied solutions.
2. Keep examples small and runnable.
3. Record mistakes and lessons learned.
4. Build projects to apply concepts.
5. Review and improve earlier work.

## Roadmap
See [ROADMAP.md](ROADMAP.md) for the planned learning sequence.
```

Create the linked README files as you populate each track.

------------------------------------------------------------------------

## 9. Final Recommendations

1.  **Start small.** Create the root README, roadmap, and the track you
    are studying now.
2.  **Keep notes and applications distinct.** Notes explain concepts;
    projects demonstrate implementation.
3.  **Make projects reproducible.** Include setup instructions,
    dependencies, and tests where appropriate.
4.  **Avoid unnecessary duplication.** If an application grows large
    enough to need independent releases, deployment, or portfolio
    presentation, consider moving it into its own GitHub repository.
5.  **Use consistent names.** Keep topic numbering and folder naming
    consistent across each learning track.
6.  **Review periodically.** Archive or reorganize material when the
    structure stops helping you find things.

**Core principle:**
`Learn → Notes → Examples → Practice → Project → Review → Commit & Push`.
