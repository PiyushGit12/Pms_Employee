from django.db import models

# Create your models here.

class EmpDaTa (models.Model):

     fname =models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     job_title = models.CharField(max_length=25, default="NA")
     last_ap_date = models.CharField(max_length=100)
     reporting_mail = models.EmailField(max_length=50)
     doj = models.CharField(max_length=100)
     evalute_by = models.CharField(max_length=100)

    # def _str_(self):
    #     return self.fname



class Emp_details(models.Model):
    emp_id = models.IntegerField(default=00)
    goal_title = models.CharField(max_length=100)
    goal_description = models.CharField(max_length=100)
    reporting_mail = models.EmailField(max_length=50)
    due_date = models.CharField(max_length=25, default="NA")
    job_title = models.CharField(max_length=25, default="NA")