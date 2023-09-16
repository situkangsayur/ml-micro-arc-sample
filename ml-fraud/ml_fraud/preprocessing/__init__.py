from typing import Any
from typing_extensions import override
from ml_abs import ProcessAbstract
import numpy as np


class Normalization(ProcessAbstract):

    @override
    def run(self, data: Any) -> Any:
        mean = np.mean(data, axis=0)
        data -= mean
        std = np.std(data, axis=0)
        data /= std
        self.result_params = {
            'mean': mean,
            'std': std
        }
        return (data, self.result_params)
