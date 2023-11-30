#!/usr/bin/python3


if __name__ == "__main__":
    module_names = dir('4-hidden_discovery.py')
    for s in module_names:
        if not s.startswith("__"):
            print("{}".format(s))
