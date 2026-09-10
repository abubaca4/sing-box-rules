# sing-box-rules

*[🇷🇺 Читать на русском](README_ru.md)*

This repository is created for the auto-generation of [sing-box](https://sing-box.sagernet.org/) rule sets that I couldn't find online but considered useful for myself. The rule sets are automatically built and updated daily via GitHub Actions.

Currently, the repository contains 2 rule sets. I will add new lists and their descriptions as the need arises. You are also welcome to suggest your own ideas!

## How to Use

You can import the rule sets into your sing-box configuration using the following URLs:

**Via jsDelivr (CDN):**
`https://cdn.jsdelivr.net/gh/abubaca4/sing-box-rules@rule-sets/<list_name>.srs`

**Via GitHub Raw:**
`https://github.com/abubaca4/sing-box-rules/raw/refs/heads/rule-sets/<list_name>.srs`

## Rule Sets

### `global-tlds`
A list of all first-level domains (TLDs) currently existing on the internet.
*   **Source:** [Official IANA TLD List](https://data.iana.org/TLD/tlds-alpha-by-domain.txt)
*   **Use Case:** The idea behind this list is to route all DNS requests to domains that do *not* belong to the global internet (e.g., local hostnames) directly to a local DNS server.
*   **Usage Example:**
    ```json
    {
      "rule_set": "global-tlds",
      "invert": true,
      "server": "dns-local"
    }
    ```

### `router-domains`
A list of domains used by router vendors to open the router's web interface.
*   **Note:** Only domains that are located on globally accessible top-level domains should be added to this list.
