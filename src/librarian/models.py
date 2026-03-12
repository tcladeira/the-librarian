from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class BookStatus(Enum):
    AVAILABLE = "AVAILABLE"
    CHECKED_OUT = "CHECKED_OUT"
    LOST = "LOST"
    IN_REPAIR = "IN_REPAIR"

@dataclass
class Book:
    isbn: str
    author: str
    title: str
    id: int
    publication_year: int
    book_status: BookStatus


@dataclass
class Member:
    member_id: int 
    member_name: str
    email: str
    fees: float
    address: str

@dataclass
class Loan:
    book_id: int
    member_id: int
    loan_number: int 
    borrow_date: datetime
    due_date: datetime
    returned_date: datetime | None = None
