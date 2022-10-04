from django.urls import path
# from .views import account_form, card_form, list_customers, loan_form, notification_form, receipt_form, register_customer, reward_form, thirdparty_form, transaction_form, wallet_form
from .import views
urlpatterns = [
    path("register/",views.register_customer,name="registration"),
    path("account/",views.account_form,name="account"),
    path("card/",views.card_form,name="card"),
    path("notification/",views.notification_form,name="notification"),
    path("receipt/",views.receipt_form,name="receipt"),
    path("reward/",views.reward_form,name="reward"),
    path("thirdparty/",views.thirdparty_form,name="thirdparty"),
    path("transaction/",views.transaction_form,name="transaction"),
    path("wallet/",views.wallet_form,name="wallet"),
    path("loan/",views. loan_form,name="loan"),
    path("customers/",views.list_customers,name="customer_list"),
    path("accounts/",views.list_accounts,name="account_list"),
    path("cards/",views.list_cards,name="card_list"),
    path("notifications/",views.list_notifications,name="notification_list"),
    path("receipts/",views.list_receipt,name="receipt_list"),
    path("rewards/",views.list_reward,name="reward_list"),
    path("thirdpartys/",views.list_thirdparty,name="thirdparty_list"),
    path("transactions/",views.list_transaction,name="transaction_list"),
    path("wallets/",views.list_wallet,name="wallet_list"),
    path("loans/",views.list_loans,name="loans_list"),
    path("customers/<int:id>/",views.customer_profile,name="customer_profile"),
    path("customers/<int:id>/",views.edit_customer_profile,name="edit_customer_profile"),
    path("walletss/<int:id>/",views.edit_wallet,name="edit_wallet"),
    path("walletss/<int:id>/",views.customer_profile,name="customer_profile"),
    path("accountss/<int:id>/",views.account_profile,name="account_profile"),
    path("accountss/<int:id>/",views.edit_profile,name="edit_profile"),
    path("notification/<int:id>/",views.notification_profile,name="notification_profile"),
    path("notification/<int:id>/",views.edit_notification,name="edit_notification"),
    

]
