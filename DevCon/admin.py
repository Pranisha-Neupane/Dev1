from django.contrib import admin


from django.contrib import admin
from .models import CustomUser, Room, Message, Participents
admin.site.register(CustomUser)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Participents)
