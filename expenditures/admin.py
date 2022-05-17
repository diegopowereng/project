from django.contrib import admin
from .models import Expenditure

class ExpenditureAdmin(admin.ModelAdmin):
    #list_display    = ['created_at', 'is_active', 'payment', 'expenditure_type', 'obs', 'amount']
    #readonly_fields = ('created_at', )
    pass

admin.site.register(Expenditure, ExpenditureAdmin)