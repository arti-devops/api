from fastapi import status
from fastapi.responses import JSONResponse

def response_builder_log(query_data, date_range) -> JSONResponse:
    if isinstance(query_data, list) and len(query_data) > 0:
        return JSONResponse(status_code=status.HTTP_200_OK, content=query_data)
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=f"Lookup failed: Log a date '{date_range}' not found")
