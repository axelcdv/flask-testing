from project.base import BaseTestCase
from . import factories


class CoreViewsTestCase(BaseTestCase):
    def test_post_list(self):
        post = factories.PostFactory()

        response = self.client.get('/')
        assert response.status_code == 200
        assert post.title in response.data.decode('utf-8')
