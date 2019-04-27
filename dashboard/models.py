from django.db import models

# Create your models here.

class Problem_statements(models.Model):
    s_name = models.CharField(max_length=200)
    s_descrip = models.CharField(max_length=400)
    s_content = models.TextField()
    s_company = models.CharField(max_length=150)

    def __str__(self):
        return self.s_name