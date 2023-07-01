from unittest import TestCase

from pycommons.lang.exception.exception import CommonsException


class TestCommonsException(TestCase):

    @staticmethod
    def _test(ex, _r_e):
        try:
            raise ex
        except Exception as e:
            raise _r_e from e

    def test_exception(self):
        exception = Exception("Some error in try block")
        runtime_error = CommonsException("Caught and rethrown from except block")
        try:
            self._test(exception, runtime_error)
        except CommonsException as commons_exception:
            self.assertEqual(exception, runtime_error.cause)
            self.assertEqual("Caught and rethrown from except block", commons_exception.message)
            self.assertIsNotNone(commons_exception.traceback)
            self.assertEqual("Some error in try block", commons_exception.detailed_message)
