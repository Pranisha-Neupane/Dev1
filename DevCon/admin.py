from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Room, Message, Participents

# Register other models
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Participents)

# Register CustomUser model with custom display settings
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'is_staff', 'is_superuser')
    ordering = ('email',)
    search_fields = ('email', 'username')
    # ✅ DO NOT add 'email' to fieldsets manually — it's already handled
