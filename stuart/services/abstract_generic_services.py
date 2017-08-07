from sqlalchemy.exc import OperationalError

from stuart.database.database import get_session
from stuart.exceptions.attribute.attribute_exception import AttributeException
from stuart.exceptions.dao_exception import DAOException
from stuart.exceptions.database.database_locked_exception import LockedDatabaseException


class AbstractGenericService(object):

    def __init__(self, dao, verifier):
        self._dao = dao
        self._verifier = verifier

    @property
    def dao(self):
        return self._dao

    def create_with_dict(self, args):
        session = get_session()
        try:
            lol = self._verifier.verify_args(**args)
            table = self._dao.table
            model = table(**lol)
            response = self._dao.create(
                session=session,
                model=model)
            session.commit()
        except OperationalError:
            raise LockedDatabaseException(
                action='create',
                table=self._dao.table)
        except AttributeException:
            session.rollback()
            raise
        finally:
            session.close()
        return response

    def read_all(self, filters):
        session = get_session()
        try:
            response = self._dao.read_all(
                session=session,
                filters=filters)
            return response
        except DAOException as err:
            raise err
        finally:
            session.close()

    def delete(self, filters):
        session = get_session()
        try:
            response = self._dao.delete(
                session=session,
                filters=filters)
            session.commit()
        except OperationalError:
            session.rollback()
            raise LockedDatabaseException(
                action='delete',
                table=self._dao.table)
        except DAOException as err:
            session.rollback()
            raise err
        finally:
            session.close()
        return response
