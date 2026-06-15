from django.shortcuts import render,redirect
from models import ContactMessage
from main.models import ContactMessage
from .forms import ContactForm
# from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    project_list = [
        {
            "name": "NotekKro App",
            "description": "Django Notes CRUD app",
            "tech": "Python, Django",
            "live": "https://django-notes-crud-production.up.railway.app/",
            "github": "https://github.com/ajaykr999/django-notes-crud",
            "features": []
        },
        {
            "name": "Mitti App",
            "description": "Wellness App",
            "tech": "Python, Django",
            "live": "https://mitti-4.onrender.com/",
            "github": "https://github.com/ajaykr999/mitti",
            "features": []
        }
    ]

    return render(request, 'project.html', {'projects': project_list})





def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )

            messages.success(request, '✅ Message sent successfully!')
            return redirect('contact')

    return render(request, 'contact.html', {'form': form})