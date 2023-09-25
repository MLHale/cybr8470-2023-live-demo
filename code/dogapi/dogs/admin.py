# @Author: Matthew Hale <mlhale>
# @Date:   2023-09-11T18:20:06-05:00
# @Email:  mlhale@unomaha.edu
# @Filename: admin.py
# @Last modified by:   mlhale
# @Last modified time: 2023-09-18T18:44:14-05:00
# @Copyright: Copyright (C) 2019 Matthew L. Hale



from django.contrib import admin
from dogs.models import Dog


# Register your models here.
class DogAdmin(admin.ModelAdmin):
    pass 


admin.site.register(Dog, DogAdmin)
