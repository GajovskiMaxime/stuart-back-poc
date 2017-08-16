
from manage import recreate_database
from stuart import create_app
from stuart.services.action_services import ActionService
from stuart.services.module_services import ModuleService
from stuart.tests.base_case import BaseTestCase


class TestTaskReadRoutes(BaseTestCase):

    client = create_app().test_client()

    def setUp(self):
        recreate_database()
        nominal_module_dict = {'label': 'test', 'command': 'command'}
        new_module = ModuleService().create(args=nominal_module_dict, autocommit=True)
        action_dict = {'module': new_module.id, 'label': 'test', 'command': 'test'}
        ActionService().create(args=action_dict, autocommit=True)

    def test_read_module_by_id_on_nominal_case(self):
        """
            :case: Nominal case.
            :method: GET
            :path: http://localhost:port/modules/<module_id>/
            :module_id:1
            :expected_status:200
        """
        with self.client:
            response = self.client.post('/task_params/',)

            self.assertEqual(response.status_code, 200)
