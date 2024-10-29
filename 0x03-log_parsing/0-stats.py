#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import re
import sys
from collections import defaultdict


total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0


def print_stats():
    print(f"File size: {total_file_size}")

    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")


line_pattern = re.compile(
    r"^([\w\.:]+) *- *"
    r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{0,6}\] *"
    r'"GET /projects/260 HTTP/1.1" *'
    r"(?P<status_code>\w+) *"
    r"(?P<file_size>\w+)$"
)

try:
    for line in sys.stdin:
        match = line_pattern.match(line.strip())

        if match:
            try:
                file_size = int(match.group("file_size"))
                total_file_size += file_size
            except ValueError:
                pass

            try:
                status_code = int(match.group("status_code"))
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    status_code_counts[status_code] += 1
            except ValueError:
                pass

            line_count += 1

            if line_count % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    pass

finally:
    print_stats()
