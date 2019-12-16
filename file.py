import argparse, json, sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help="Configuration file in json format")
    args = parser.parse_args()
    json_file = args.c
    if json_file:
        with open("C:\\Users\\elie\\Workspace\\smarthome\\config.json") as f:
            config = json.load(f)
            print(config)