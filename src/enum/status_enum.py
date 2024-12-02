from enum import Enum

class Status(Enum):
    INITIAL = "initial"    # Represents the initial state
    PROCESSING = "processing"  # Represents the state during processing
    COMPLETE = "complete"   # Represents a successfully completed state
    FAILED = "failed"       # Represents a failed state
