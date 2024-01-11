from rest_framework import serializers
from .models import HintExplanation

class HintExplanationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HintExplanation
        fields = '__all__'