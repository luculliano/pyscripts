#!/usr/bin/python
import ipaddress
import json
import os
import sys
from secrets import choice
from string import ascii_lowercase

import requests

# Add api key to API_KEY here
API_KEY = os.getenv("IPDATA_API")


def ip_check(ip_address):
    "Check is ip address is valid"
    try:
        ipaddress.ip_network(ip_address)
        return True
    except ValueError:
        return False


def get_ip_info(api_key, ip_address=""):
    "Get information via ip address using ipdata.co API"
    fields_first = (
        "ip",
        "country_name",
        "region",
        "city",
        "postal",
        "calling_code",
        "time_zone",
        "latitude",
        "longitude",
        "asn",
        "threat",
    )
    fields_second = (
        "name",
        "current_time",
        "domain",
        "route",
        "is_tor",
        "is_vpn",
        "is_proxy",
        "is_datacenter",
        "is_anonymous",
    )

    try:
        response = requests.get(
            f"https://api.ipdata.co/{ip_address}",
            params={"api-key": api_key},
            timeout=1,
        )
        # get only desiried data from the response
        result = {}
        for first_key, first_value in response.json().items():
            if first_key in fields_first:
                if not isinstance(first_value, dict):
                    result.setdefault(first_key, first_value)
                else:
                    for second_key, second_value in first_value.items():
                        if second_key in fields_second:
                            result.setdefault(first_key, {}).update(
                                {second_key: second_value}
                            )
        # return sorted data
        return dict(sorted(result.items(), key=lambda tpl: fields_first.index(tpl[0])))

    except requests.ConnectionError:
        return False


def get_dns_info():
    "Get dns server information using ip-api.com"
    try:
        # chars for faster response
        chars = "".join(choice(ascii_lowercase + "1234567890") for _ in range(32))
        dns_url = f"http://{chars}.edns.ip-api.com/json"
        response = requests.get(dns_url, timeout=1)

        return response.json()

    except requests.ConnectionError:
        return False


def main():
    "The logic of the script"
    args = sys.argv

    print(f"Usage: {os.path.basename(args[0])} [IP]\n---")

    if len(args) == 1:
        ip_data = get_ip_info(API_KEY)
        if ip_data:
            # add map link to result
            ip_data.setdefault(
                "map",
                f"https://www.openstreetmap.org/search/?query={ip_data['latitude']}%2C{ip_data['longitude']}",
            )

            dns_data = get_dns_info()
            if dns_data:
                # add dns server to result
                ip_data.update(dns_data)

            print(json.dumps(ip_data, indent=3))
        else:
            print("No response provided!")

    elif len(args) == 2:
        if ip_check(args[1]):
            ip_data = get_ip_info(API_KEY, args[1])
            if ip_data:
                # add map link to result
                ip_data.setdefault(
                    "map",
                    f"https://www.openstreetmap.org/search/?query={ip_data['latitude']}%2C{ip_data['longitude']}",
                )
                print(json.dumps(ip_data, indent=3))
            else:
                print("No response provided!")
        else:
            print(f"'{args[1]}' does not appear to be an IPv4 or IPv6 network")

    else:
        print("Invalid arguments!")


if __name__ == "__main__":
    main()
