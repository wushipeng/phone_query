from django.contrib import admin
from phone_query.models import PersonPhone,RegionalPhone
# Register your models here.



class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'pyjc', 'phone_number', 'part')

    # 筛选器
    list_filter =  ('name', 'pyjc', 'phone_number', 'part')  # 过滤器
    search_fields = ('name', 'pyjc', 'phone_number', 'part') # 搜索字段

class RegionAdmin(admin.ModelAdmin):
    list_display = ('city_name','phone_number')
    list_filter = ('city_name','phone_number')
    search_fields = ('city_name','phone_number')

admin.site.site_header = "电话分机查询"  #后台标题

# admin.site.register([RegionalPhone])
admin.site.register(PersonPhone,PersonAdmin)
admin.site.register(RegionalPhone,RegionAdmin)

