from decimal import Decimal
from pickle import NONE
from .models import Expenditure
from.serializers import ExpenditureSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Sum


from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict, defaultdict

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def customHandler1(self, company_id=None):
        array_status = []
        #for a in LogData.objects.filter(company__id=company_id).values_list('date', flat=True):
        #    array_status.append(a) 
        return list(set(array_status))

    def customHandler2(self, company_id=None):
        array_document = []
        #for a in LogData.objects.filter(company__id=company_id).values_list('document','document__document_type__name', 'document__employee__name', 'document__company__name'):
        #    if a[0] != None:
        #        array_document.append(a) 
        return list(set(array_document))

    def SumSolution(self, data):
        if data:
            result = 0
            for od in data:
                result += Decimal(od['amount'])
            return result
        return 0

    def get_paginated_response(self, data):
        aux_data = None
        if len(data) > 0:
            aux_data = data
        return Response({
             'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
             },
             'count': self.page.paginator.count,
             'results': data,
             "all_dates": self.customHandler1(aux_data),
             "all_docs": self.customHandler2(aux_data),
             "sum": self.SumSolution(aux_data),

         })



class ExpendituresViewSet(ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer
    filterset_fields = ['created_at', 'payment', 'expenditure_type']
    search_fields = ['obs']
    pagination_class = LargeResultsSetPagination


    def get_queryset(self):
        queryset = super(ExpendituresViewSet, self).get_queryset()

        start = self.request.query_params.get('start', None)
        end = self.request.query_params.get('end', None)
        if start is not None and start != "":
            queryset = queryset.filter(created_at__range=(start, end)).order_by('-created_at')
        else:
            queryset = queryset.order_by('-created_at')
        return queryset



from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView





class ExpenditureList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'expenditures/listar_despesas.html'

    def get(self, request):
            queryset = Expenditure.objects.all()
            soma = str(round(Expenditure.objects.aggregate(Sum('amount'))['amount__sum'], 2))
            '''
            created_at = self.request.query_params.get('created_at')
            is_active = self.request.query_params.get('is_active')
            payment = self.request.query_params.get('payment')
            expenditure_type = self.request.query_params.get('expenditure_type')
            obs = self.request.query_params.get('obs')
            amount = self.request.query_params.get('amount')
            if created_at:
                queryset = queryset.filter(created_at=created_at)
            elif is_active:
                queryset = queryset.filter(is_active=is_active)
            elif payment:
                queryset = queryset.filter(payment=payment)
            elif expenditure_type:
                queryset = queryset.filter(expenditure_type=expenditure_type)
            elif obs:
                queryset = queryset.filter(obs=obs)
            elif amount:
                queryset = queryset.filter(amount=amount)
            '''
            return Response({'despesas': queryset, 'soma': soma})
