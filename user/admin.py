from django.contrib import admin

from user.models import userdetail,books

class userdataAdmin(admin.ModelAdmin):
    list_display=['username','name','store']

admin.site.register(userdetail,userdataAdmin)

class bookdataAdmin(admin.ModelAdmin):
    list_display=['username','store','book','counts','price','author']
    

admin.site.register(books,bookdataAdmin)

