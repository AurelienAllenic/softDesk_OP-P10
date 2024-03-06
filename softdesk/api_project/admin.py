from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api_user.models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'age', 'consent', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'age',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Consent', {'fields': ('consent',), 'classes': ('readonly',)}),  # Ajout du champ 'consent' en lecture seule
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'age', 'is_staff', 'is_active', 'consent',)}
        ),
    )
    search_fields = ('username', 'email',)
    ordering = ('username',)
    readonly_fields = ('consent',)  # Déclarer le champ 'consent' comme lecture seule

admin.site.register(CustomUser, CustomUserAdmin)
