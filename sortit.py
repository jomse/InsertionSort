#!/usr/bin/env python3
import sys
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser('Sort lines of text file using insertion sort')
    group_sort_type = parser.add_mutually_exclusive_group()
    group_sort_type.add_argument('-i', '--integer', help='Compare lines as integers',
                                 action='store_true')
    group_sort_type.add_argument('-s', '--string', help='Compare lines lexicographically',
                                 action='store_true')

    group_sort_mode = parser.add_mutually_exclusive_group()
    group_sort_mode.add_argument('-a', help='Sort lines in ascending order',
                                 action='store_true')
    group_sort_mode.add_argument('-d', help='Sort lines in descending order ',
                                 action='store_true')

    parser.add_argument('input_file', type=str, default='in.txt', help='Path to input file',
                        metavar='PATH')
    parser.add_argument('output_file', type=str, default='out.txt', help='Path to output file',
                        metavar='PATH')

    return parser.parse_args()


def main():
    args = parse_arguments()
    try:
        sort_list = read_lines(args.input_file)
        sort_list = convert_lines_to_ints(args.integer, sort_list)
        insertion_sort(sort_list)
        write_file(args.integer, args.d, args.output_file, sort_list)
    except NotIntError as err_list:
        print(err_list)
        sys.exit(1)
    except FileReadError as err:
        print('Can not read file', str(err))
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
        pass


def read_lines(input_file):
    try:
        with open(input_file) as input_file:
            lines = input_file.read().splitlines()
    except IOError as err:
        raise FileReadError('Cannot read input file {0}: {1}'.format(input_file, err))
    print(lines)
    return lines


def convert_lines_to_ints(is_integer, lines):
    if not is_integer:
        return lines
    convention_err = []
    int_list = []
    for i in range(0, len(lines)):
        try:
            int_list.append(int(lines[i]))
        except ValueError:
            convention_err.append('Input line № {0} "{1}" is not an integer'.format(i, lines[i]))
    if convention_err:
        raise NotIntError('\n'.join(convention_err))
    print(int_list)
    return int_list


def write_file(is_integer, reverse, output_file, sort_list):
    if is_integer:
        sort_list = [str(rec) for rec in sort_list]
    if reverse:
        sort_list.reverse()
    print(sort_list)
    try:
        with open(output_file, 'w') as output_file:
            output_file.write('\n'.join(sort_list) + '\n')
    except IOError as err:
        raise FileReadError('Cannot read output file {0}: {1}'.format(output_file, err))


def insertion_sort(sort_list):
    for j in range(1, len(sort_list)):
        key = sort_list[j]
        i = j - 1
        while i >= 0 and sort_list[i] > key:
            sort_list[i + 1] = sort_list[i]
            i -= 1
        sort_list[i + 1] = key


class FileReadError(Exception):
    pass


class NotIntError(Exception):
    pass


if __name__ == '__main__':
    main()
