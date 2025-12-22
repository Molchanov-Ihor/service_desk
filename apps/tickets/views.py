from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from apps.tickets.models import Ticket


class TicketListView(ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'tickets.html'
    paginate_by = 30


class TicketDetailView(DetailView):
    model = Ticket
    context_object_name = 'ticket'
    template_name = 'ticket.html'

# class TicketCreateView(CreateView):
#     model = Ticket
#     form_class = TicketForm()
#     template_name = 'ticket.html'
#     success_url = reverse_lazy('tickets:list')