from project.base import BaseTestCase
from . import factories


class PostsViewsTestCase(BaseTestCase):
    def test_post_list(self):
        post = factories.PostFactory()

        response = self.client.get('/posts')
        assert response.status_code == 200
        assert post.title in response.data.decode('utf-8')

    def test_post_detail(self):
        post = factories.PostFactory()
        self.db.session.add(post)
        self.db.session.commit()

        response = self.client.get(f'/posts/{post.id}')
        assert response.status_code == 200
        assert post.body in response.data.decode('utf-8')


class AuthorsViewsTestCase(BaseTestCase):
    def test_author_list(self):
        author = factories.AuthorFactory()

        response = self.client.get('/authors')
        assert response.status_code == 200
        assert author.first_name in response.data.decode('utf-8')
