from django.urls import path
from .views import (
    MachineListCreateView, MachineDetailView,
    AttackListCreateView, AttackDetailView,
    AttackResultListCreateView, AttackResultDetailView
)

urlpatterns = [
    # Machine URLs
    path('machine/', MachineListCreateView.as_view(), name='machine-list-create'),
    path('machine/<int:id>/', MachineDetailView.as_view(), name='machine-detail'),

    # Attack URLs
    path('attack/', AttackListCreateView.as_view(), name='attack-list-create'),
    path('attack/<int:id>/', AttackDetailView.as_view(), name='attack-detail'),

    # AttackResult URLs
    path('attack-result/', AttackResultListCreateView.as_view(), name='attack-result-list-create'),
    path('attack-result/<int:id>/', AttackResultDetailView.as_view(), name='attack-result-detail'),
]