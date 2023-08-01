from django.db import models


# Create your models here.
class First_Table(models.Model):
    F_Name=models.CharField(max_length=30)
    L_Name=models.CharField(max_length=30)
    V_Name=models.CharField(max_length=40)
    S_Id=models.IntegerField()
    S_Cgpa=models.FloatField()
    S_Age=models.IntegerField()

    class Meta:
      db_table="First_Table"

    def __str__(self):
     return self.F_Name + " " + self.L_Name


class Second_table(models.Model):
   First_Name=models.CharField(max_length=30)
   Last_Name=models.CharField(max_length=30)
   Versity_Name=models.CharField(max_length=40)
   Student_Mail=models.EmailField()

   def __str__(self):
      return self.First_Name + " " + self.Last_Name