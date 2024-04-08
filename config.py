interface = "{1984C643-096C-42F0-8CD9-48BAD766A457}"

pingv4_targets = [
    ["8.8.8.8", "Google DNS"],
    ["8.8.4.4", "Google DNS Backup"],
]

pingv6_targets = [
    ["2001:4860:4860::8888", "Google DNS IPv6"],
    ["2001:4860:4860::8844", "Google DNS Backup IPv6"],
]

#Windows
pingv4_short_option = ["-4 -n 1 -w 1"]
pingv4_large_option = ["-4 -n 1 -l 1472 -w 1"]
pingv6_short_option = ["-6 -n 1 -w 1"]
pingv6_large_option = ["-6 -n 1 -l 1452 -w 1"]

#Linux
#pingv4_large_option = ["-4","-c", "2", "-M", "do", "-s", "1000", "-W", "1"]
#pingv4_short_option = ["-4","-c", "2", "-s", "64", "-W", "1"]
#pingv6_large_option = ["-6","-c", "2", "-s", "1000", "-W", "1"]
#pingv6_short_option = ["-6","-c", "2", "-s", "128", "-W", "1"]

http_check_targets = [
    ["http://ipv4.google.com", "Google-IPv4"],
    ["http://ipv6test.google.com/", "Google-IPv6"],
]

virus_check_targets = [
    ["http://urlfiltering.paloaltonetworks.com/test-command-and-control", "Palo virus check_1"],
    ["http://urlfiltering.paloaltonetworks.com/test-malware", "Palo virus check_2"],
    ["http://urlfiltering.paloaltonetworks.com/test-phishing","Palo virus check_3"],
    ["http://urlfiltering.paloaltonetworks.com/test-ransomware","Palo virus check_4"],
    ["http://wildfire.paloaltonetworks.com/publicapi/test/pe","Palo virus check_5"],
]

mtr_v4_targets = [
    ["8.8.8.8", "Google DNS"],
]

mtr_v6_targets = [
    ["2001:4860:4860::8888", "Google DNS IPv6"],
]

mtr_v4_mark_hosts = [
    ["8.8.8.8", "Google DNS"],
]

mtr_v6_mark_hosts = [
    ["2001:4860:4860::8888", "Google DNS IPv6"],
]
