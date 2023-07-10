from config.db import pymongo, devicesdb
from dsi.schemas.device import devicesEntity

def process_query_data(filter):

    q = filter.q
    brand = filter.brand
    status = filter.status
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
    if brand:
        query["device_brand_name"] = {"$regex": brand, "$options": "i"}
    if status:
        query["device_status"] = {"$regex": status, "$options": "i"}

    # Count the total number of devices
    total_devices = devicesdb.count_documents(query)

    # Calculate pagination
    total_pages = (total_devices + items_per_page - 1) // items_per_page
    page = min(page, total_pages)
    if page == 0: page = 1

    # Apply pagination and retrieve the devices
    paginated_devices = devicesdb.find(query).sort(key_or_list=sort_by_value, direction=sort_by_order).skip((page - 1) * items_per_page).limit(items_per_page)

    # Process the devices
    devices = devicesEntity(paginated_devices)
    # Construct the response
    response = {
        "devices": devices,
        "totalPages": total_pages,
        "totalDevices": total_devices,
        "page": page
    }

    return response