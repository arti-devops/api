from typing import List
from pydantic import BaseModel, Field, validator
from src.modules.dsesp.models.options import ListOptions

# SECTION - Project Models

# ANCHOR - Project Member
class ProjectMemberModel(BaseModel):
    project_member_id: str = Field(default="", description="Project member id/matricule")
    project_member_role: str = Field(default="", description="Project role")
    project_member_name: str = Field(default="", description="Project name")

# ANCHOR - Project Task
class ProjectTaskModel(BaseModel):
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
    project_members: List[ProjectMemberModel]
    project_tasks: List[ProjectTaskModel]

# ANCHOR - Project Member
class ProjectModel(BaseModel):
    project_title: str = Field(default="", description="Project title")
    project_budget: int = Field(default="", description="Project budget")
    project_status: str = Field(default="", description="Project status")
    project_stratob: str = Field(default="", description="Project strategic objective")
    project_end_date: str = Field(default="", description="Project end date")
    project_direction: str = Field(default="", description="Project direction/departement in charge")
    project_start_date: str = Field(default="", description="Project start date")
    project_description: str = Field(default="", description="Project description")
    project_members: List[ProjectMemberModel]

# !SECTION

# SECTION - Project Filter Models
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

# !SECTION

# SECTION - Project Update Models
class ProjectColumnsUpdate(BaseModel):
    project_status: str = Field(..., description="Project Status")
    project_end_date: str = Field(..., description="Project End Date")

class UpdateProject(BaseModel):
    update: ProjectColumnsUpdate

# SECTION - Create Project Model

class PostProject(BaseModel):
    project: ProjectModel

class PostProjectTask(BaseModel):
    project_id: str
    task: ProjectTaskModel

class DeleteProjectTask(BaseModel):
    project_id: str
    project_task_id: str

# !SECTION - Create Project
