#!/usr/bin/python3
'''A script for parsing HTTP request logs and printing statistics.
'''
import re
import sys


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.
    
    Args:
        input_line (str): A single line from the log input.
    
    Returns:
        dict: A dictionary containing status_code and file_size if matched,
              otherwise returns the default dictionary.
    '''
    # Regular expression to match the expected log format
    log_fmt = (
        r'(?P<ip>\S+) - \[(?P<date>[^\]]+)\] "GET /projects/260 HTTP/1.1" '
        r'(?P<status_code>\d{3}) (?P<file_size>\d+)'
    )
    
    match = re.match(log_fmt, input_line)
    if match:
        return {
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size'))
        }
    return {'status_code': 0, 'file_size': 0}  # default if line doesn't match


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.
    
    Args:
        total_file_size (int): The total size of files processed.
        status_codes_stats (dict): A dictionary of status code counts.
    '''
    print(f'File size: {total_file_size}')
    for status_code in sorted(status_codes_stats.keys()):
        if status_codes_stats[status_code] > 0:
            print(f'{status_code}: {status_codes_stats[status_code]}')


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): The current counts of status codes.

    Returns:
        int: The new total file size after updating with the line's file size.
    '''
    line_info = extract_input(line)
    status_code = line_info['status_code']
    
    # Update only if the status code is valid
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    
    # Return the new total file size
    return total_file_size + line_info['file_size']


def run():
    '''Starts the log parser. Reads input and prints statistics every 10 lines
       or upon keyboard interruption (Ctrl+C).
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    
    try:
        # Read from stdin line by line
        for line in sys.stdin:
            total_file_size = update_metrics(line, total_file_size, status_codes_stats)
            line_num += 1
            # Print stats every 10 lines
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        # Handle Ctrl+C or end of file input gracefully
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
