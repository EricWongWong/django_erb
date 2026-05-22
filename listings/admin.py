from django.contrib import admin
from django import forms
from .models import Listing
from taggit.forms import TagWidget
from django.forms import NumberInput
from django.db import models
# Register your models here.""

class ListingAdminForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        widgets = {
            'services' : TagWidget(),
        }


class ListingAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published', 'tag_list', 'list_date', "doctor"
    list_display_links = ('id', 'title')
    list_filter = ('doctor', "services")
    list_editable = ('is_published',)
    search_fields = ('title', 'description', "doctor__name","services__name",) 
    list_per_page = 25
    formfield_overrides = {
        models.IntegerField: {
        "widget": forms.NumberInput(attrs={"size":"10"})
        }
    }

    def get_queryset(self,request):
        return super().get_queryset(request).prefetch_related("services")
    
    def tag_list(self, obj):
        return ", ".join([tag.name for tag in obj.services.all()]) or "No tags"
        tag_list.short_description = "Services"

admin.site.register(Listing, ListingAdmin) 
