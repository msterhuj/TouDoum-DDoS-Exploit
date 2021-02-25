import shodan


# shodan return prob ip list todo need to rewrite this function
def get_from_shodan(api: str):
    try:
        api = shodan.Shodan(api)
        ips = []
        print("[*] Shodan request... 0/3")
        results_memcached = api.search("memcached")
        print("[*] Shodan request... 1/3")
        results_dns = api.search("dns")
        print("[*] Shodan request... 2/3")
        results_ntp = api.search("ntp")
        print("[*] Shodan request ok 3/3")
        for result in results_memcached['matches']:
            ips.append(result['ip_str'].replace("\n", ""))
        for result in results_dns['matches']:
            ips.append(result['ip_str'].replace("\n", ""))
        for result in results_ntp['matches']:
            ips.append(result['ip_str'].replace("\n", ""))
        return ips
    except shodan.exception.APIError:
        print("[*] Shodan Api error :/")
        exit(-1)
