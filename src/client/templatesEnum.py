from enum import Enum

class TemplateEnum(Enum):
    """
    Enumerate the differents path to acess to the view
    """

    INDEX_WIEW = "index.html"
    PROJECTS_VIEW = "projects/projects.html"
    PROJECT_VIEW = "projects/projetDetail.html"