from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
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

    fieldsets = (
        ('Profile', {
            "fields": (('user', 'picture'),),
        }),
        ('Extra info',{
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
        })
    )
    # Si no se agrega no se pueden agregar en la linea de 
    # arriba ya que solo son datos de lectura
    readonly_fields = ('created', 'modified')
    

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False;
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)