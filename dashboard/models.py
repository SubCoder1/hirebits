from django.db import models

class learn_statements(models.Model):
    s_lname = models.CharField(max_length=200)
    s_ldescrip = models.CharField(max_length=400)
    s_lcontent = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.s_lname

class Problem_statements(models.Model):
    s_name = models.CharField(max_length=200)
    s_descrip = models.CharField(max_length=400)
    s_content = models.TextField()
    s_company = models.CharField(max_length=150)

    objects = models.Manager()

    def __str__(self):
        return self.s_name