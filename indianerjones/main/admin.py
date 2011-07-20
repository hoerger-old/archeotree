import main.models
from django.contrib import admin

class CountryAdmin(admin.ModelAdmin):
    pass

class UniversityAdmin(admin.ModelAdmin):
#    fields = ('name', 'country')
#    fields = ()
#    exclude = ('name',)
     list_display = ('name', 'country',)

class DepartmentAdmin(admin.ModelAdmin):
    pass

class LinkAdmin(admin.ModelAdmin):
    pass

def getUniversity(obj):
	return obj.department.university
getUniversity.short_description = 'University'

def getDissertation(obj):
	if not obj.subtitle:
		return obj.title

	return ("%s - %s" % (obj.title, obj.subtitle))

getDissertation.short_description = 'Dissertation'

class StudentAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', getUniversity, 'department', 'publish_date', getDissertation)

admin.site.register(main.models.Country, CountryAdmin)
admin.site.register(main.models.University, UniversityAdmin)
admin.site.register(main.models.Department, DepartmentAdmin)
admin.site.register(main.models.Link, LinkAdmin)
admin.site.register(main.models.Student, StudentAdmin)
