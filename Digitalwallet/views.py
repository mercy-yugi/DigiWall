from django.shortcuts import redirect, render

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

def customer_profile(request,id):
    customers=Customer.objects.get(id=id)
    return render(request, 'wallet/customer_profile.html', {
        "customer": customers})

def edit_customer_profile(request,id):
    customer=Customer.objects.get(id=id)
    request.method=="POST"
    form=forms.CustomerRegistrationForm(request.POST,instance=customer)
    if form.is_valid():
        form.save()
        return redirect("customer_profile",id=customer.id)
    else:
        form=forms.CustomerRegistrationForm(instance=customer)
        return render(request,"Digitalwallet/edit_profile.html",{'form':form})
    



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
def wallet_profile(request,id):
    wallet=Wallet.objects.get(id=id)
    return render(request, 'wallet/account_profile.html', {
        "customer": wallet})

def edit_account(request,id):
    account=Account.objects.get(id=id)
    request.method=="POST"
    form=forms.AccountForm(request.POST,instance=account)
    if form.is_valid():
        form.save()
        return redirect("account_profile",id=account.id)
    else:
        form=forms.AccountForm(instance=account)
        return render(request,"Digitalwallet/edit_account.html",{'form':form})




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

def card_profile(request,id):
    card=Card.objects.get(id=id)
    return render(request, 'wallet/card_profile.html', {
        "cards": card})

def card_account(request,id):
    card=Account.objects.get(id=id)
    request.method=="POST"
    form=forms.CardForm(request.POST,instance=card)
    if form.is_valid():
        form.save()
        return redirect("card_profile",id=card.id)
    else:
        form=forms.CardForm(instance=card)
        return render(request,"Digitalwallet/edit_card.html",{'form':form})

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
def notification_profile(request,id):
    notification=Wallet.objects.get(id=id)
    return render(request, 'wallet/account_profile.html', {
        "customer": notification})

def edit_notification(request,id):
    notification=Notifications.objects.get(id=id)
    request.method=="POST"
    form=forms.NotificationForm(request.POST,instance=notification)
    if form.is_valid():
        form.save()
        return redirect("notification_profile",id=notification.id)
    else:
        form=forms.NotificationForm(instance=notification)
        return render(request,"Digitalwallet/edit_notification.html",{'form':form})


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
def receipt_profile(request,id):
    receipt=Receipt.objects.get(id=id)
    return render(request, 'wallet/receipt_profile.html', {
        "receipts": receipt})

def edit_receipt(request,id):
    receipt=Receipt.objects.get(id=id)
    request.method=="POST"
    form=forms.ReceiptForm(request.POST,instance=receipt)
    if form.is_valid():
        form.save()
        return redirect("receipt_profile",id=receipt.id)
    else:
        form=forms.ReceiptForm(instance=receipt)
        return render(request,"Digitalwallet/edit_receipt.html",{'form':form})




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

def reward_profile(request,id):
    reward=Reward.objects.get(id=id)
    return render(request, 'wallet/reward_profile.html', {
        "rewards": reward})

def edit_reward(request,id):
    account=Reward.objects.get(id=id)
    request.method=="POST"
    form=forms.RewardForm(request.POST,instance=account)
    if form.is_valid():
        form.save()
        return redirect("reward_profile",id=account.id)
    else:
        form=forms.RewardForm(instance=account)
        return render(request,"Digitalwallet/edit_reward.html",{'form':form})

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
def thirdparty_profile(request,id):
    third=Reward.objects.get(id=id)
    return render(request, 'wallet/thirdparty_profile.html', {
        "thirds": third})

def edit_thirdparty(request,id):
    account=ThirdParty.objects.get(id=id)
    request.method=="POST"
    form=forms.ThirdParty(request.POST,instance=account)
    if form.is_valid():
        form.save()
        return redirect("reward_profile",id=account.id)
    else:
        form=forms.ThirdpartyForm(instance=account)
        return render(request,"Digitalwallet/edit_thirdparty.html",{'form':form})


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
def transaction_profile(request,id):
    transaction=Transaction.objects.get(id=id)
    return render(request, 'wallet/transaction_profile.html', {
        "transactions": transaction})

def edit_transaction(request,id):
    transaction=Transaction.objects.get(id=id)
    request.method=="POST"
    form=forms.Transaction (request.POST,instance=transaction)
    if form.is_valid():
        form.save()
        return redirect("wallet_profile",id=transaction.id)
    else:
        form=forms.TransactionForm(instance=transaction)
        return render(request,"Digitalwallet/edit_transaction.html",{'form':form})
    



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


def wallet_profile(request,id):
    wallet=Wallet.objects.get(id=id)
    return render(request, 'wallet/wallet_profile.html', {
        "customer": wallet})

def edit_wallet(request,id):
    wallet=Wallet.objects.get(id=id)
    request.method=="POST"
    form=forms.CustomerRegistrationForm(request.POST,instance=wallet)
    if form.is_valid():
        form.save()
        return redirect("wallet_profile",id=wallet.id)
    else:
        form=forms.CustomerRegistrationForm(instance=wallet)
        return render(request,"Digitalwallet/edit_wallet.html",{'form':form})
    


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
def list_loans(request):
    loan=Loan.objects.all()
    return render(request, 'wallet/list_loan.html', {
        "loans": loan})
def loan_profile(request,id):
    loan=Loan.objects.get(id=id)
    return render(request, 'wallet/loan_profile.html', {
        "loans": loan})

def edit_loan(request,id):
    loan=Loan.objects.get(id=id)
    request.method=="POST"
    form=forms.LoanForm(request.POST,instance=loan)
    if form.is_valid():
        form.save()
        return redirect("wallet_profile",id=loan.id)
    else:
        form=forms.LoanForm(instance=loan)
        return render(request,"Digitalwallet/edit_loan.html",{'form':form})