try:
    from models.store import StoreModel
    from tests.base_test import BaseTest
except ModuleNotFoundError:
    from testing_flask_rest_api.app.models.store import StoreModel
    from testing_flask_rest_api.app.tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store(self):
        store = StoreModel('test')

        self.assertEqual(store.name, 'test',
                         "The name of the store after creation does not equal the constructor argument.")
