from django.db import models

class Project(models.Model):
    """
    Project model
    """

    project_name = models.CharField(max_length=30)
    project_description = models.CharField(max_length=300)
    usedLangages = models.CharField(max_length=100)
    usedTools = models.CharField(max_length=100, blank = True)
    usedSkills = models.CharField(max_length=100, blank = True)
    github = models.CharField(max_length=100, blank = True)

    def get_used_skills_list(self):
        """
        Get all the skills
        """

        tab = []
        if self.usedSkills:
            tab = self.usedSkills.split(";")
        return tab

    def get_used_langages_list(self):
        """
        Get all the langages 
        """

        tab = []
        if self.usedLangages:
            tab = self.usedLangages.split(";")
        return tab

    def get_used_tools_list(self):
        """
        get all the tools 
        """

        tab = []
        if self.usedTools:
            tab = self.usedTools.split(";")
        return tab