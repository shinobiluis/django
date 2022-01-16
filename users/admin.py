from django.contrib import admin
#importamos el modelo de Profile
from users.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')

    # Hacer que al dar click al numero nos abra el registro
    list_display_links = ('pk' ,'user', 'phone_number')

    #edicion rapida
    list_editable = ('website', 'picture')

    #Agregando buscador
    # se agreag user__ para decir que se puede buscar por el correo de ese usuario
    search_fields = (
        'user__email', 
        'user__username', 
        'user__first_name', 
        'user__last_name', 
        'phone_number'
    )

    # Agregando filtros
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )