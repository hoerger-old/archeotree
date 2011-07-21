import main.models
from django.contrib import admin

class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name']

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)
    search_fields = ['name', 'country__name']

class DepartmentAdmin(admin.ModelAdmin):
    def getCountryFromDepartment(obj):
            return obj.university.country
    getCountryFromDepartment.short_description = 'Country'

    search_fields = ['name', 'university__name', 'university__country__name']
    list_display = ('name', 'university', getCountryFromDepartment)

class LinkAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'url', 'student')

class LinkInlineAdmin(admin.TabularInline):
    model = main.models.Link
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    def getUniversity(obj):
        return obj.department.university
    def getDissertation(obj):
        if not obj.subtitle:
            return obj.title
        return ("%s - %s" % (obj.title, obj.subtitle))
    def getCountryFromStudent(obj):
        return obj.department.university.country

    getDissertation.short_description = 'Dissertation'
    getUniversity.short_description = 'University'
    getCountryFromStudent.short_description = 'Country'

    search_fields = ['first_name', 'middle_name', 'last_name']
    list_display = ('__unicode__', getUniversity, getCountryFromStudent, 'department', 'publish_date', getDissertation)
    inlines = [LinkInlineAdmin]
    filter_horizontal = ['adviser']
    fieldsets = (
        (None, {
            'fields': ('first_name', 'middle_name', 'last_name', 'publish_date','adviser', 'title', 'subtitle', 'department', 'isbn' )
        }),
    )

admin.site.register(main.models.Country, CountryAdmin)
admin.site.register(main.models.University, UniversityAdmin)
admin.site.register(main.models.Department, DepartmentAdmin)
admin.site.register(main.models.Link, LinkAdmin)
admin.site.register(main.models.Student, StudentAdmin)
