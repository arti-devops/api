from src.config.db import pymongo, projectsdb
from src.modules.dsesp.schemas.project import projectsEntity

def process_query_data(filter):

    q = filter.q
    status = filter.status
    dirname = filter.dirname
    options = filter.options

    sorting = {
        "asc": pymongo.ASCENDING,
        "desc": pymongo.DESCENDING
    }

    # Extract options
    sort_by_value = options.sortBy[0].key
    sort_by_order = sorting[options.sortBy[0].order]  
    items_per_page = options.itemsPerPage
    page = options.page

    query = {}

    # Search and filter devices
    if q:
        query["device_user"] = {"$regex": q, "$options": "i"}
    if dirname:
        query["project_direction"] = {"$regex": dirname, "$options": "i"}
    if status:
        query["project_status"] = {"$regex": status, "$options": "i"}

    # Count the total number of devices
    total_projects = projectsdb.count_documents(query)

    # Calculate pagination
    total_pages = (total_projects + items_per_page - 1) // items_per_page
    page = min(page, total_pages)
    if page == 0: page = 1

    # Apply pagination and retrieve the devices
    paginated_projects = projectsdb.find(query).sort(key_or_list=sort_by_value, direction=sort_by_order).skip((page - 1) * items_per_page).limit(items_per_page)

    # Process the devices
    projects = projectsEntity(paginated_projects)
    
    # Construct the response
    response = {
        "projects": projects,
        "totalPages": total_pages,
        "totalDevices": total_projects,
        "page": page
    }
    return response