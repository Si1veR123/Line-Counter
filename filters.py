django_filter = {
    "extensions": [
        ".py",
        ".js",
        ".css",
        ".html",
    ],
    "exceptions": [
        "admin/",
        "staticfiles/",
        "manage",
        "wsgi",
        "asgi",
        "migrations/",
        "settings"
    ]
}

vue_filter = {
    "extensions": [
        ".js",
        ".vue"
    ],
    "exceptions": [
        "node_modules/",
        "dist/",
    ]
}

filter_templates = {
    "django": django_filter,
    "vue": vue_filter,
}

class Filter:
    def __init__(self):
        self.extensions = []
        self.exceptions = [
            ".idea/",
            ".git/",
            ".gitignore",
            ".komodoproject",
            ".komodotools/",
            "Pipfile",
            "Procfile",
            "__pycache__/",
            "__init__",
        ]

    def apply_filter_template(self, template):
        if template in filter_templates.keys():
            self.extensions += filter_templates[template]["extensions"]
            self.exceptions += filter_templates[template]["exceptions"]
        else:
            raise ValueError("Specified template not available")
