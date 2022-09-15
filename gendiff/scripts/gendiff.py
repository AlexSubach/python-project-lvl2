#!/usr/bin/env python

from gendiff.gendiff import generate_diff
from gendiff.cli import pars


def main():
    args = pars()
    print(generate_diff(args[0], args[1]))


if __name__ == '__main__':
    main()
