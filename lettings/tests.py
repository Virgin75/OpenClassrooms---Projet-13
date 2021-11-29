import pytest

from django.urls import reverse
from .models import Letting, Address


@pytest.mark.django_db
def test_letings_index(client):
    url = reverse('lettings:index')
    response = client.get(url)

    html_content = str(response.content)
    h1_tag = html_content.split('<h1>', 1)[1].split('</h1>', 1)[0]

    assert 'Lettings' in h1_tag
    assert response.status_code == 200


@pytest.mark.django_db
def test_letings_view(client):
    address = Address.objects.create(number=21, street='Rue du Gonfe', city='Paris',
                                     state='IDF', zip_code=75001, country_iso_code='FRA')
    letting = Letting.objects.create(title='Nouvelle Location Bordeaux', address=address)

    url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(url)

    html_content = str(response.content)
    h1_tag = html_content.split('<h1>', 1)[1].split('</h1>', 1)[0]

    assert letting.title in h1_tag
    assert response.status_code == 200
