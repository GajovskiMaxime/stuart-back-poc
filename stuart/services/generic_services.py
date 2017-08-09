from flask import current_app
from sqlalchemy.exc import OperationalError, IntegrityError

from stuart.database.database import get_session
from stuart.exceptions.dao_exception import DAOException
from stuart.exceptions.database.database_locked_exception import LockedDatabaseException
from stuart.exceptions.database.object_not_found_exception import ObjectNotFoundException
from stuart.exceptions.database.unique_constraint_exception import UniqueConstraintException


class GenericService(object):

    def __init__(self, dao, verifier):
        self._dao = dao
        self._verifier = verifier

    @property
    def dao(self):
        return self._dao

    def create(self, args, autocommit):
        response = None
        session = get_session()
        try:
            response = self.create_with_recursion(
                args=args,
                session=session,
                autocommit=autocommit)

            if autocommit is False:
                session.commit()
                current_app.logger.info(
                    "Objects from session committed successfully.")

        except IntegrityError:
            session.rollback()

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

    def create_with_recursion(self, args, session, autocommit):

        # try:

        verified_args = self._verifier.verify(
            autocommit=autocommit,
            session=session,
            args=args)

        try:
            object_already_exists = self._dao.read(
                session=session,
                filters=verified_args,
                mode='exact')

            err = UniqueConstraintException(
                action='create',
                object_id=object_already_exists[0].id,
                table=self._dao.table)
            current_app.logger.warning(str(err.serialize))
            raise err
        except ObjectNotFoundException:
            pass

        response = self._dao.create(
            session=session,
            args=verified_args)

        if autocommit:
            session.commit()
            current_app.logger.info(
                "Object {} with id '{}' created successfully."
                .format(self._dao.table.table_name(), response.id))
        else:
            current_app.logger.info(
                "Object {} with id {} added to session successfully."
                .format(self._dao.table.table_name(), response.id))
        # except DatabaseException:
        #     raise

        return response

    def read(self, filters, mode):
        session = get_session()
        try:
            response = self._dao.read(
                session=session,
                filters=filters,
                mode=mode)
            return response
        except DAOException as err:
            raise err
        finally:
            session.close()

    def delete(self, mode, filters):
        session = get_session()
        try:
            response = self._dao.delete(
                session=session,
                filters=filters,
                mode=mode)
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
