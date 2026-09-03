import re

def analyze_log(log_file):
    """Analyzes an SSH authentication log file for failed and successful login attempts."""
    print(f"Analyzing log file: {log_file}...\n")

    failed_login_counts = {}
    successful_login_counts = {}

    ip_pattern = r"\d{1,3}(?:\.\d{1,3}){3}"

    try:
        with open(log_file, 'r') as f:
            for line in f:
                match = re.search(ip_pattern, line)
                if not match:
                    continue

                ip_address = match.group(0)

                if "Failed password" in line:
                    failed_login_counts[ip_address] = failed_login_counts.get(ip_address, 0) + 1

                elif "Accepted password" in line:
                    successful_login_counts[ip_address] = successful_login_counts.get(ip_address, 0) + 1

    except FileNotFoundError:
        print(f"Error: File not found at '{log_file}'")
        return

    print("\n--- Security Analysis Report ---")

    if not failed_login_counts:
        print("No failed login attempts found.")
    else:
        print("Summary of failed login attempts by IP address:")
        sorted_failed = sorted(failed_login_counts.items(), key=lambda x: x[1], reverse=True)
        for ip, count in sorted_failed:
            print(f"- IP Address: {ip:<18} Failed Count: {count}")

    print()

    if not successful_login_counts:
        print("No successful login attempts found.")
    else:
        print("Summary of successful login attempts by IP address:")
        sorted_successful = sorted(successful_login_counts.items(), key=lambda x: x[1], reverse=True)
        for ip, count in sorted_successful:
            print(f"- IP Address: {ip:<18} Success Count: {count}")

    print("\n--- End of Report ---")


if __name__ == "__main__":
    log_file_path = "auth.log"
    analyze_log(log_file_path)