from rest_framework.serializers import ModelSerializer
from .models import Expenditure



class ExpenditureSerializer(ModelSerializer):
    class Meta:
        model = Expenditure
        fields = ['id', 'created_at', 'scheduled', 'payment', 'expenditure_type', 'obs', 'amount', 'receipt', 'scheduled_date', 'responsible']

    def create(self, validated_data):
        despesa = Expenditure.objects.create(**validated_data)
        print(despesa)
        print('SEND DEFAULT EMAIL')
        return despesa


class DisableCSRFMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response
