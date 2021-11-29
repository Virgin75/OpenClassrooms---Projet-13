import pytest

from django.urls import reverse
from .models import Profile


@pytest.mark.django_db
def test_profiles_index(client):
    url = reverse('profiles:index')
    response = client.get(url)

    html_content = str(response.content)
    h1_tag = html_content.split('<h1>', 1)[1].split('</h1>', 1)[0]

    assert 'Profiles' in h1_tag
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view(client, django_user_model):
    user = django_user_model.objects.create(
        username='someone', password='password'
    )
    profile = Profile.objects.create(favorite_city='Bordeaux', user=user)

    url = reverse('profiles:profile', kwargs={'username': profile.user.username})
    response = client.get(url)

    html_content = str(response.content)
    h1_tag = html_content.split('<h1>', 1)[1].split('</h1>', 1)[0]

    assert profile.user.username in h1_tag
    assert response.status_code == 200
