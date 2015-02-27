from checkio_referee import RefereeBase
from checkio_referee.validators import BaseValidator, ValidationError

import settings
import settings_env
from tests import TESTS

PRECISION = 0.001


class SuperRootValidator(BaseValidator):
    def validate(self, outer_result):
        if not isinstance(outer_result, (int, float)):
            self.additional_data = "The result should be a float or an integer."
            raise ValidationError
        if abs(outer_result) > 12:
            raise ValidationError
        p = outer_result ** outer_result
        self.additional_data = p
        if abs(self._test["input"] - p) >= PRECISION:
            raise ValidationError


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "super_root"
    VALIDATOR = SuperRootValidator
