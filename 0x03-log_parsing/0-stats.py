#!/usr/bin/python3
"""
Reads `stdin` line by line and computes metrics.
"""

import re

pattern = (
    r'(?P<ip_address>\S+) - \[(?P<date>.+?)\] "(?P<method>\S+) '
    r'(?P<endpoint>\S+) HTTP/\d\.\d" (?P<status_code>\d+) '
    r'(?P<file_size>\d+)'
)

total_size = 0
status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
status_codes = {code: 0 for code in status_codes}

read_lines = 0
did_print = False

try:
    while True:
        line = input()
        match = re.match(pattern, line)

        if match:
            data = match.groupdict()
            total_size += int(data["file_size"])
            status_codes[data["status_code"]] += 1

        read_lines += 1
        did_print = False

        if read_lines % 10 == 0:
            print(f"File size: {total_size}")

            for k, v in status_codes.items():
                print(f"{k}: {v}")

            did_print = True

except (KeyboardInterrupt, EOFError):
    if not did_print:
        print(f"File size: {total_size}")

        for k, v in status_codes.items():
            print(f"{k}: {v}")
