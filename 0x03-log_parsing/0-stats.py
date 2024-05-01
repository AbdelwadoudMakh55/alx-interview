#!/usr/bin/env python3
"""
Parsing log from stdin
"""
import sys
from typing import Tuple
import signal


def check_format(line: str) -> bool:
    return True


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


def ctrl_c(output: str):
    def handler(signum, frame):
        print(output, end="")
    return handler


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
    for key, value in stat_code.items():
        if value != 0:
            output += f'{key}: {value}\n'
    if i % 10 == 9:
        print(output, end="")
    signal.signal(signal.SIGINT, ctrl_c(output))
