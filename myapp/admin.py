from django.contrib import admin

# Register your models here.
from .models import Ticket, KycDetails,Dash,Wallet,Watchlist,Images

admin.site.register(Ticket)
admin.site.register(KycDetails)
admin.site.register(Dash)
admin.site.register(Wallet)
admin.site.register(Watchlist)
admin.site.register(Images)
