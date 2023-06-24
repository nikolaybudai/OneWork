import datetime

from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
import django.http
from .models import Offer
from .forms import AddOffer, RegisterUserForm
from django.core.paginator import Paginator


# Create your views here.
def main(request):
    return render(request, "main.html")


def offers(request):
    offers = Offer.objects.all()
    paginator = Paginator(offers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'offers': offers}
    return render(request, "offers.html", context)


def offer(request, offer_id):
    try:
        o = Offer.objects.get(id=offer_id)
        context = {'offer': o}
        print(o.user_id)
        return render(request, "offer.html", context)
    except:
        return django.http.HttpResponseNotFound("Not found")


def category(request, name):
    offers = Offer.objects.filter(category=name)
    paginator = Paginator(offers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'offers': offers}
    return render(request, "offers.html", context)


def add_offer(request):
    context = {}
    if request.method == "POST":
        form = AddOffer(request.POST, request.FILES)
        current_user = request.user
        if form.is_valid():
            offer_entry = form.save(commit=False)
            offer_entry.issued = datetime.datetime.now()
            offer_entry.user_id = current_user.id
            offer_entry.save()
            return redirect('offer', offer_entry.id)
        else:
            message = "Error: incorrect input!"
            context['message'] = message
    else:
        form = AddOffer()
    context['form'] = form
    return render(request, "add_offer.html", context)


def register(request):
    context = {}
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            message = "Error: incorrect input!"
            context['message'] = message
    else:
        form = RegisterUserForm()
    context['form'] = form
    return render(request, "registration/register.html", context)


def profile(request):
    current_user_id = request.user.id
    user_offers = Offer.objects.filter(user_id=current_user_id)
    context = {'user_offers': user_offers}
    return render(request, "profile.html", context)


def delete_offer(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    offer.delete()
    return redirect('profile')
