from flask import current_app, json

from stuart.exceptions.attribute.attribute_exception import AttributeException
from stuart.exceptions.attribute.attribute_not_found_exception import AttributeNotFoundException
from stuart.exceptions.attribute.empty_attribute_exception import EmptyAttributeException
from stuart.exceptions.attribute.unexpected_attribute_exception import UnexpectedAttributeException
from stuart.models.module import Module
from stuart.services.module_services import ModuleService
from stuart.tests.base_case import BaseTestCase


class TestModuleService(BaseTestCase):

    _service = ModuleService()
    #
    # def test_read_by_id_service_with_bad_id_format(self):
    #
    #     client = self.create_app().test_client()
    #
    #     expected_message = "On table module, attribute 'id'" \
    #                        " with value {} must be an integer."
    #
    #     bad_format_id = 'test'
    #
    #     with client:
    #         response = client.get('/modules/' + bad_format_id)
    #         data = json.loads(response.data.decode())
    #         current_app.logger.info(data)
    #         self.assertEqual(response.status_code, 400)
    #         self.assertTrue('datetime' in data)
    #         self.assertEqual(data['data']['attribute_value'], bad_format_id)
    #         self.assertEqual(
    #             data['data']['message'],
    #             expected_message.format(data['data']['attribute_value']))
    #
    # def test_create_with_dict_service_on_nominal_case(self):
    #
    #     module_dict = {'label': 'label', 'command': 'command'}
    #
    #     module_from_create_method = self._service.\
    #         create_with_dict(args=module_dict)
    #
    #     module_from_read_method = self._service.\
    #         read_by_id(module_from_create_method.id)
    #     current_app.logger.error(module_from_create_method)
    #     current_app.logger.error(module_from_read_method)
    #     self.assertTrue(module_from_create_method == module_from_read_method)
    #
    # def test_create_with_dict_service_with_extra_fields(self):
    #
    #     module_dict = {'command': 'command', 'label': 'label', 'test': 'test'}
    #
    #     self.assertRaises(
    #         UnexpectedAttributeException,
    #         self._service.create_with_dict,
    #         args=module_dict)
    #

    def test_create_with_dict_service_with_empty_field_on_label(self):

        module_dict = {'command': 'command', 'label': ''}

        self.assertRaises(
            EmptyAttributeException,
            self._service.create_with_dict,
            args=module_dict)

    def test_create_with_dict_service_without_all_mandatory_fields(self):

        module_dict = {'command': 'command'}

        self.assertRaises(
            AttributeNotFoundException,
            self._service.create_with_dict,
            args=module_dict)

    def test_read_by_id_service_on_nominal_case(self):

        module_dict = {'command': 'command', 'label': 'label'}

        inserted_module = self._service.\
            create_with_dict(args=module_dict)

        module_from_get = self._service.\
            read_by_id(object_id=inserted_module.id)

        self.assertTrue(inserted_module == module_from_get)
