import re

def analyze_failed_logins(log_file):
    """Analyzes auth log file for failed login attempts."""
    print(f"Analyzing failed login data from: {log_file}...\n")

    failed_login_counts = {}
    ip_pattern = r"\d{1,3}(?:\.\d{1,3}){3}"

    try:
        with open(log_file, 'r') as f:
            for line in f:
                if "Failed password" in line:
                    match = re.search(ip_pattern, line)
                    if match:
                        ip_address = match.group(0)
                        failed_login_counts[ip_address] = failed_login_counts.get(ip_address, 0) + 1

    except FileNotFoundError:
        print(f"Error: File not found at '{log_file}'")
        return

    print("--- Failed Login Report ---")
    if not failed_login_counts:
        print("No failed login attempts found.")
    else:
        print("Summary of failed login attempts by IP address:")
        sorted_failed = sorted(failed_login_counts.items(), key=lambda x: x[1], reverse=True)
        for ip, count in sorted_failed:
            print(f"- IP Address: {ip:<18} Failed Count: {count}")
    print("--- End of Failed Login Report ---\n")


def analyze_successful_logins(log_file):
    """Analyzes auth log file for successful login sessions."""
    print(f"Analyzing successful login data from: {log_file}...\n")

    successful_login_counts = {}
    user_pattern = r"session opened for user (\w+)"

    try:
        with open(log_file, 'r') as f:
            for line in f:
                if "session opened for user" in line:
                    match = re.search(user_pattern, line)
                    if match:
                        username = match.group(1)
                        successful_login_counts[username] = successful_login_counts.get(username, 0) + 1

    except FileNotFoundError:
        print(f"Error: File not found at '{log_file}'")
        return

    print("--- Successful Login Report ---")
    if not successful_login_counts:
        print("No successful login attempts found.")
    else:
        print("Summary of successful logins by username:")
        sorted_successful = sorted(successful_login_counts.items(), key=lambda x: x[1], reverse=True)
        for user, count in sorted_successful:
            print(f"- Username: {user:<18} Success Count: {count}")
    print("--- End of Successful Login Report ---\n")


if __name__ == "__main__":
    log_file_path = "auth.log"
    analyze_failed_logins(log_file_path)
    analyze_successful_logins(log_file_path)
   
