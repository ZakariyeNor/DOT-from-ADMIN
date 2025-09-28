from django.urls import path
from . import views

urlpatterns = [
    # Mission URLs
    path('missions/', views.mission_list, name='mission_list'),
    path('missions/create/', views.mission_create, name='mission_create'),
    path('missions/<int:pk>/', views.mission_detail, name='mission_detail'),
    path('missions/<int:pk>/edit/', views.mission_update, name='mission_update'),
    path('missions/<int:mission_id>/assign/<int:agent_id>/', views.assign_agent_to_mission, name='assign_agent'),
    path('agents/', views.agent_list, name='agent_list'),
    path('agents/<int:agent_id>/status/<str:new_status>/', views.change_agent_status, name='change_agent_status'),
    path('missions/<int:pk>/update_status/', views.mission_update_status, name='mission_update_status'),
]
