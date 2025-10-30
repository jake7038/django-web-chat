import pytest
from blog.factories import PostFactory

@pytest.fixture
def post_publisher():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(post_publisher):
    assert post_publisher.title == 'pytest with factory'