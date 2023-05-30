from django.urls import path

from users.views import MemberCreateListAPIView, MemberRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('<int:pk>', MemberRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
    path('member', MemberCreateListAPIView.as_view(), name='member'),
]
