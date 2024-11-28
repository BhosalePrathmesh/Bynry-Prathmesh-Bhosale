# creating admin views
from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'status', 'created_at', 'updated_at')
    search_fields = ('user__username', 'service_type', 'status')
    list_filter = ('service_type', 'status')
    readonly_fields = ('created_at', 'updated_at')
