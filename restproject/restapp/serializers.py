from restapp.models import UserModel
from rest_framework.validators import UniqueValidator

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','programming_lang')