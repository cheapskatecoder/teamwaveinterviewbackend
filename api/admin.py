from django.contrib import admin
from api.models import Query

class QueryAdmin(admin.ModelAdmin):
    readonly_fields = ['date_created']

admin.site.register(Query, QueryAdmin)
