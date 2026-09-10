from curl_cffi import requests
from utils import process_rule_set

# Официальный список IANA
URL = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
RULE_NAME = "global-tlds"

def fetch_tlds():
    # impersonate="chrome" позволяет обойти большинство базовых защит Cloudflare/DDoS-Guard
    response = requests.get(URL, impersonate="chrome")
    response.raise_for_status()

    tlds = []
    for line in response.text.splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            tlds.append(f".{line.lower()}")

    return sorted(tlds)

def main():
    try:
        tlds = fetch_tlds()
        if not tlds:
            raise ValueError("Fetched TLD list is empty!")

        # Формируем правило для sing-box (без invert, т.к. headless-списки
        # предоставляют только сами данные, invert настраивается уже на клиенте)
        rule = {
            "domain_suffix": tlds
        }

        process_rule_set(RULE_NAME, [rule])

    except Exception as e:
        print(f"[{RULE_NAME}] Error: {e}")
        raise

if __name__ == "__main__":
    main()
