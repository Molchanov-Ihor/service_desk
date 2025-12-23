from django.urls import path

from apps.tickets import views

app_name = 'tickets'
urlpatterns = [
    path('', views.TicketListView.as_view(), name='tickets-list'),
    path('create/', views.TicketCreateView.as_view(), name='create-ticket'),
    path('<int:pk>/', views.TicketDetailView.as_view(), name='ticket-detail'),
    path('edit/<int:pk>/', views.TicketUpdateView.as_view(), name='ticket-update'),
    path('delete/<int:pk>/', views.TicketDeleteView.as_view(), name='ticket-delete'),

    path('statuses/', views.StatusListView.as_view(), name='statuses-list'),
    path('statuses/create/', views.StatusCreateView.as_view(), name='create-status'),
    path('statuses/edit/<int:pk>/', views.StatusUpdateView.as_view(), name='status-update'),
    path('statuses/delete/<int:pk>/', views.StatusUpdateView.as_view(), name='status-delete'),
]
