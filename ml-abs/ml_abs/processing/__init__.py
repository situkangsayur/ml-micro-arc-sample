
from abc import ABC, abstractmethod
from typing import Any, Dict


class ProcessAbstract(ABC):
    process_name: str = ''
    model: Any = None
    result_params: Dict[Any, Any] = {}
    method_params: Dict[Any, Any] = {}

    def set_result_params(self, result_params: Dict[Any, Any]) -> None:
        self.result_params = result_params

    def set_method_params(self, method_params: Dict[Any, Any]) -> None:
        self.method_params = method_params

    @abstractmethod
    def run(self, data: Any) -> Any:
        raise Exception('Not yet Implemented')
