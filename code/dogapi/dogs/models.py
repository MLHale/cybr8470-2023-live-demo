# @Author: Matthew Hale <mlhale>
# @Date:   2023-09-11T18:20:06-05:00
# @Email:  mlhale@unomaha.edu
# @Filename: models.py
# @Last modified by:   mlhale
# @Last modified time: 2023-09-18T18:45:19-05:00
# @Copyright: Copyright (C) 2019 Matthew L. Hale



from django.db import models

# Create your models here.
class Dog(models.Model):
    first_name = models.CharField(max_length=30)
    breed = models.CharField(max_length=40)
    
    def __str__(self):
        return str(self.id)+ " : " + str(self.first_name)
