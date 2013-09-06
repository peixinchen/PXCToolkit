__all__ = ["parse"]

import re

ip_seg = r"(1[0-9]{2}|2[1-4][0-9]|25[0-5]|[1-9][0-9]{0,1})"
ip_pattern = re.compile(r"(?P<ip>{ip_seg}\.{ip_seg}\.{ip_seg}\.{ip_seg})".format(ip_seg = ip_seg))

private_rules = (
    r"10\.{ip_seg}\.{ip_seg}\.{ip_seg}".format(ip_seg = ip_seg),
    r"172\.16\.{ip_seg}\.{ip_seg}".format(ip_seg = ip_seg),
    r"172\.17\.{ip_seg}\.{ip_seg}".format(ip_seg = ip_seg),
    r"172\.18\.{ip_seg}\.{ip_seg}".format(ip_seg = ip_seg),
    r"172\.19\.{ip_seg}\.{ip_seg}".format(ip_seg = ip_seg),
    r"172\.2[0-9]\.{ip_seg}\.{ip_seg}".format(ip_seg = ip_seg),
    r"172\.31\.{ip_seg}\.{ip_seg}".format(ip_seg = ip_seg),
    r"192\.168\.{ip_seg}\.{ip_seg}".format(ip_seg = ip_seg),
)

private_pattern = re.compile(r"({rule})".format(
    rule = "|".join(private_rules)
))

def parse(content):
    result = {
        "private": [],
        "public": [],
        "all": [],
    }
    iter = re.finditer(ip_pattern, content)
    if iter:
        for match in iter:
            ip = match.group("ip")
            result["all"].append(ip)
            if re.match(private_pattern, ip):
                result["private"].append(ip)
            else:
                result["public"].append(ip)

    return result
