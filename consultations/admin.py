from django.contrib import admin
from .models import Consultation, ConsultationAvailability


class ConsultationAvailabilityInline(admin.TabularInline):
    model = ConsultationAvailability
    extra = 1

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'price', 'image', 'rating')
    inlines = [ConsultationAvailabilityInline]
    ordering = ('sku',)

admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(ConsultationAvailability)