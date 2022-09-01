from django.urls import path
from .views import account_form, card_form, loan_form, notification_form, receipt_form, register_customer, reward_form, thirdparty_form, transaction_form, wallet_form

urlpatterns = [
    path("register/",register_customer,name="registration"),
    path("account/",account_form,name="account"),
    path("card/",card_form,name="card"),
    path("notification/",notification_form,name="notification"),
    path("receipt/",receipt_form,name="receipt"),
    path("reward/",reward_form,name="reward"),
    path("thirdparty/",thirdparty_form,name="thirdparty"),
    path("transaction/",transaction_form,name="transaction"),
    path("wallet/",wallet_form,name="wallet"),
    path("loan/",loan_form,name="loan"),

]
