import models
from django.contrib import admin

class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None                   , {'fields':['full_name','number','order', 'is_active']}),
        ('Personal Information' , {'fields':['birth_date','weight','height','cv', 'info','cv_image','roster_image']}),
        ('Skills'               , {'fields':['stick','position','speed','agility','shoot','puck_control', ]}),
            
    ]
    list_display = ('full_name', 'is_active')

admin.site.register(models.Player, PlayerAdmin)
admin.site.register(models.Application)

