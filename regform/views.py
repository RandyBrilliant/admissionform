from regform.forms import StudentForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail


# Create your views here.


def index(request):
    return render(request, "regform/home.html", {})


def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            request.session['register-page'] = True
            form.save()
            # process the data in form.cleaned_data as required
            # send_mail('Thanks for applying to IB IT&B', 'Test Success Message',
            #           'computerclub.itnb@gmail.com',
            #           ['randybrilliant68@gmail.com', 'junottheodore@gmail.com', 'valentinaaali72@gmail.com'])
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('success-page'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentForm()
    context = {
        'form': form
    }
    return render(request, "regform/register.html", context)


def success(request):
    if not request.session.get('register-page', False):
        return redirect('register-page')
    else:
        return render(request, "regform/success.html", {})
