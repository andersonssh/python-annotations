from jsonschema import validate, draft7_format_checker

schema = {
    "format": "uri",
    "pattern": "^https?://"
}

instance = 'http://aaaaaa!+'

validate(instance=instance, schema=schema, format_checker=draft7_format_checker)