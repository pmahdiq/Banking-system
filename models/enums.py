from enum import Enum

class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"

class LoanTitle(str, Enum):
    PERSONAL = "personal"
    EDUCATION = "education"