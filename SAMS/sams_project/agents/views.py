from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Mission, Agent
from .forms import MissionForm, MissionLogForm, MissionUpdateForm

from django.http import HttpResponseForbidden

@login_required
def mission_list(request):
    missions = Mission.objects.all()
    return render(request, 'agents/mission_list.html', {'missions': missions})

@login_required
def mission_detail(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    return render(request, 'agents/mission_detail.html', {'mission': mission})

@login_required
def mission_create(request):
    if not request.user.has_perm('agents.can_create_mission'):
        return HttpResponseForbidden(
            'You do not have permission to create missions.'
        )
    
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mission_list')
    else:
        form = MissionForm()
    return render(request, 'agents/mission_form.html', {'form': form})

@login_required
def assign_agent_to_mission(request, mission_id, agent_id):
    if not request.user.has_perm('agents.can_assign_mission'):
        return HttpResponseForbidden(
            'You do not have permission to assign agents.'
        )

    mission = get_object_or_404(Mission, pk=mission_id)
    agent = get_object_or_404(Agent, pk=agent_id)
    mission.agents.add(agent)
    return redirect('mission_detail', pk=mission_id)

@login_required
def change_agent_status(request, agent_id, new_status):
    if not request.user.has_perm('agents.can_change_status'):
        return HttpResponseForbidden(
            'You do not have permission to change agent status.'
        )
    
    agent = get_object_or_404(Agent, pk=agent_id)
    if new_status not in dict(Agent.STATUS_CHOICES):
        return HttpResponseForbidden('Invalid status value.')
    agent.status = new_status
    agent.save()
    return redirect('agent_detail', pk=agent_id)

@login_required
def mission_update(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    if request.method == 'POST':
        form = MissionForm(request.POST, instance=mission)
        if form.is_valid():
            form.save()
            return redirect('mission_detail', pk=pk)
    else:
        form = MissionForm(instance=mission)
    return render(request, 'agents/mission_form.html', {'form': form})


@login_required
def mission_update_status(request, pk):
    mission = get_object_or_404(Mission, pk=pk)
    
    if not request.user.has_perm('agents.can_assign_mission'):
        return HttpResponseForbidden("You do not have permission to update missions.")

    if request.method == 'POST':
        form = MissionUpdateForm(request.POST, instance=mission)
        log_form = MissionLogForm(request.POST)
        if form.is_valid() and log_form.is_valid():
            form.save()
            log = log_form.save(commit=False)
            log.mission = mission
            log.save()
            return redirect('mission_detail', pk=mission.pk)
    else:
        form = MissionUpdateForm(instance=mission)
        log_form = MissionLogForm()
    return render(request, 'agents/mission_update_status.html', {'form': form, 'log_form': log_form})

@login_required
def agent_list(request):
    agents = Agent.objects.all()
    return render(request, 'agents/agent_list.html', {'agents': agents})