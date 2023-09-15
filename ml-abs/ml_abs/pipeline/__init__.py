
from abc import ABC, abstractmethod
from typing import Any, Dict, List
from typing_extensions import override

from ml_abs.processing import ProcessAbstract


class PipelineAbstract(ABC):

    @abstractmethod
    def get_pipe(self) -> List[ProcessAbstract]:
        raise Exception('Not yet implemented')

    @abstractmethod
    def get_process_by_name(self, name: str) -> ProcessAbstract:
        raise Exception('Not yet implemented')

    @abstractmethod
    def get_process_by_index(self, index: int) -> ProcessAbstract:
        raise Exception('Not yet implemented')

    @abstractmethod
    def add_process(self, process: ProcessAbstract) -> None:
        raise Exception('Not yet Implemented')

    @abstractmethod
    def execute(self) -> Any:
        raise Exception('Not Yet Implemented')


class Pipeline(PipelineAbstract):

    pipe:List[ProcessAbstract] 
    name_seq: Dict[str, int]

    def __init__(self) -> None:
        super().__init__()
        self.pipe = []
        self.name_list = {}

    @override
    def get_pipe(self) -> List[ProcessAbstract]:
        return self.pipe

    @override
    def get_process_by_name(self, name: str) -> ProcessAbstract:
        return self.pipe[self.name_list[name]]

    @override
    def get_process_by_index(self, index: int) -> ProcessAbstract:
        return self.pipe[index]

    @override
    def add_process(self, process: ProcessAbstract) -> None:
        self.pipe.append(process)
        self.name_list[process.process_name] = len(self.pipe) - 1
        
    @override
    def execute(self, data: Any) -> Any:
        result: Any = data
        
        for process in self.pipe:
            result = process.run(result)

        return result

