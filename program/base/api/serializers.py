from rest_framework.serializers import ModelSerializer
from base.models import User
from base.models import Data
from base.models import Medicine


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'


class MedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class DataweightSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = ['weight']


class DatatemperatureSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = ['temperature']


class DatapressuresSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = ['pressures']


class DatapressuredSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = ['pressured']


class DataheartbeatSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = ['heartbeat']

