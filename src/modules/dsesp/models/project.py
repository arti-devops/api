from typing import List
from pydantic import BaseModel, Field, validator
from src.modules.dsesp.models.options import ListOptions

class ProjectMember(BaseModel):
    project_member_id: str
    project_member_role: str
    project_member_name: str

class ProjectTask(BaseModel):
    project_task_id: str
    project_task_title: str
    project_task_budget: int
    project_task_status: str
    project_task_manager: str
    project_task_end_date: str
    project_task_start_date: str
    project_task_description: str

class ProjectResponse(BaseModel):
    project_id: str
    project_title: str
    project_budget: int
    project_status: str
    project_stratob: str
    project_end_date: str
    project_direction: str
    project_start_date: str
    project_description: str
    project_members: List[ProjectMember]
    project_tasks: List[ProjectTask]

class ProjectFilter(BaseModel):
    q: str = Field(default="", description="Search by Project Name")
    dirname: str = Field(default="", description="Project Direction Name filter")
    status: str = Field(default="", description="Project Status filter")
    options: ListOptions = ListOptions()

    @validator('dirname', 'status', pre=True)
    def set_default_if_null(cls, v):
        if v is None:
            return ""
        return v

class FilterProject(BaseModel):
    filter : ProjectFilter = ProjectFilter()

class ProjectColumnsUpdate(BaseModel):
    project_status: str = Field(..., description="Project Status")
    project_end_date: str = Field(..., description="Project End Date")

class UpdateProject(BaseModel):
    update: ProjectColumnsUpdate