import main.models
from django.contrib import admin

class CountryAdmin(admin.ModelAdmin):
    pass

class UniversityAdmin(admin.ModelAdmin):
    pass

class DepartmentAdmin(admin.ModelAdmin):
    pass

class LinkAdmin(admin.ModelAdmin):
    pass

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(main.models.Country, CountryAdmin)
admin.site.register(main.models.University, UniversityAdmin)
admin.site.register(main.models.Department, DepartmentAdmin)
admin.site.register(main.models.Link, LinkAdmin)
admin.site.register(main.models.Student, StudentAdmin)
