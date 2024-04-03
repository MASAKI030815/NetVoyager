interface = "eth0"
pingv4_targets = [
    ["8.8.8.8", "Google DNS"],
    ["8.8.4.4", "Google DNS Backup"],
]
pingv6_targets = [
	["2001:4860:4860::8888", "Google DNS IPv6"],
    ["2001:4860:4860::8844", "Google DNS Backup IPv6"],
]
pingv4_large_option = ["-c", "1", "-M", "do", "-s", "3000", "-W", "1"]
pingv4_short_option = ["-c", "1", "-s", "64", "-W", "1"]
pingv6_large_option = ["-c", "5", "-s", "3000", "-W", "5"]
pingv6_short_option = ["-c", "5", "-s", "128", "-W", "5"]
http_check_targets = [
    ["http://ipv4.google.com", "Google-IPv4"],
    ["http://ipv6test.google.com/", "Google-IPv6"],
]
virus_check_targets = [
    ["http://example.com/malicious_file", "Malicious File 1"],
    ["http://example.org/bad_file", "Malicious File 2"]
]
mtr_v4_targets = [
    ["google.com", "Google DNS"],
]
mtr_v6_targets = [
    ["ipv6test.google.com", "Google DNS IPv6"],
]
mtr_v4_mark_hosts = [
    ["google.com", "Google DNS"],
]
mtr_v6_mark_hosts = [
    ["ipv6test.google.com", "Google DNS IPv6"],
]
