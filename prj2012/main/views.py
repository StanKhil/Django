from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from main.forms import *
from django.core.files.storage import FileSystemStorage
# Create your views here.

@csrf_protect
def get_contacts(request):
    contact_form = {}
    if request.method == "POST":
        contact_form['name'] = request.POST.get("name")
        contact_form['age'] = request.POST.get("age")
        contact_form['email'] = request.POST.get("email")
        contact_form['bio'] = request.POST.get("bio")
        contact_form['agree'] = request.POST.get("agree")
        contact_form["sent"] = True
        return render(request, "contacts.html", contact_form)
    return render(request, "contacts.html", {'sent': False})

class ContactFormView(TemplateView):
    template_name = "contactCBV.html"
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)
    def post(self, request, *args, **kwargs):
        contact_form = {}
        contact_form['name'] = request.POST.get("name")
        contact_form['age'] = request.POST.get("age")
        contact_form['email'] = request.POST.get("email")
        contact_form['bio'] = request.POST.get("bio")
        contact_form['agree'] = request.POST.get("agree")
        return render(request, self.template_name, contact_form)
@csrf_protect
def prime_numbers(request):
    numbers = {}
    if request.method == "POST":
        numbers["num1"] = request.POST.get("num1")
        numbers["num2"] = request.POST.get("num2")
        numbers["sent"] = True
        primes = []
        for i in range( int(numbers["num1"]), int(numbers["num2"]) + 1):
            if i < 2:
                continue
            else:
                for j in range(2, int(i**0.5) + 1):
                    if i % j == 0:
                        break
                else:
                    primes.append(i)

        return render(request, "prime_numbers.html", {"primes": primes, "sent": True})
    return render(request, "prime_numbers.html", {})

class WaterFormView(TemplateView):
    template_name = "water.html"
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)
    def post(self, request, *args, **kwargs):
        contact_form = {}
        contact_form['name'] = request.POST.get("name")
        contact_form['surname'] = request.POST.get("surname")
        contact_form['email'] = request.POST.get("email")
        contact_form['phone'] = request.POST.get("phone")
        contact_form['duration'] = request.POST.get("duration")
        contact_form['valume'] = request.POST.get("valume")
        return render(request, self.template_name, contact_form)
    

@csrf_protect
def get_contact1(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            return render(request, "contact1.html", {"sent": True})
    else:
        contact_form = ContactForm()
    return render(request, "contact1.html", {"contact_form":contact_form, "sent": False})

@csrf_protect
def get_feedback(request):
    if request.method == "POST":
        feeedback_form = FeedbackForm(request.POST)
        if feeedback_form.is_valid():
            return render(request, "feedback.html", {"sent": True})
    else:
        feeedback_form = FeedbackForm()
    return render(request, "feedback.html", {"feedback_form":feeedback_form, "sent": False})


@csrf_protect
def add_film(request):
    if request.method =='POST':
        form = AddFilmForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES:
                poster = request.FILES["poster"]
                fs = FileSystemStorage()
                filename = fs.save(poster.name, poster)
            return render(request, "film.html", {"sent": True})
    else:
        form = AddFilmForm()
    return render(request, "film.html", {"form":form, "sent": False})