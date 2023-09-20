from typing import Callable

from lib import NMEAMissingRegistryError
from lib.inlet import InletBot

import logging

log = logging.getLogger(__name__)


class InletFactory:
    registry = {}

    @classmethod
    def register(cls, name: str) -> Callable:
        def inner_wrapper(wrapped_class: InletBot) -> Callable:
            if name in cls.registry:
                log.warning(f'Executor {name} already exists. Will replace it')
            cls.registry[name] = wrapped_class
            return wrapped_class

        return inner_wrapper

    @classmethod
    def create_executor(cls, name: str, **kwargs) -> 'InletBot':
        """Inlet Factory to create the executor.
        This method gets the appropriate Executor class from the registry
        and creates an instance of it, while passing in the parameters
        given in ``kwargs``.
        Args:
            name (str): The name of the executor to create.
        Returns:
            An instance of the executor that is created.
        """

        if name not in cls.registry:
            log.warning(f'Executor {name} does not exist in the registry')
            raise NMEAMissingRegistryError

        exec_class = cls.registry[name]
        executor = exec_class(**kwargs)
        return executor
