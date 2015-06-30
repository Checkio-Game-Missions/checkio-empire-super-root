from checkio_referee import RefereeBase
from checkio_referee import validators, ENV_NAME


import settings_env
from tests import TESTS

PRECISION = 0.001

Result = validators.ValidatorResult


class SuperRootValidator(validators.BaseValidator):
    def validate(self, outer_result):
        if not isinstance(outer_result, (int, float)):
            return Result(False, "The result should be a float or an integer.")
        if abs(outer_result) > 12:
            return Result(False)
        p = outer_result ** outer_result
        return Result(abs(self._test["input"] - p) < PRECISION, p)


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "super_root"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "superRoot"
    }
    VALIDATOR = SuperRootValidator
