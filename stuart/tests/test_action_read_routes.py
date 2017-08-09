
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
        new_module = ModuleService().create(args=nominal_module_dict, autocommit=True)
        action_dict = {'module_id': new_module.id, 'label': 'test', 'command': 'test'}
        ActionService().create(args=action_dict, autocommit=True)

    def test_read_action_by_id_on_nominal_case(self):
        """
            :case: Nominal case. (action belongs to module)
            :method: GET
            :path: http://localhost:port/modules/<module_id>/actions/<action_id>/
            :module_id:1
            :action_id:1
            :expected_status:200
        """
        with self.client:
            response = self.client.get('/modules/1/actions/1/')
            self.assertEqual(response.status_code, 200)

    def test_read_action_by_id_who_does_not_belongs_to_module(self):
        """
            :case: Action does not belong to module
            :method: GET
            :path: http://localhost:port/modules/<module_id>/actions/<action_id>/
            :module_id:1
            :action_id:2 (err, action.module_id = 1)
            :expected_status:404
        """
        with self.client:
            response = self.client.get('/modules/1/actions/2/')
            self.assertEqual(response.status_code, 404)

    def test_read_action_with_bad_format_into_module_id(self):
        """
            :case: Bad format for module_id
            :method: GET
            :path: http://localhost:port/modules/<module_id>/actions/<action_id>/
            :module_id:test (err, needed to be an integer)
            :action_id:1
            :expected_status:404
        """
        with self.client:
            response = self.client.get('/modules/test/actions/1/')
            self.assertEqual(response.status_code, 404)

    def test_read_action_with_bad_format_action_id(self):
        """
            :case: Bad format for action_id
            :method: GET
            :path: http://localhost:port/modules/<module_id>/actions/<action_id>/
            :module_id:1
            :action_id:test (err, needed to be an integer)
            :expected_status:404
        """
        with self.client:
            response = self.client.get('/modules/1/actions/test/')
            self.assertEqual(response.status_code, 404)

    def test_read_action_with_one_query_param(self):
        """
            :case: Search with one query param (search : (label,test))
            :method: GET
            :path: http://localhost:port/modules/<module_id>/actions/<action_id>/?label=test
            :module_id:1
            :action_id:1
            :filters:(label,test)
            :expected_status:200
        """
        with self.client:
            response = self.client.get('/modules/1/actions/1/?label=test')
            self.assertEqual(response.status_code, 200)

    def test_read_action_with_query_params(self):
        """
            :case: Search with query params (search : (label,test), (id,1))
            :method: GET
            :path: http://localhost:port/modules/<module_id>/actions/?label=test&id=1
            :module_id:1
            :query_params:(label,test), (id,1)
            :expected_status:200
        """
        with self.client:
            response = self.client.get('/modules/1/actions/?label=test&id=1')
            self.assertEqual(response.status_code, 200)

    def test_read_action_with_unexpected_key_on_query_param(self):
        """
            :case: Search with unexpected key filter (search : (test,test))
            :method: GET
            :path: http://localhost:port/modules/<module_id>/actions/?test=test
            :module_id:1
            :query_params:(test,test)
            :expected_status:400
        """
        with self.client:
            response = self.client.get('/modules/1/actions/?test=test')
            self.assertEqual(response.status_code, 404)
    #
    # def test_read_action_when_nothing_on_database(self):
    #     """
    #         :case: Nothing on table action
    #         :method: GET
    #         :path: http://localhost:port/modules/<module_id>/actions/
    #         :module_id:1
    #         :expected_status:204
    #     """
    #     with self.client:
    #         self.client.delete('/modules/1/actions/1/')
    #         response = self.client.get('/modules/1/actions/')
    #         self.assertEqual(response.status_code, 204)
