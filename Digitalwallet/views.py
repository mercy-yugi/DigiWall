from django.shortcuts import render

from Digitalwallet.models import Account, Card, Customer, Loan, Notifications, Receipt, Reward, ThirdParty, Transaction, Wallet
# from .forms import AccountForm, CardForm, CustomerRegistrationForm, NotificationForm, ReceiptForm, RewardForm, ThirdpartyForm, TransactionForm, WalletForm
from .import forms
# handles httpRequest
# Create your views here.
# content of a http request.
def register_customer(request):
    if request.method == 'POST':
        form = forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.CustomerRegistrationForm()
    return render(request, 'wallet/register_customer.html', {
        "form": form
    })
def list_customers(request):
    customer=Customer.objects.all()
    return render(request, 'wallet/list_customer.html', {
        "customers": customer})

# account information
def account_form(request):
    if request.method == 'POST':
        form = forms.AccountForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.AccountForm()
    return render(request, 'wallet/account_form.html',{
        "form": form
    })
def list_accounts(request):
    account=Account.objects.all()
    return render(request, 'wallet/list_accounts.html',{
        "accounts":account})


# card information
def card_form(request):
    if request.method == 'POST':
        form = forms.CardForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.CardForm()
    return render(request, 'wallet/card_form.html', {
        "form": form
    })
def list_cards(request):
    card=Card.objects.all()
    return render(request, 'wallet/list_cards.html', {
        "cards": card})

# notification information

def notification_form(request):
    if request.method == 'POST':
        form = forms.NotificationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.NotificationForm()
    return render(request, 'wallet/notification_form.html', {
        "form": form
    })
def list_notifications(request):
    notification=Notifications.objects.all()
    return render(request, 'wallet/list_notifications.html', {
        "notifications": notification})


# receipt notifications
def receipt_form(request):
    if request.method == 'POST':
        form = forms.ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.ReceiptForm()
    return render(request, 'wallet/receipt_form.html', {
        "form": form
    })
def list_receipt(request):
    receipt=Receipt.objects.all()
    return render(request, 'wallet/list_receipt.html', {
        "receipts": receipt})

# reward information
def reward_form(request):
    if request.method == 'POST':
        form = forms.RewardForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.RewardForm()
    return render(request, 'wallet/reward_form.html', {
        "form": form
    })
def list_reward(request):
    reward=Reward.objects.all()
    return render(request, 'wallet/list_reward.html', {
        "rewards": reward})


# Thirdparty payment
def thirdparty_form(request):
    if request.method == 'POST':
        form = forms.ThirdpartyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.ThirdpartyForm()
    return render(request, 'wallet/thirdparty_form.html', {
        "form": form
    })
def list_thirdparty(request):
    thirdparty=ThirdParty.objects.all()
    return render(request, 'wallet/list_thirdparty.html', {
        "thirdpartys": thirdparty})


# transaction information
def transaction_form(request):
    if request.method == 'POST':
        form = forms.TransactionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.TransactionForm()
    return render(request, 'wallet/transaction_form.html', {
        "form": form
    })
def list_transaction(request):
    transaction=Transaction.objects.all()
    return render(request, 'wallet/list_transaction.html', {
        "transactions": transaction})


# wallet transaction
def wallet_form(request):
    if request.method == 'POST':
        form = forms.WalletForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.WalletForm()
    return render(request, 'wallet/wallet_form.html', {
        "form": form
    })
def list_wallet(request):
    wallet=Wallet.objects.all()
    return render(request, 'wallet/list_wallet.html', {
        "wallets": wallet})

# loan information
def loan_form(request):
    if request.method == 'POST':
        form = forms.LoanForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        loan=forms.LoanForm()
    return render(request, 'wallet/wallet_form.html', {
         "form": form
    })
def list_wallet(request):
    loan=Loan.objects.all()
    return render(request, 'wallet/list_loan.html', {
        "loans": loan})