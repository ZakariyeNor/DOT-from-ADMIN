from django.contrib import admin
from .models import Agent, Mission, MissionLog

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('agent_code', 'user', 'rank', 'status')
    list_filter = ('rank', 'status')
    search_fields = ('agent_code', 'user__username', 'user__email')

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'mission_type', 'status', 'start_date', 'end_date')
    list_filter = ('mission_type', 'status')
    search_fields = ('name',)
    filter_horizontal = ('agents',)

@admin.register(MissionLog)
class MissionLogAdmin(admin.ModelAdmin):
    list_display = ('mission', 'agent', 'timestamp', 'note')
    list_filter = ('mission', 'agent')
    search_fields = ('note',)