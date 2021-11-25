from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'password', 'last_login', 'username', 'first_name', 'last_name', 'email', 'date_joined')


class UserModelSerializerWithStaff(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
