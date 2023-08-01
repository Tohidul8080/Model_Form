from django.contrib import admin
from First_App.models import First_Table
from First_App.models import Second_table

# Register your models here.
admin.site.register(First_Table)
admin.site.register(Second_table)
