from .models import Fires
from .serializers import BrazilFires

from rest_framework import viewsets

# Create your views here.
class FireView(viewsets.ModelViewSet):
    queryset = Fires.objects.all()
    serializer_class = BrazilFires

    ## Insert Queryable Features
