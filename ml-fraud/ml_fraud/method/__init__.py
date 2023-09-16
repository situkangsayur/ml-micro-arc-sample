from os import pipe
from typing import Any, Dict, overload
from typing_extensions import override
from ml_abs import LoaderAbstract, MethodAbstract, Model, pipeline
from tensorflow import keras
from keras.src.engine.base_layer import Layer
import uuid
import datetime


class KerasFraudAlgo(MethodAbstract):

    def __init__(self, filename: str, data_loader: LoaderAbstract, pipeline: Pipeline, params: Dict[Any, Any]) -> None:
        self.pipeline = pipeline
        self.instances, self.targets = data_loader.load_data(filename)
        self.params = params
        self.dataset_name = filename

        self.model_structure = [{
                    'dense': 256,
                    'activation': 'relu',
                    'input_shape' : -1,
                    },{
                    'dense' : 256,
                    'activation': 'relu',
                    'dropout': 0.3,
                    },{
                    'dense' : 256,
                    'activation': 'relu',
                    'dropout': 0.3,
                    },{
                    'dense' : 256,
                    'activation': 'relu',
                    'dropout': 0.3,
                    }]

        self.optimizer= {
                'optimizer': keras.optimizers.Adam(1e-2), 
                'loss' : "binary_crossentropy"
                }



    def object_to_model(self, object_model: keras.engine.training.Model) -> Dict[Any, Any]:
        model_dict = {
                'model_structure' : self.model_structure,
                'optimizer' : self.optimizer
                }
        return model_dict
       
    @override
    def training(self) -> Model:
        layers:List[Layer] = []

        for l in self.model_structure:
            if 'input_shape' in l:
                layers.append(keras.layers.Dense(
                    l['dense'], activation=l['activation'], input_shape=(train_features.shape[l['input_shape']],)
                    ))
            else:
                layers.append(keras.layers.Dense(l['dense'], activation=l['activation']))
                if 'dropout' in l:
                    layers.append(keras.layers.Dropout(0.3))


        self.obj_model = keras.Sequential(layers)

        self.obj_model.compile(
            optimizer=self.optimizer['optimizer'], loss=self.optimizer['loss']
        )

        callbacks = [keras.callbacks.ModelCheckpoint(
            "fraud_model_at_epoch_{epoch}.h5")]
        class_weight = {0: weight_for_0, 1: weight_for_1}

        self.obj_model.fit(
            train_features,
            train_targets,
            batch_size=self.params['barch_size'],
            epochs=self.params['epoch'],
            verbose=self.verbose['verbose'],
            callbacks=callbacks,
            validation_data=(val_features, val_targets),
            class_weight=class_weight,
        )

        self.model = Model(
            id_mode=uuid.uuid5(),
            dataset_name=self.dataset_name,
            method_detail=self.object_to_model(slef.obj_model),
            pipeline=None,
            feature_column=[],
            version=str(datetime.datetime.now()),
            created_at=datetime.datetime.now()
        )
        return self.model

    def evaluate(self) -> Model:
        raise Exception('Not yet implemented')

    def predict(self) -> Any:
        raise Exception('Not yet implemented')
