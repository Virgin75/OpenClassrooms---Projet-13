import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_main_index(client):
    url = reverse('index')
    response = client.get(url)

    html_content = str(response.content)
    h1_tag = html_content.split('<h1>', 1)[1].split('</h1>', 1)[0]

    assert 'Welcome to Holiday Homes' in h1_tag
    assert response.status_code == 200
