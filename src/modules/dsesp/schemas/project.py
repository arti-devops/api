def get_project_tasks(item,column_name):
    try:
        item = item[column_name]
        return list([
            dict({
                "project_task_id": str(t["project_task_id"]),
                "project_task_title": str(t["project_task_title"]),
                "project_task_budget": int(t["project_task_budget"]),
                "project_task_status": str(t["project_task_status"]),
                "project_task_manager": str(t["project_task_manager"]),
                "project_task_end_date": str(t["project_task_end_date"]),
                "project_task_start_date": str(t["project_task_start_date"]),
                "project_task_description": str(t["project_task_description"]),
            })
        ] for t in item)
    except:
        return None

def projectEntity(item) -> dict:
    return{
        "project_id": str(item["_id"]),
        "project_title": str(item["project_title"]),
        "project_budget": int(item["project_budget"]),
        "project_status": str(item["project_status"]),
        "project_stratob": str(item["project_stratob"]),
        "project_end_date": str(item["project_end_date"]),
        "project_direction": str(item["project_direction"]),
        "project_start_date": str(item["project_start_date"]),
        "project_description": str(item["project_description"]),
        "project_members": list([
            dict({
                "project_member_id": str(m["project_member_id"]),
                "project_member_role": str(m["project_member_role"]),
                "project_member_name": str(m["project_member_name"]),
        })
        ] for m in item["project_members"]),
        "project_tasks": get_project_tasks(item,"project_tasks")
    }

def projectsEntity(entity) -> list:
    return [projectEntity(item) for item in entity]