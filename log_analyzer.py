def analyze_logs_manually(log_file_path):
    """
    Parses a web server log file using only basic Python dictionaries
    to identify top traffic sources and potential bots.
    """
    print(f"--- Starting manual analysis of {log_file_path} ---")

    # Initialize dictionaries to store the counts of IPs, pages, and countries.
    ip_counts = {}
    page_counts = {}
    country_counts = {}

    # Open the log file and process it line by line.
    with open(log_file_path, 'r') as f:
        for line in f:
            try:
                # Split each line into parts to extract the required data.
                parts = line.split()
                ip = parts[0]
                page = parts[6]
                country = parts[2]

                # Increment the count for the IP address in its dictionary.
                if ip in ip_counts:
                    ip_counts[ip] += 1
                else:
                    ip_counts[ip] = 1

                # Increment the count for the visited page.
                if page in page_counts:
                    page_counts[page] += 1
                else:
                    page_counts[page] = 1
                
                # Increment the count for the country code.
                if country in country_counts:
                    country_counts[country] += 1
                else:
                    country_counts[country] = 1

            # Skip any lines that are malformed or blank.
            except IndexError:
                print(f"Warning: Could not parse line: {line.strip()}")

    # --- ANALYSIS AND RESULTS ---

    # Sort the IP addresses by count and print the top 10.
    print("\n--- TOP 50 IP ADDRESSES ---")
    sorted_ips = sorted(ip_counts.items(), key=lambda item: item[1], reverse=True)
    for ip, count in sorted_ips[:50]:
        print(f"{ip}: {count} requests")

    # Sort the visited pages by count and print the top 10.
    print("\n--- TOP 10 VISITED PAGES ---")
    sorted_pages = sorted(page_counts.items(), key=lambda item: item[1], reverse=True)
    for page, count in sorted_pages[:10]:
        print(f"{page}: {count} visits")

    # Sort the countries by count and print the top 5.
    print("\n--- TOP 5 TRAFFIC COUNTRIES ---")
    sorted_countries = sorted(country_counts.items(), key=lambda item: item[1], reverse=True)
    for country, count in sorted_countries[:5]:
        print(f"{country}: {count} requests")


# This block runs only when the script is executed directly.
if __name__ == "__main__":
    # Define the name of the log file to be analyzed.
    log_filename = "sample-log.log"
    # Call the main function to start the analysis.
    analyze_logs_manually(log_filename)
