from django.shortcuts import render
from .forms import AccountForm, CardForm, CustomerRegistrationForm, NotificationForm, ReceiptForm, RewardForm, ThirdpartyForm, TransactionForm, WalletForm
# handles httpRequest
# Create your views here.
# content of a http request.
def register_customer(request):
    form=CustomerRegistrationForm()
    return render(request, 'wallet/register_customer.html', {
        "form": form
    })
def account_form(request):
    form=AccountForm()
    return render(request, 'wallet/account_form.html',{
        "form": form
    })
def card_form(request):
    form=CardForm()
    return render(request, 'wallet/card_form.html', {
        "form": form
    })
def notification_form(request):
    form=NotificationForm()
    return render(request, 'wallet/notification_form.html', {
        "form": form
    })
def receipt_form(request):
    form=ReceiptForm()
    return render(request, 'wallet/receipt_form.html', {
        "form": form
    })
def reward_form(request):
    form=RewardForm()
    return render(request, 'wallet/reward_form.html', {
        "form": form
    })
def thirdparty_form(request):
    form=ThirdpartyForm()
    return render(request, 'wallet/thirdparty_form.html', {
        "form": form
    })
def transaction_form(request):
    form=TransactionForm()
    return render(request, 'wallet/transaction_form.html', {
        "form": form
    })
def wallet_form(request):
    form=WalletForm()
    return render(request, 'wallet/wallet_form.html', {
        "form": form
    })
def loan_form(request):
    form=WalletForm()
    return render(request, 'wallet/wallet_form.html', {
        "form": form
    })