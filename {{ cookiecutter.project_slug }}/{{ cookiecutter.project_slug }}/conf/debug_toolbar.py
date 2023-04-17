# To fix django-debug-toolbar disappearing when running application with Docker.
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}
