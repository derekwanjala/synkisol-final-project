from django.contrib import admin

from .models import About, Clients, Company, Service, Strategy, Team

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'status', 'updated']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_detail', 'status']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_detail', 'status',]


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'image']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'status', 'image']
    readonly_fields = ['image']


@admin.register(Strategy)
class StrategyAdmin(admin.ModelAdmin):
    list_display = ['mission', 'vision', 'quality']