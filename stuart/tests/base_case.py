from unittest import TestCase

from manage import recreate_database
from stuart import create_app


class BaseTestCase(TestCase):

    app = create_app()

    def create_app(self):
        self.app.config.from_object('stuart.config.DevelopmentConfig')
        return self.app

    def setUp(self):
        recreate_database()
