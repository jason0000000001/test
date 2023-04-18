from django.contrib import admin

# Register your models here.

#from .models import Room
from .models import User
from .models import Data
from .models import Medicine


#admin.site.register(Room)
admin.site.register(User)
admin.site.register(Data)
admin.site.register(Medicine)

