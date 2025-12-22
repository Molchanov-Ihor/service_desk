from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from apps.tickets.forms import TicketCreateForm, TicketUpdateForm
from apps.tickets.models import Ticket


class TicketListView(ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'tickets.html'
    paginate_by = 30


class TicketDetailView(DetailView):
    model = Ticket
    context_object_name = 'ticket'
    template_name = 'ticket_detail.html'


class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketCreateForm
    template_name = 'tickets/ticket_create.html'
    success_url = reverse_lazy('tickets:tickets-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketUpdateForm
    template_name = 'tickets/ticket_update.html'
    success_url = reverse_lazy('tickets:tickets-list')
