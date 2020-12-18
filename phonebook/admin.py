from django.contrib import admin
from phonebook.models import PhoneBook

class PhoneBookView(admin.ModelAdmin):
    list_display=('id','이름','전화번호','이메일','생년월일')




admin.site.register(PhoneBook,PhoneBookView)

# Register your models here.
