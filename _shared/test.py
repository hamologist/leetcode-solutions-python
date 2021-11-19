from typing import Generic, TypeVar
from unittest import TestCase, main


T = TypeVar('T')


class BaseTest(TestCase, Generic[T]):
    _solution: T = None

    def setUp(self) -> None:
        self.solution: T = self._solution()
        super().setUp()

    @staticmethod
    def execute() -> None:
        main()
