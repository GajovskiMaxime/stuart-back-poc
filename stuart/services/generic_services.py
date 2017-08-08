from flask import current_app
from sqlalchemy.exc import OperationalError, IntegrityError

from stuart.database.database import get_session
from stuart.exceptions.dao_exception import DAOException
from stuart.exceptions.database.database_locked_exception import LockedDatabaseException
from stuart.exceptions.database.unique_constraint_exception import UniqueConstraintException


class GenericService(object):

    def __init__(self, dao, verifier):
        self._dao = dao
        self._verifier = verifier

    @property
    def dao(self):
        return self._dao

    def create(self, args):
        session = get_session()
        try:
            verified_args = self._verifier.verify(
                session=session,
                args=args)
            response = self._dao.create(
                session=session,
                args=verified_args)

            session.commit()

            current_app.logger.info(
                "Object {} with id {} created successfully."
                .format(self._dao.table, response.id))

        except IntegrityError:
            session.rollback()
            err = UniqueConstraintException(
                action='create',
                table=self._dao.table)
            current_app.logger.error(str(err.serialize))
            raise err
        # except OperationalError:
        #     session.rollback()
        #     err = LockedDatabaseException(
        #         action='create',
        #         table=self._dao.table)
        #     current_app.logger.error(err.serialize)
        #     raise err
        finally:
            session.close()
        return response

    def read(self, filters):
        session = get_session()
        try:
            response = self._dao.read(
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
