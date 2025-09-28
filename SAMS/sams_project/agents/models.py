from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.utils import timezone

# Helper function to generate unique agent codes
def generate_agent_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


# Agent model
class Agent(models.Model):
    # Link to Django User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Unique agent code
    agent_code = models.CharField(max_length=10, unique=True, default=generate_agent_code)

    # Rank choices
    RANK_CHOICES = [
        ('Field Agent', 'Field Agent'),
        ('Analyst', 'Analyst'),
        ('Director', 'Director'),
    ]
    rank = models.CharField(max_length=20, choices=RANK_CHOICES)

    # Status
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Retired', 'Retired'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')

    # Assigned missions (ManyToMany)
    assigned_missions = models.ManyToManyField('Mission', blank=True)

    # Custom permissions
    class Meta:
        permissions = [
            ("can_assign_mission", "Can assign missions to agents"),
            ("can_change_status", "Can change agent status"),
            ("can_create_mission", "Can create new missions"),
        ]

    def __str__(self):
        return f"{self.agent_code} ({self.user.username})"

# Mission model
class Mission(models.Model):
    MISSION_TYPE_CHOICES = [
        ('Recon', 'Reconnaissance'),
        ('Rescue', 'Rescue Operation'),
        ('Surveillance', 'Surveillance'),
        ('Assassination', 'Assassination'),
    ]

    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    mission_type = models.CharField(max_length=20, choices=MISSION_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Planned')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    agents = models.ManyToManyField('Agent', related_name='missions', blank=True)

    # Progress tracking
    progress_percentage = models.IntegerField(default=0) 
    
    def __str__(self):
        return f"{self.name} ({self.mission_type})"
    

# Mission log model
class MissionLog(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='logs')
    agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    note = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.agent} - {self.mission.name}"