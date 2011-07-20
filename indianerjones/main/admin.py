import main.models
from django.contrib import admin

class CountryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'flag',)
	pass

class UniversityAdmin(admin.ModelAdmin):
#    fields = ('name', 'country')
#    fields = ()
#    exclude = ('name',)
     list_display = ('name', 'country',)

def getCountryFromDepartment(obj):
        return obj.university.country

getCountryFromDepartment.short_description = 'Country'

class DepartmentAdmin(admin.ModelAdmin):
     list_display = ('name', 'university', getCountryFromDepartment)

class LinkAdmin(admin.ModelAdmin):
     list_display = ('name', 'url',)

def getUniversity(obj):
	return obj.department.university
getUniversity.short_description = 'University'

def getDissertation(obj):
	if not obj.subtitle:
		return obj.title

	return ("%s - %s" % (obj.title, obj.subtitle))

getDissertation.short_description = 'Dissertation'

def getCountryFromStudent(obj):
	return obj.department.university.country

getCountryFromStudent.short_description = 'Country'

class StudentAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', getUniversity, getCountryFromStudent, 'department', 'publish_date', getDissertation)

admin.site.register(main.models.Country, CountryAdmin)
admin.site.register(main.models.University, UniversityAdmin)
admin.site.register(main.models.Department, DepartmentAdmin)
admin.site.register(main.models.Link, LinkAdmin)
admin.site.register(main.models.Student, StudentAdmin)
