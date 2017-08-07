from flask import current_app

from stuart.database.database import get_session
from stuart.exceptions.attribute.attribute_exception import AttributeException
from stuart.exceptions.dao_exception import DAOException
from stuart.exceptions.format.id_is_not_an_integer_exception import IdIsNotAnIntegerException


class AbstractGenericService(object):

    def __init__(self, dao, verifier):
        self._dao = dao
        self._verifier = verifier

    @property
    def dao(self):
        return self._dao

    def create_with_dict(self, args):
        return AbstractGenericService.__create_with_dict(
            dao=self._dao,
            verifier=self._verifier,
            **args)

    def read_by_id(self, object_id):
        return AbstractGenericService.__read_by_id(
            dao=self._dao,
            object_id=object_id)

    # TODO : Add verifier model
    @staticmethod
    def __create_with_model(dao, verifier, model):

        session = get_session()
        try:
            response = dao.create(
                session=session,
                model=model)
            session.commit()

        except AttributeException:
            session.rollback()
            current_app.logger.info("coucou")
            raise
        finally:
            session.close()
        return response

    @staticmethod
    def __create_with_dict(dao, verifier, **args):

        session = get_session()
        response = None
        try:
            lol = verifier.verify_args(**args)
            table = dao.table
            current_app.logger.info(args)
            model = table(**lol)
            response = dao.create(
                session=session,
                model=model)
            session.commit()

        except AttributeException:
            session.rollback()
            current_app.logger.info("coucou")
            raise
        finally:
            session.close()
        return response

    @staticmethod
    def __read_by_id(dao, object_id):
        session = get_session()
        try:
            response = dao.read_by_id(
                session=session,
                object_id=int(object_id))

        except DAOException as dao_exception:
            raise dao_exception
        except ValueError:
            raise IdIsNotAnIntegerException(
                table=dao.table,
                attribute_value=object_id)
        finally:
            session.close()
        return response
