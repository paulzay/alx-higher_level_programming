#!/usr/bin/python3


def main():
    module_names = dir('4-hidden_discovery.py')
    for s in module_names:
        if not s.startswith("__"):
            print("{}".format(s))


if __name__ == "__main__":
    main()
