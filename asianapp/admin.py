from django.contrib import admin
from asianapp.models import *

class CustomerEmailAdmin(admin.ModelAdmin):

    list_display = ('firstname', 'lastname', 'customeremails', 'customermessage', 'status')

# Register your models here.
admin.site.register(Header)
admin.site.register(Content)
admin.site.register(Slider)
admin.site.register(Video)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Contact)
admin.site.register(SocialLink)
admin.site.register(NewsUpdate)
admin.site.register(Advertisement)
admin.site.register(CustomerEmail, CustomerEmailAdmin)
