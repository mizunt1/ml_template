from dataclasses import dataclass
from simple_parsing import ArgumentParser
from model_factory import load_model, load_data, load_train_fn
import hydra

@hydra.main(config_path='conf', config_name='config')
def main(cfg):
    model = load_model(cfg.model.name, cfg.model_kwargs)
    data = load_data(cfg.data.name)
    train_fn = load_train_fn(cfg.train_fn)
    print("printing this")
    model.print_this()
    print("printing data")
    print(data)
    print("printing train fn")
    print(train_fn)

if __name__ == "__main__":
    main()
