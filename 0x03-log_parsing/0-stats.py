#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_file_size = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
valid_status_codes = set(status_code_counts.keys())
line_count = 0

def print_stats():
    """Print the total file size and the count of status codes in ascending order."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (Ctrl + C)."""
    print_stats()
    sys.exit(0)

# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
try:
    for line in sys.stdin:
        parts = line.split()
        
        # Check if the line matches the expected format
        if len(parts) != 7 or not parts[0].count('.') == 3 or not parts[1] == '-' or not parts[3].startswith('"GET') or not parts[4] == 'HTTP/1.1"':
            continue  # Skip invalid lines
        
        try:
            # Extract file size and status code
            status_code = int(parts[5])
            file_size = int(parts[6])
            
            # Update total file size
            total_file_size += file_size
            
            # Update status code count if it's a valid code
            if status_code in valid_status_codes:
                status_code_counts[status_code] += 1
            
            line_count += 1
            
            # Every 10 lines, print the stats
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            continue  # Skip lines with invalid numbers or missing fields

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

