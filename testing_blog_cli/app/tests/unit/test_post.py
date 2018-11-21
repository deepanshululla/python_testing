from unittest import TestCase

from testing_blog_cli.app.post import Post

class PostTest(TestCase):
    def test_create_post(self):
        # why is this test useful
        # Any future changes to the class signature
        # will fail this test if we are using
        p=Post('title1','content1')
        self.assertEqual('title1',p.title)
        self.assertEqual('content1', p.content)

    def test_json(self):
        p = Post('title1', 'content1')
        expected={
            'title': 'title1',
            'content': 'content1',
        }
        self.assertDictEqual(p.json(),expected)