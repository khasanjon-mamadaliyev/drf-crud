from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.models import Member
from users.serializers import MemberModelSerializer


class MemberCreateListAPIView(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberModelSerializer


class MemberRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberModelSerializer
