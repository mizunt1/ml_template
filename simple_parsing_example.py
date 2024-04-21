from dataclasses import dataclass
from simple_parsing import ArgumentParser


def main(log_dir=None, size_input=None, seed=None):
    print(size_input)
    
    
if __name__ == "__main__":
    @dataclass 
    class Default():
        # use like default values
        # argparse will over write these default values
        size_input: int = 5
    parser = ArgumentParser()

    parser.add_arguments(Default, dest="options")
    args = parser.parse_args()
    main(**vars(args.options))
    
