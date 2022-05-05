from rest_framework.serializers import ModelSerializer
from .models import Expenditure



class ExpenditureSerializer(ModelSerializer):
    class Meta:
        model = Expenditure
        fields = ['id', 'created_at', 'is_active', 'status']