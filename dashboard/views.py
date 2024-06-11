from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from api.models import Machine, Attack, AttackResult
from .helpers import _paginator
# Create your views here.
from rich import print

def home(request):
    
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {
        'pagename': 'Dashboard',
        'machines': Machine.objects.all()
    }
    attacks = Attack.objects.all()
    for attack in attacks:
        total_results_num = AttackResult.objects.filter(attack=attack).count()
        success_results_num = AttackResult.objects.filter(attack=attack, success=True).count()
        success_rate = (success_results_num / total_results_num) * 100
        attack.__setattr__('success_rate', success_rate)
    
    context['attacks'] = attacks
    
    return render(request, 'dashboard/dashboard.html', context=context)

def machines(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {
        'pagename': 'Dashboard',
        'machines': Machine.objects.all()
    }
    attacks = Attack.objects.all()
    for attack in attacks:
        total_results_num = AttackResult.objects.filter(attack=attack).count()
        success_results_num = AttackResult.objects.filter(attack=attack, success=True).count()
        success_rate = (success_results_num / total_results_num) * 100
        
        attack.__setattr__('success_rate', success_rate)
    
    context['attacks'] = attacks
    
    return render(request, 'dashboard/machines.html', context=context)


def attacks(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {
        'pagename': 'Attacks'
    }
    attacks = Attack.objects.all()
    for attack in attacks:
        total_results_num = AttackResult.objects.filter(attack=attack).count()
        success_results_num = AttackResult.objects.filter(attack=attack, success=True).count()
        success_rate = (success_results_num / total_results_num) * 100
        attack.__setattr__('success_rate', success_rate)
    
    context['attacks'] = attacks
    
    return render(request, 'dashboard/attack.html', context=context)


def attack_results(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {
        'pagename': 'Attack Results',
        'filter_options': [attack.name.title() for attack in Attack.objects.all()]
    }
    
    machine_id = request.GET.get('machine_id', None)
    mitre_id = request.GET.get('mitre_id', None)
    
    results = AttackResult.objects.all().order_by('-executed_date')
    
    if machine_id:
        machine = Machine.objects.filter(id=machine_id).first()
        results = results.filter(machine=machine)    
        
    
    if mitre_id:
        attack = Attack.objects.filter(mitre_id=mitre_id).first()
        results = results.filter(attack=attack)
        
        
    #pagination
    results = _paginator(request, results, num_per_page=10)
    
    context['results'] = results
    
    return render(request, 'dashboard/attack_results.html', context=context)


def result_detail(request, id):
    context = {
        'pagename': 'Result Detail',
        'result': AttackResult.objects.get(id=id)
    }

    return render(request, 'dashboard/attack_result_detail.html', context=context)