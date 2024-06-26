#!/usr/bin/python3
"""
Parsing log from stdin
"""
import re
import sys
from typing import Tuple


def check_format(line: str) -> bool:
    ip_adress = r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?){4}'
    date = r'\[\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}\.\d+\]'
    status_code = '200|301|400|401|403|404|405|500'
    file_size = r'0|[1-9]\d{0,2}|102[0-4]'
    regex = f'{ip_adress} - {date} "GET /projects/260 HTTP/1.1"\
 {status_code} {file_size}$'
    if re.search(regex, line):
        return True
    return False


def extract_size_file_st_code(line: str) -> Tuple[int, int]:
    size = ""
    status_code = ""
    i = -2
    while line[i] != ' ':
        size += line[i]
        i -= 1
    i -= 1
    while line[i] != ' ':
        status_code += line[i]
        i -= 1
    size = int(size[::-1]) if size.isnumeric() else 0
    status_code = int(status_code[::-1]) if status_code.isnumeric() else 0
    return size, status_code


if __name__ == '__main__':
    size_files = 0
    status = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    i = 0
    try:
        for line in sys.stdin:
            if check_format(line):
                i += 1
                size, status_code = extract_size_file_st_code(line)
                size_files += size
                if status_code != 0:
                    status[status_code] += 1
            if i == 10:
                i = 0
                print(f'File size: {size_files}')
                for key, value in status.items():
                    if value != 0:
                        print(f'{key}: {value}')
    except KeyboardInterrupt:
        raise
    finally:
        print(f'File size: {size_files}')
        for key, value in status.items():
            if value != 0:
                print(f'{key}: {value}')
