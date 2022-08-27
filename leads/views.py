from django.shortcuts import render
from .models import Leads
from .models import Agent
from django.shortcuts import redirect
from .forms import LeadModelCreateForm
from django.views.generic import TemplateView
from django.views import generic
from leads.forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('leads:lead_list')

def lead_list(request):

    leads = Leads.objects.all()
    context = {
        'leads': leads
    }
    return render(request, 'leads/lead-list.html', context)

def lead_detail(request, pk):

    lead = Leads.objects.get(id=pk)
    context = {
        'lead': lead        
    }
    return render(request, 'leads/lead-detail.html', context)

def lead_create(request):

    #New version
    form = LeadModelCreateForm
    if request.method == "POST":
        form = LeadModelCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads:lead_list')
    context = {
        'form': form
    }
    return render(request, 'leads/lead-create.html', context)

def lead_delete(request, pk):

    lead = Leads.objects.get(id=pk)
    lead.delete()
    return redirect('leads:lead_list')

def lead_update(request, pk):

    #New version
    lead = Leads.objects.get(id=pk)
    form = LeadModelCreateForm(instance=lead)
    if request.method == "POST":
        form = LeadModelCreateForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads:lead_list')
    context = {
        'form': form
    }
    print(form)
    return render(request, 'leads/lead-create.html', context)

class LandingPageView(TemplateView):

    template_name = 'leads/landing-page.html'
