from django.db import models
#DataFlair #DataBaseMigrations


class Specs(models.Model):

    admin = models.CharField(max_length = 20)
    emp_id = models.IntegerField(default= 0)
    password = models.CharField(max_length= 20)

    def __str__(self):
        return self.emp_id