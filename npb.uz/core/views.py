from django.shortcuts import redirect, render
from .forms import ContactForm
from requests import get
import requests
# Create your views here.

def home(request):
    print(request.method)
    if request.method == "POST":
        print(request.POST)
        form = ContactForm(data=request.POST)
        if form.is_valid():
            fullname = request.POST.get("fullname")
            phone = request.POST.get("phone")
            get("https://api.telegram.org/bot5046439124:AAFUJMJzy2dCWNObY1rbEZIWpJ6P7fpR0nA/sendMessage?chat_id=@nbpplast&text={}".format(
                f"Имя: {fullname}\nТелефонный номер: {phone}"
            ))
            return redirect('/')
    return render(request, 'index.html')