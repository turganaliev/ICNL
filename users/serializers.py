from rest_framework import serializers
from .models import User, Code


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id phone'.split()


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = 'id conf_code'.split()
