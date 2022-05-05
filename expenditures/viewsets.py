from .models import Expenditure
from.serializers import ExpenditureSerializer
from rest_framework.viewsets import ModelViewSet



class ExpendituresViewSet(ModelViewSet):
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer