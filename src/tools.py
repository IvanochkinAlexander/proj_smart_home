import yaml


def load_config(path):
    with open(path, 'r') as stream:
        try:
            a = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        return a
