
from manage import recreate_database
from stuart import create_app
from stuart.services.action_services import ActionService
from stuart.services.module_services import ModuleService
from stuart.tests.base_case import BaseTestCase


class TestActionDeleteRoutes(BaseTestCase):

    client = create_app().test_client()

    def setUp(self):
        recreate_database()
        nominal_module_dict = {'label': 'test', 'command': 'command'}
        new_module = ModuleService().create(args=nominal_module_dict)
        action_dict = {'module_id': new_module.id, 'label': 'test', 'command': 'test'}
        ActionService().create(args=action_dict)

    def test_delete_action_on_nominal_case(self):
        """
            :case: Nominal case. (action belongs to module)
            :method: GET
            :path: http://localhost:port/modules/<module_id>/actions/<action_id>/
            :module_id:1
            :action_id:1
            :expected_status:200
        """
        with self.client:
            response = self.client.delete('/modules/1/actions/1/')
            self.assertEqual(response.status_code, 200)

    def test_delete_action_who_does_not_belongs_to_module(self):
        """
            :case: Action does not belong to module
            :method: GET
            :path: http://localhost:port/modules/<module_id>/actions/<action_id>/
            :module_id:1
            :action_id:2 (err, action.module_id = 1)
            :expected_status:404
        """
        with self.client:
            response = self.client.delete('/modules/1/actions/2/')
            self.assertEqual(response.status_code, 404)

    def test_delete_action_with_bad_format_into_module_id(self):
        """
            :case: Bad format for module_id
            :method: GET
            :path: http://localhost:port/modules/<module_id>/actions/<action_id>/
            :module_id:test (err, needed to be an integer)
            :action_id:1
            :expected_status:404
        """
        with self.client:
            response = self.client.delete('/modules/test/actions/1/')
            self.assertEqual(response.status_code, 404)

    def test_delete_action_with_bad_format_action_id(self):
        """
            :case: Bad format for action_id
            :method: GET
            :path: http://localhost:port/modules/<module_id>/actions/<action_id>/
            :module_id:1
            :action_id:test (err, needed to be an integer)
            :expected_status:404
        """
        with self.client:
            response = self.client.delete('/modules/1/actions/test/')
            self.assertEqual(response.status_code, 404)
