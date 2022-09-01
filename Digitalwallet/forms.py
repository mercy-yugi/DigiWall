from dataclasses import fields
from django.forms import ModelForm
from .models import Account, Card, Customer, Loan, Notifications, Receipt, Reward, ThirdParty, Transaction, Wallet

class CustomerRegistrationForm(ModelForm):
    class Meta:
        model = Customer
        fields="__all__"
class RewardForm(ModelForm):
    class Meta:
        model = Reward
        fields="__all__"
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields="__all__"
class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields="__all__"
class CardForm(ModelForm):
    class Meta:
        model = Card
        fields="__all__"
class ThirdpartyForm(ModelForm):
    class Meta:
        model = ThirdParty
        fields="__all__"
class NotificationForm(ModelForm):
    class Meta:
        model = Notifications
        fields="__all__"
class WalletForm(ModelForm):
    class Meta:
        model = Wallet
        fields="__all__"
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields="__all__"
class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields="__all__"

