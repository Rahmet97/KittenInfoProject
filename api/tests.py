import pytest

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from faker import Faker

from .models import Kitten, Breed

fake = Faker()

@pytest.fixture
def user(db):
    """Create a test user."""
    user = get_user_model().objects.create_user(
        username=fake.user_name(),
        password='testpassword'
    )
    return user

@pytest.fixture
def authenticated_client(user):
    """Create an authenticated client using JWT."""
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client


@pytest.fixture
def breed(db):
    """Create a test breed."""
    return Breed.objects.create(name=fake.word())

@pytest.fixture
def kitten(db, breed, user):
    """Create a test kitten."""
    return Kitten.objects.create(
        color=fake.color_name(),
        age=fake.random_int(min=1, max=12),
        description=fake.text(),
        breed=breed,
        user=user
    )

@pytest.mark.django_db
class TestKittenAPI:
    def test_get_kittens(self, authenticated_client):
        """Test retrieving the list of kittens."""
        response = authenticated_client.get(reverse('kitten-list'))
        assert response.status_code == status.HTTP_200_OK

    def test_get_kitten_detail(self, authenticated_client, kitten):
        """Test retrieving details of a specific kitten."""
        response = authenticated_client.get(reverse('kitten-detail', args=[kitten.id]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['color'] == kitten.color

    def test_create_kitten(self, authenticated_client, breed):
        """Test creating a new kitten."""
        data = {
            'color': fake.color_name(),
            'age': fake.random_int(min=1, max=12),
            'description': fake.text(),
            'breed_id': breed.id
        }
        response = authenticated_client.post(reverse('kitten-list'), data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Kitten.objects.count() == 1
        assert Kitten.objects.get().color == data['color']

    def test_update_kitten(self, authenticated_client, kitten):
        """Test updating an existing kitten."""
        data = {
            'color': fake.color_name(),
            'age': kitten.age,
            'description': kitten.description,
            'breed_id': kitten.breed.id
        }
        response = authenticated_client.put(reverse('kitten-detail', args=[kitten.id]), data)
        assert response.status_code == status.HTTP_200_OK
        kitten.refresh_from_db()
        assert kitten.color == data['color']

    def test_delete_kitten(self, authenticated_client, kitten):
        """Test deleting a kitten."""
        response = authenticated_client.delete(reverse('kitten-detail', args=[kitten.id]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Kitten.objects.count() == 0

    def test_get_breeds(self, authenticated_client):
        """Test retrieving the list of breeds."""
        response = authenticated_client.get(reverse('breed-list'))
        assert response.status_code == status.HTTP_200_OK

    def test_get_kittens_by_breed(self, authenticated_client, breed):
        """Test retrieving kittens by breed."""
        response = authenticated_client.get(reverse('kitten-list'), {'breed': breed.id})
        assert response.status_code == status.HTTP_200_OK

    def test_user_can_only_modify_own_kittens(self, authenticated_client, kitten):
        """Test that users can only modify their own kittens."""
        new_user = get_user_model().objects.create_user(username=fake.user_name(), password='password')
        kitten.user = new_user
        kitten.save()

        response = authenticated_client.put(reverse('kitten-detail', args=[kitten.id]), {
            'color': 'Orange',
            'age': 2,
            'description': 'This update should fail',
            'breed_id': kitten.breed.id
        })
        assert response.status_code == status.HTTP_403_FORBIDDEN
