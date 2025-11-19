import  re

def analyze_log(log_file):
    """ Analyzes an SSH authentication log file for failed login attempts.      """
    print(f"Analyzing log file: {log_file}...\n")

    failed_login_counts = {} 

   # This regular expression will match most standard IPv4 addresses.
    # The 'r' before the string means it's a "raw string", which is best practice for regex.
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    try:
      # Open the log file in read mode ('r')
        with open(log_file, 'r') as f:
            for line in f:
            # Check if the substring "Failed password" exists in the line
             if "Failed password" in line:

              # Now, search within that line for our IP address pattern
               match = re.search(ip_pattern, line)

                 # If the search was successful, 'match' will be an object
               if match:
                 # Extract the matched string (the IP address)
                   ip_address = match.group(0)
                 
                   if ip_address in failed_login_counts:
                       failed_login_counts[ip_address] += 1
                   else:
                       failed_login_counts[ip_address] = 1
                   

    except FileNotFoundError:
      # Handle the case where the log file does not exist 
      print(f"Error: File not found at '{log_file}'")
      return

    print("\n--- Security Analysis Report ---")

    if not failed_login_counts:
       print("No failed login attempts found.")
    else:
       print("Summary of failed login attempts by IP address:")
       sorted_ips = sorted(failed_login_counts.items(), key=lambda x: x[1], reverse=True)

       for ip, count in sorted_ips:
           print(f"- IP Address: {ip:<18} Count: {count}")

    print("\n--- End of Report ---")

# This block ensures the code inside only runs when the script is executed directly
if __name__ == "__main__":
  log_file_path = "auth.log"
  analyze_log(log_file_path)
                      