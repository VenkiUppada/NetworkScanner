Title: ARP Network Scanner

Description:
This code performs an ARP network scan to discover the IP and MAC addresses of devices within a specified IP address range. It uses the scapy library to send ARP requests and receive responses from devices on the network. The code allows the user to specify the IP address range to scan as a command-line argument.

Usage:
1. Make sure you have the scapy library installed.
2. Run the code with the desired IP address range as a command-line argument.

Steps:
1. Import Required Libraries:
   - The code imports the necessary libraries for SSL options, tabnanny verbose mode, time measurement, scapy functionalities, and command-line argument parsing.

2. Define the get_args() Function:
   - This function uses the optparse library to parse command-line arguments.
   - It creates an OptionParser object and adds an option for the target IP address range.
   - If no IP address range is provided, the function raises an error.
   - Otherwise, it returns the parsed options.

3. Define the scan() Function:
   - The scan() function takes the target IP address range as input.
   - It creates an ARP request packet with the specified IP address range.
   - It creates an Ethernet broadcast packet to send the ARP request to all devices on the network.
   - It combines the ARP request and broadcast packets.
   - It uses the scapy.srp() function to send the combined packet and receive responses within a timeout.
   - It extracts the IP and MAC addresses from the received responses and stores them in a list of dictionaries.
   - Finally, it returns the list of dictionaries containing the IP and MAC addresses.

4. Define the print_result() Function:
   - The print_result() function takes the result list as input.
   - It prints the header for the IP and MAC address table.
   - It iterates over each dictionary in the result list and prints the IP and MAC addresses in a formatted manner.

5. Parse Command-Line Arguments:
   - The code calls the get_args() function to parse the command-line arguments and retrieve the options.
   - If no IP address range is specified, an error is raised.

6. Perform Network Scan and Print Results:
   - The code calls the scan() function with the specified IP address range to perform the network scan and retrieve the scan results.
   - The code calls the print_result() function to print the IP and MAC addresses of the discovered devices.

Functions and Libraries:
- ssl.Options: Provides options for SSL/TLS connections.
- tabnanny.verbose: Enables verbose mode for tabnanny, which checks for inconsistent indentation.
- time.time(): Measures the current time.
- scapy.all: Provides various functions and classes for network scanning and packet manipulation.
- optparse.OptionParser: Parses command-line arguments.
- get_args(): Parses command-line arguments and returns the options.
- scan(ip): Performs an ARP network scan and returns a list of dictionaries containing IP and MAC addresses.
- print_result(result_list): Prints the IP and MAC addresses from the result list in a formatted manner.
- options = get_args(): Parses command-line arguments and retrieves the options.
- scan_result = scan(options.ip): Performs a network scan with the specified IP address range and stores the results.
- print_result(scan_result): Prints the IP and MAC addresses of the discovered devices.
