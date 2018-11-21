from unittest import TestCase
from testing_blog_cli.app.blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b=Blog('Test','author')
        self.assertEqual(b.title,'Test')
        self.assertEqual(b.author,'author')
        self.assertEqual(0, len(b.posts))
        self.assertListEqual([], b.posts)

    def test_json_no_posts(self):
        b = Blog('Test', 'Test author')
        self.assertDictEqual(b.json(), {
            'title': b.title,
            'author': b.author,
            'posts': [],
        })
