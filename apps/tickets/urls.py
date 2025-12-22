from django.urls import path

from apps.tickets import views

app_name = 'tickets'
urlpatterns = [
    path('', views.TicketListView.as_view(), name='tickets-list'),
    path('create/', views.TicketCreateView.as_view(), name='create-ticket'),
    path('<int:pk>/', views.TicketDetailView.as_view(), name='ticket-detail'),
    path('edit/<int:pk>/', views.TicketUpdateView.as_view(), name='ticket-update'),
]
