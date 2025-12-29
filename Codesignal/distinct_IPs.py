# We have a directory /root/devops with multiple subdirectories and files. 
# Some files contain text with valid and invalid IP-like strings. 
# An IP address is valid if: Format: x.x.x.x Each x is between 0 and 255 inclusive Task Scan all files recursively under /root/devops 
# Extract only valid IP addresses Remove duplicates 
# Print them in lexicographical order

import os


root = "/root/devops"

def valid_ip(text):
    parts = text.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if not p.isdigit():
            return False
        p = int(p)
        if (p < 0 or p > 255):
            return False
    return True


def find_ips(root):
    result =  set()
    for path, dir, files in os.walk(root):
        for file in files:
            full_path = os.path.join(path, file)

            try:
                with open(full_path, "r", errors="ignore") as f:
                    for lines in f:
                        for word in lines.split():
                            ips  = word.strip(",.;:")  # strip() only removes characters from the start and the end of the string. # It does not touch anything in the middle.
                            if valid_ip(ips):
                                result.add(ips)
            except OSError:
                continue
    return result          


def main():
    validated_ips = find_ips(root)
    for ip in sorted(validated_ips):
        print(ip)
