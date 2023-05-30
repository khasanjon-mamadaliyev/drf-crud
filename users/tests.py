import pytest
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient

from users.models import Member


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def member():
    member = Member.objects.create(name="jek")
    return member


@pytest.mark.django_db
def test_create_member(api_client):
    data = {
        'name': 'jek'
    }
    url = reverse_lazy('member')
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    member = Member.objects.first()
    assert member is not None
    assert member.name == data['name']


@pytest.mark.django_db
def test_list_member(api_client):
    url = reverse_lazy('member')
    response = api_client.get(url)
    data = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert len(data) == Member.objects.count()


@pytest.mark.django_db
def test_update_member(api_client, member):
    url = reverse_lazy('detail', args=(member.pk,))
    data = {
        'name': 'salom'
    }
    response = api_client.patch(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['name'] == data['name']


@pytest.mark.django_db
def test_destroy_member(api_client, member):
    url = reverse_lazy('detail', args=(member.pk,))
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Member.objects.exists()


@pytest.mark.django_db
def test_detail_member(api_client, member):
    url = reverse_lazy('detail', args=(member.pk,))
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['name'] == member.name


