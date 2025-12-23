from django import forms

from apps.tickets.models import Ticket, Status


class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Назва тікету',
            'description': 'Опис',
        }


class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'executor': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Назва тікету',
            'description': 'Опис',
            'author': 'Автор',
            'executor': 'Виконувач',
            'status': 'Статус',
        }


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Назва статусу'
        }
