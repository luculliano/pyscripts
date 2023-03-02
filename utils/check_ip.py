#!/usr/bin/env python3
from urllib import error, request


def get_ip_info():
    url = "https://ipinfo.io/json"
    try:
        res = request.urlopen(url, timeout=3)
        return res.read().decode()
    except (error.URLError, error.HTTPError, TimeoutError) as err:
        return err


if __name__ == "__main__":
    print(get_ip_info())
