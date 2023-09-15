from abc import ABC, abstractmethod
from typing import Any

from ml_abs.model import Model
from ml_abs.pipeline import Pipeline


class MethodAbstract(ABC):

    pipeline: Pipeline = Pipeline()
    model: Model
    obj_model: Any
    target: str = ''

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
    def predict(self) -> Model:
        raise Exception('Not yet implemented')


