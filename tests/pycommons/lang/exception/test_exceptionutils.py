from unittest import TestCase

from pycommons.lang.exception import ExceptionUtils


class TestExceptionUtils(TestCase):
    @staticmethod
    def _test(ex, _r_e):
        try:
            raise ex
        except Exception as e:
            raise _r_e from e

    def test_get_cause(self):
        exception = Exception("Some error in try block")
        runtime_error = RuntimeError("Caught and rethrown from except block")

        try:
            self._test(exception, runtime_error)
        except RuntimeError as r:
            self.assertEqual(exception, ExceptionUtils.get_cause(r))

    def test_ignored_context_when_thrown_exception_match(self):
        exception = Exception("Some error in try block")
        runtime_error = RuntimeError("Caught and rethrown from except block")

        with ExceptionUtils.ignored(RuntimeError) as ctx:
            self._test(exception, runtime_error)

        self.assertEqual(runtime_error, ctx.exception)

    def test_ignored_context_when_thrown_exception_doesnt_match(self):
        exception = Exception("Some error in try block")
        runtime_error = ReferenceError("Caught and rethrown from except block")
        with self.assertRaises(ReferenceError):
            with ExceptionUtils.ignored(RuntimeError) as ctx:
                self._test(exception, runtime_error)

        self.assertEqual(runtime_error, ctx.exception)

    def test_ignored_context_when_block_doesnt_throw_exception(self):
        with ExceptionUtils.ignored(RuntimeError) as ctx:
            pass

        self.assertIsNone(ctx.exception)
