from django.db import models

class Project(models.Model):
    project_url = models.CharField(max_length=30, blank = True)  
    project_name = models.CharField(max_length=30)
    project_description = models.CharField(max_length=300)
    project_technologies = models.CharField(max_length=100)
    project_tools = models.CharField(max_length=100, blank = True)
    project_skills = models.CharField(max_length=100, blank = True)
    project_github = models.CharField(max_length=100, blank = True)
    project_image_path = models.CharField(max_length=100, blank = True)
    project_category = models.ForeignKey("client.Category", verbose_name="Category", on_delete=models.CASCADE, blank=True, null=True)

    def get_used_skills_list(self):
        """
        Get all the skills
        """

        tab = []
        if self.project_skills:
            tab = self.project_skills.split(";")
        return tab

    def get_used_technologies_list(self):
        """
        Get all the langages 
        """

        tab = []
        if self.project_technologies:
            tab = self.project_technologies.split(";")
        return tab

    def get_used_tools_list(self):
        """
        get all the tools 
        """

        tab = []
        if self.project_tools:
            tab = self.project_tools.split(";")
        return tab
    
class Category(models.Model):
    category_url = models.CharField(max_length=30, blank= True)
    category_name = models.CharField(max_length=30, blank = True)