
from manage import recreate_database
from stuart import create_app
from stuart.services.action_services import ActionService
from stuart.services.module_services import ModuleService
from stuart.tests.base_case import BaseTestCase


class TestActionReadRoutes(BaseTestCase):

    client = create_app().test_client()

    def setUp(self):
        recreate_database()
        nominal_module_dict = {'label': 'test', 'command': 'command'}
        new_module = ModuleService().create(args=nominal_module_dict)
        action_dict = {'module_id': new_module.id, 'label': 'test', 'command': 'test'}
        ActionService().create(args=action_dict)

    def test_read_module_by_id_on_nominal_case(self):
        """
            :case: Nominal case.
            :method: GET
            :path: http://localhost:port/modules/<module_id>/
            :module_id:1
            :expected_status:200
        """
        with self.client:
            response = self.client.get('/modules/1/')
            self.assertEqual(response.status_code, 200)

    def test_read_module_with_bad_format_id(self):
        """
            :case: Bad format for module_id
            :method: GET
            :path: http://localhost:port/modules/<module_id>/
            :module_id:test (err, needed to be an integer)
            :expected_status:404
        """
        with self.client:
            response = self.client.get('/modules/test/')
            self.assertEqual(response.status_code, 404)

    def test_read_module_with_one_query_param(self):
        """
            :case: Search with one query param (search : (label,test))
            :method: GET
            :path: http://localhost:port/modules/?label=test
            :query_params:(label,test)
            :expected_status:200
        """
        with self.client:
            response = self.client.get('/modules/?label=test')
            self.assertEqual(response.status_code, 200)

    def test_read_module_with_several_query_param(self):
        """
            :case: Search with several query params (search : (label,test), (id,1))
            :method: GET
            :path: http://localhost:port/modules/?label=test&id=1
            :query_params:(label,test), (id,1)
            :expected_status:200
        """
        with self.client:
            response = self.client.get('/modules/?label=test&id=1')
            self.assertEqual(response.status_code, 200)

    def test_read_module_with_unexpected_key_on_query_param(self):
        """
            :case: Search with unexpected key filter (search : (test,test))
            :method: GET
            :path: http://localhost:port/modules/?test=test
            :query_params:(test,test)
            :expected_status:404
        """
        with self.client:
            response = self.client.get('/modules/?test=test')
            self.assertEqual(response.status_code, 404)
