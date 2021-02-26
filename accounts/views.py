from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import AccountForm
from .models import Account

# Create your views here.
def account_list(request):
    accounts = Account.objects.all()
    context = {
        'account_list':accounts
    }
    return render(request, "account_list.html", context)

def account_detail(request, account_email):
        account = Account.objects.get(email=account_email)
        context = {
            'account': account
        }
        return render(request, "account_detail.html", context)


def Create(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/accounts')
    context = {
        "form":form,
        'form_type': 'Create'
    }
    return render(request, "SignUp.html", context) 

def Update(request, account_id):
    account = Account.objects.get(id=account_id)
    form = AccountForm(request.POST or None, instance=account)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/accounts')

    context = {
        "form":form,
        'form_type': 'Update'
    }
    return render(request, "SignUp.html", context) 

def Delete(request, account_id):
    account = Account.objects.get(id=account_id)
    account.delete()
    return HttpResponseRedirect('/accounts')