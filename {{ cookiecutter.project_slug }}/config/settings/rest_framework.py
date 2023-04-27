COMMON = {
    "COERCE_DECIMAL_TO_STRING": False,
    "DEFAULT_PAGINATION_CLASS": "{{ cookiecutter.project_slug }}.pagination.DefaultLimitOffsetPagination",
}

DEV = {
    **COMMON,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

PROD = {
    **COMMON,
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}
