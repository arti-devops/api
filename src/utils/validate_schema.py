def validate_schema_str_attr(schema, attr):
    try:
        return schema[attr]
    except KeyError:
        return ""
    
def validate_schema_int_attr(schema, attr):
    try:
        return schema[attr]
    except KeyError:
        return None