from django.contrib import admin
from .models import BodyData
from .models import BodyParts
from  .models import BodytestStandard
from  .models import UserPysicalTest
from .models import starlevel
from .models import GradeLevel
from .models import Courses
from .models import PartCourse
# Register your models here.
class Courseadmin(admin.ModelAdmin):
    list_display=("courseid","coursename","decription","pic")
    list_display_links=("courseid","coursename","decription","pic")

class PartCourseadmin(admin.ModelAdmin):
    list_display = ("partcode","courseid","courselevel","frequency")
    list_display_links = ("partcode","courseid","courselevel","frequency")

class GradeLe(admin.ModelAdmin):
    list_display = ("grade","level")

    list_display_links=("grade","level")

admin.site.register(GradeLevel,GradeLe)
admin.site.register(BodyData)
admin.site.register(BodyParts)
admin.site.register(BodytestStandard)
admin.site.register(UserPysicalTest)
admin.site.register(starlevel)
admin.site.register(Courses,Courseadmin)
admin.site.register(PartCourse,PartCourseadmin)

