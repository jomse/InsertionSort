#!/usr/bin/env python3
import unittest
import sortit
import tempfile


class Tests(unittest.TestCase):
    def test_read_lines_int(self):
        with tempfile.NamedTemporaryFile(mode='w+') as tmp:
            tmp.write('34\n2\n333\n10\n8\n')
            tmp.seek(0)
            self.assertEqual(sortit.read_lines(tmp.name), ['34', '2', '333', '10', '8'])

    def test_read_lines_str(self):
        with tempfile.NamedTemporaryFile(mode='w+') as tmp:
            tmp.write('dfdf\na\ngg\n\n\n\nhty\ncccccc\nzz\n')
            tmp.seek(0)
            self.assertEqual(sortit.read_lines(tmp.name), ['dfdf', 'a', 'gg', '', '', '', 'hty', 'cccccc', 'zz'])

    def test_file_writer(self):
        with tempfile.NamedTemporaryFile(mode='w+') as tmp:
            sortit.write_file(True, False, tmp.name, [34, 2, 333, 10, 8])
            lines = tmp.read().splitlines()
            self.assertEqual(lines, ['34', '2', '333', '10', '8'])

    def test_raises_read_lines(self):
        with self.assertRaises(sortit.FileReadError):
            sortit.read_lines('input_gg.txt')

    def test_raises_file_writer(self):
        with self.assertRaises(sortit.FileReadError):
            sortit.write_file(True, True, 'output.txt', ['zz', 'hty', 'gg', 'dfdf', 'cccccc', 'a', '', '', ''])

    def test_raises_convert_lines_to_ints_int(self):
        with self.assertRaises(sortit.NotIntError):
            sortit.convert_lines_to_ints(True, ['34', 'z', '333', '10', '8'])

    def test_raises_convert_lines_to_ints_str(self):
        with self.assertRaises(sortit.NotIntError):
            sortit.convert_lines_to_ints(True, ['dfdf', 'a', 'gg', '', '', '', 'hty', 'cccccc', 'zz'])


if __name__ == '__main__':
    unittest.main()

