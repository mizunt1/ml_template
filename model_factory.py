import importlib
import models
def load_model(model_name, model_kwargs):
    model = getattr(models, model_name)
    return model(model_kwargs)

def load_data(data_name):
    return data_name

def load_train_fn(train_name):
    return train_name

