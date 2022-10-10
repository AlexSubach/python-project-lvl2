import argparse


def pars():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')   # noqa: E501
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format',
                        type=str,
                        choices=['stylish'],
                        default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
