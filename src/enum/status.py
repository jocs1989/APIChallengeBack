from enum import Enum
class Status(Enum):
    INITIAL = "initial"
    PROCESS = "process"
    COMPLETE = "complete"
    FAILED = "failed"  # Corrección en "FAILD" a "FAILED"