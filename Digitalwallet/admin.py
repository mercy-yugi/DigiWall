from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notifications, Receipt, Reward, ThirdParty, Transaction, Wallet

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age','email',)
    search_fields = ('first_name', 'last_name',)
admin.site.register(Customer, CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('balance','amount','time','status')
    search_fields = ('balance','amount','time')
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=('account_name','account_type','balance',Wallet)
    search_fields=('account_name','account_type','balance')
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=('transaction_code','transaction_type','transaction_fee','transaction_time')
    search_fields=('transaction_code','transaction_type','transaction_fee')
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):   
    list_display=('card_name','card_type','card_number','card_issuer')
    search_fields=('card_name','card_type','card_number')
admin.site.register(Card,CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin): 
    list_display=('party_name','party_id','phone_number',Account)
    search_fields=('party_name','party_id','phone_number')
admin.site.register(ThirdParty,ThirdPartyAdmin)

class NotificationsAdmin(admin.ModelAdmin):
    list_display=('customer_name','notification_status','notification_date_time','recipient')
    search_fields=('customer_name','notification_status','notification_date_time')
admin.site.register(Notifications,NotificationsAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display=('receipt_type','receipt_date','receipt_file','total_amount')
    search_fields=('receipt_type','receipt_date','receipt_file')
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=('loan_type','loan_date','loan_amount','loan_number','loan_term')
    search_fields=('loan_type','loan_date','loan_amount')
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=('gender','reward_date','reward_points',Transaction)
    search_fields=('reward_date','reward_points','gender')
admin.site.register(Reward,RewardAdmin)