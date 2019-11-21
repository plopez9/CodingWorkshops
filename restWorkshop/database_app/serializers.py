from rest_framework import serializers
from .models import Fires

class BrazilFires(serializers.ModelSerializer):
    class Meta:
        model = Fires
        fields =("year", "state", "month", "number", "date")

        read_only_fields = [f.name for f in Fires._meta.get_fields()]
