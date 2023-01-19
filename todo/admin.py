from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.site_title = 'To Do Woo'
admin.site.site_header = 'Админ-панель Сайта To Do Woo'


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'memo', 'created', 'date_completed', 'important', 'user')  # Отображаемые поля
    list_display_links = ('id', 'title')  # Поля в виде ссылки для перехода к конкретной записи
    search_fields = ('id', 'title')  # Поля по которым можно производить поиск
    list_editable = ('important',)
    list_filter = ('created', 'date_completed', 'user')
    readonly_fields = ('created',)
    fields = ('title', 'memo', 'created', 'date_completed', 'important', 'user')


admin.site.register(Todo, TodoAdmin)
