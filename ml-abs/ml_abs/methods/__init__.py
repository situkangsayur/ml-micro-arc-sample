from abc import ABC, abstractmethod
from typing import Any

from ml_abs.model import Model
from ml_abs.pipeline import Pipeline
from ml_abs.utilities.data_loader import LoaderAbstract


class MethodAbstract(ABC):

    pipeline: Pipeline = Pipeline()
    model: Model
    obj_model: Any
    target: str = ''
    data_loader: LoaderAbstract

    def set_pipeline(self, pipeline: Pipeline) -> None:
        self.pipeline = pipeline

    def set_model(self, model: Model) -> None:
        self.model = model

    @abstractmethod
    def training(self) -> Model:
        raise Exception('Not yet implemented')

    @abstractmethod
    def evaluate(self) -> Model:
        raise Exception('Not yet implemented')

    @abstractmethod
    def predict(self) -> Any:
        raise Exception('Not yet implemented')
