from typing import List
from pydantic import BaseModel

class PrinterIP(BaseModel):
    ip: str

class PostPrinter(BaseModel):
    printers: List[PrinterIP]