from django.contrib import admin
from .models import Consultation

# Register your models here.
class ConsultationAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'image',
        'rating',
    )

    ordering = ('sku',)

admin.site.register(Consultation, ConsultationAdmin)