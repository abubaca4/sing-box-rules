import os

from utils import process_rule_set

RULE_NAME = "router-domains"
LOCAL_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../local_sources/router-domains.txt'))

def main():
    if not os.path.exists(LOCAL_FILE):
        raise FileNotFoundError(f"Local source not found: {LOCAL_FILE}")

    domains = []
    with open(LOCAL_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                domains.append(line)

    domains = sorted(set(domains)) # Убираем дубликаты и сортируем

    rule = {
        "domain": domains
    }

    process_rule_set(RULE_NAME, [rule])

if __name__ == "__main__":
    main()
