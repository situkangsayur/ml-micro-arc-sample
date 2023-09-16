from abc import ABC, abstractmethod
from typing import Any, Dict


class LoaderAbstract(ABC):

    @abstractmethod
    def load_data(self, params: Dict[Any, Any]) -> Any:
        raise Exception('Not yet Implemented')
