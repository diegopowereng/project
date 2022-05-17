from rest_framework.serializers import ModelSerializer
from .models import Expenditure



class ExpenditureSerializer(ModelSerializer):
    class Meta:
        model = Expenditure
        fields = ['id', 'created_at', 'scheduled', 'payment', 'expenditure_type', 'obs', 'amount', 'receipt', 'scheduled_date']