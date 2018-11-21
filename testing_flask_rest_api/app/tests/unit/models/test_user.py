try:
    from models.user import UserModel
    from tests.base_test import BaseTest
except ModuleNotFoundError:
    from testing_flask_rest_api.app.models.user import UserModel
    from testing_flask_rest_api.app.tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test',
                         "The name of the user after creation does not equal the constructor argument.")
        self.assertEqual(user.password, 'abcd',
                         "The password of the user after creation does not equal the constructor argument.")
