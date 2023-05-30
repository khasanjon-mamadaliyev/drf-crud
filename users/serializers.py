from rest_framework.serializers import ModelSerializer

from users.models import Member


class MemberModelSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
