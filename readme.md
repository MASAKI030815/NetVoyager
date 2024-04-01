# Network Diagnostic Tool

This script is a tool for conducting network diagnostics. It automatically checks IPv4 and IPv6 connectivity, HTTP responses, and access to specific malware download sites. The results of the diagnostics are displayed in real-time on the console, allowing you to quickly grasp the state of the network.

## Features

- Ping check for IPv4 and IPv6
- Check for HTTP response status
- Check access to malware download sites
- Trace route analysis with MTR reports

## Prerequisites

To run this script, Python must be installed. Additionally, the following Python modules are required:

- netifaces
- requests

## Installation

Execute the following command to install the necessary Python modules:

```bash
pip install netifaces requests
```

## How to Use

To run the script, enter the following command in the terminal:

```bash
python network_diagnostic_tool.py
```

Upon execution, the following results will be output:
- Network configuration information for the specified interface
- Results of the ping test
- Results of the HTTP status check
- Results of the access check to malware download sites
- Trace route analysis with MTR

## License

This project is published under the MIT license.
