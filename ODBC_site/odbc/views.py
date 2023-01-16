from django.shortcuts import render, redirect
from odbc.models import events
from odbc.forms import EditEventsForm

# Create your views here.

# homepage
def index(request):
    
    style_name = 'index'
    
    return render(request, 'odbc/index.html', {'style_name' : style_name})


# about page
def about(request):

    style_name = 'about'
    
    return render(request, 'odbc/about.html', {'style_name' : style_name})


# announcements page
def announcements(request):

    style_name = 'announcements'

    odbc_events = events.objects.order_by('event_date')
    
    return render(request, 'odbc/announcements-news.html', {'style_name' : style_name, 'odbc_events': odbc_events})


# admin dashboard
def odbc_admin(request):

    odbc_events = events.objects.order_by('event_date')

    return render(request, 'odbc/odbc-admin.html', {'odbc_events': odbc_events})


# create new event
def odbc_admin_create(request):
    
    event_form = EditEventsForm()

    if request.method == "POST":

        event_form = EditEventsForm(request.POST, request.FILES)

        if event_form.is_valid():
            
            event_form.save(commit=True)

            return redirect('odbc-admin')

    return render(request, 'odbc/event-form.html', {'event_form': event_form})


# update existing event
def odbc_admin_update(request, id):

    update_form = events.objects.get(id=id)

    event_form = EditEventsForm(instance=update_form)

    if request.method == "POST":

        event_form = EditEventsForm(request.POST, instance=update_form)

        if event_form.is_valid():
            
            event_form.save(commit=True)

            return redirect('odbc-admin')

    return render(request, 'odbc/event-form.html', {'event_form': event_form})


# delete an event
def odbc_admin_delete(request, id):

    update_form = events.objects.get(id=id)

    if request.method == "POST":

        update_form.delete()

        return redirect('odbc-admin')        

    return render(request, 'odbc/event-form-delete.html', {'item': update_form})