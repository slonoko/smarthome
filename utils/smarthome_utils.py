import argparse, json, sys

def read_configuration():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",  nargs='+', help="Configuration file in json format")
    args = parser.parse_args()
    json_file = args.config[0]
    config = {}
    if json_file:
        with open(json_file) as f:
            config = json.load(f)
    return config