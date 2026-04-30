from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
# from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'project.html')

def contact(request):
    return render(request, 'contact.html')

# contact form

def contact_view(request):
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            print(name, email, message)  # abhi testing ke liye
            
    return render(request, 'contact.html', {'form': form})