#!/usr/bin/python3
"""
Parsing log from stdin
"""
import re
import sys
from typing import Tuple
import signal


def check_format(line: str) -> bool:
    ip_adress = r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}'
    date = r'\d{4}\-\d{2}\-\d{2} \d{2}:\d{2}:\d{2}\.\d+'
    status_code = '200|301|400|401|403|404|405|500'
    file_size = r'\b(?:0|[1-9]\d*)\b'
    regex = f'{ip_adress} - [{date}] "GET /projects/260 HTTP/1.1"\
 {status_code} {file_size}$'
    if re.search(regex, line):
        return True
    return False


def extract_size_file_st_code(line: str) -> Tuple[int, int]:
    size = ""
    status_code = ""
    i = -1
    while line[i] != ' ':
        size += line[i]
        i -= 1
    i -= 1
    while line[i] != ' ':
        status_code += line[i]
        i -= 1
    return int(size[::-1]), int(status_code[::-1])


def handler(signum, frame):
    print(output)


signal.signal(signal.SIGINT, handler)
size_files = 0
stat_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
i = 0
for line in sys.stdin:
    output = ""
    if check_format(line):
        i += 1
        size, status_code = extract_size_file_st_code(line)
        size_files += size
        stat_code[status_code] += 1
    output += f'File size: {size_files}\n'
    if i % 10 == 0:
        print(f'File size: {size_files}')
        for key, value in stat_code.items():
            if value != 0:
                print(f'{key}: {value}')
    for key, value in stat_code.items():
        if value != 0:
            output += f'{key}: {value}\n'
