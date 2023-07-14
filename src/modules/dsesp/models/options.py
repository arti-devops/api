from typing import List
from pydantic import BaseModel, Field, validator

class SortOption(BaseModel):
    key: str
    order: str

class ListOptions(BaseModel):
    sortBy: List[SortOption] = Field([SortOption(key="project_start_date", order="asc")], description="Sort by field")
    itemsPerPage: int = Field(10, description="Items per page")
    page: int = Field(1, description="Page number")

    @property
    def offset(self):
        return (self.page - 1) * self.itemsPerPage
    
    @validator('sortBy', pre=True)
    def handle_empty_sortBy(cls, v):
        if isinstance(v, list) and len(v) == 0:
            return [SortOption(key="project_start_date", order="asc")]
        return v