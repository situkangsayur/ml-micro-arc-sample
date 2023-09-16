from typing import Any, Dict
from typing_extensions import override
from ml_abs import LoaderAbstract
import numpy as np


class CSVLoeader(LoaderAbstract):

    @override
    def load_data(self, params: Dict[Any, Any]) -> Any:
        fname: str = params['filename']
        all_features = []
        all_targets = []
        with open(fname) as f:
            for i, line in enumerate(f):
                if i == 0:
                    print("HEADER:", line.strip())
                    continue  # Skip header
                fields = line.strip().split(",")
                all_features.append([float(v.replace('"', ""))
                                    for v in fields[:-1]])
                all_targets.append([int(fields[-1].replace('"', ""))])
                if i == 1:
                    print("EXAMPLE FEATURES:", all_features[-1])

        features = np.array(all_features, dtype="float32")
        targets = np.array(all_targets, dtype="uint8")
        print("features.shape:", features.shape)
        print("targets.shape:", targets.shape)
        return (features, targets)
