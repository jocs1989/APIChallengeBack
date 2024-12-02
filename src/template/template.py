
from src.enum.status_enum import Status


from datetime import datetime
from uuid import uuid4


class Template:
    def __init__(self, bach_id=str(uuid4())) -> None:

        self.batch_id = bach_id
        self.item=None
        self.item={}

    def get_batchId(self) -> str:
        # batchId
        self.item["batchId"] = self.batch_id

    def get_createdAt(self) -> str:
        self.item["createdAt"] = datetime.now()

    def get_updatedAt(self, date=datetime.now()) -> str:
        self.item["updatedAt"] = date

    def get_status(self, status: str = Status.INITIAL.value) -> str:
        self.item["status"] = status


      

    def run(self):
        self.get_batchId()
        self.get_createdAt()
        self.get_updatedAt()
        self.get_status()
        self.item["producto"]=None
        self.item["precio"] = None
        self.item["img"] = None
        return self.item
