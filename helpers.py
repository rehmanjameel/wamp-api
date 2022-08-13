import inspect

from autobahn.wamp import ApplicationError
from marshmallow import ValidationError


def validate_call_params(serializer_class, session):
    validator = serializer_class()

    def _type_check(func):
        def _type_check(*args, **kwargs):
            arguments = inspect.getcallargs(func, *args, **kwargs)
            arguments.pop('self', None)
            arguments.pop('details', None)

            try:
                validator.validate(arguments, session=session)
            except ValidationError as e:
                raise ApplicationError('com.thing.system.error.validation_error', e)

            return func(*args, **kwargs)

        return _type_check

    return _type_check
