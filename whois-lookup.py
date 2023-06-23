import whois

def is_registered(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)

domains = [
    "google.com",
    "github.com",
    "caddnation.com"
]

for domain in domains:
    whois_info = whois.whois(domain)
    print("Domain:", domain)
    print("Domain registrar:", whois_info.registrar)
    print("WHOIS Server:", whois_info.whois_server)
    print("Domain creation date:", whois_info.creation_date)
    print("Expiration date:", whois_info.expiration_date)
