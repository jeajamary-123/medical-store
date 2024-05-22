from rest_framework import serializers
from medicine_store.models import med_kit

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = med_kit
        fields = '__all__'