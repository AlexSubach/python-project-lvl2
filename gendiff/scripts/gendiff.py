#!/usr/bin/env python

from gendiff.gendiff import generate_diff
from gendiff.cli import pars


def main():
    first_file, second_file, formats = pars()
    print(generate_diff(first_file, second_file, formats))


if __name__ == '__main__':
    main()
