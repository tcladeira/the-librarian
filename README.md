The Library - Project Structure

librarian/
│
├── src/
│   └── librarian/
│       ├── __init__.py
│       ├── models.py
│       ├── repository.py
│       ├── exceptions.py
│       │
│       └── adapters/
│           ├── __init__.py
│           └── memory.py
│
├── tests/
│   └── test_repository.py
│
├── docs/
│
├── examples/
│
├── pyproject.toml
├── README.md

Designing Models:

BOOK:
isbn -> string (unique)
author -> string
title -> string
id -> int (unique)
publication -> string

BOOKSTATUS (ENUM):
available - 1
checkOut - 2
lost - 3
inRepear - 4

MEMBERS:
memberId -> int (unique)
memberStatus -> diccionary
rentedBooks -> list(BOOKS)
email -> string (unique)
fees -> float

LOAN:
loanNumber -> int (unique)
borrowDate -> datetime
returnDate -> datetime
