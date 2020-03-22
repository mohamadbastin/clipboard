from rest_framework import serializers

from apiv1.models import Text


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'


class EmptySerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = []
