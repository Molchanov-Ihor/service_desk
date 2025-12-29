from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.tickets.forms import TicketCreateForm, TicketUpdateForm, StatusForm
from apps.tickets.models import Ticket, Status


class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'tickets.html'

    def get_queryset(self):

        if self.request.user.position.id == 1:
            queryset = Ticket.objects.filter(author=self.request.user).select_related('author', 'executor', 'status')
        else:
            queryset = Ticket.objects.all().select_related('executor', 'status')
        print(queryset)
        return queryset


class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    context_object_name = 'ticket'
    template_name = 'ticket_detail.html'


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketCreateForm
    template_name = 'tickets/ticket_create.html'
    success_url = reverse_lazy('tickets:tickets-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = Status.objects.get(pk=1)
        return super().form_valid(form)

    def get_queryset(self):
        queryset = Ticket.objects.select_related('author', 'executor', 'status')
        return queryset


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    form_class = TicketUpdateForm
    template_name = 'tickets/ticket_update.html'
    success_url = reverse_lazy('tickets:tickets-list')


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    context_object_name = 'ticket'
    success_url = reverse_lazy('tickets:tickets-list')


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'status/statuses_list.html'


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'status/status_form.html'
    success_url = reverse_lazy('tickets:statuses-list')


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'status/status_form.html'
    success_url = reverse_lazy('tickets:statuses-list')


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    context_object_name = 'status'
    success_url = reverse_lazy('tickets:statuses-list')
