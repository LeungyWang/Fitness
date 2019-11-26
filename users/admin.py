from django.contrib import admin
from .models import New_User
from .models import User_Login
from .models import Admin_Login
# Register your models here.


admin.site.register(New_User)
admin.site.register(User_Login)
admin.site.register(Admin_Login)