"""
Problem to solve: 

Take a list of domains (one per line) from a text file as input, find the IP address for the domain using the standard system level DNS, and then check against DoH answers from both cloudflare and google. and say if all answers match properly or not.

"""
import socket
import requests


def main():
    try:
        with open("dumpsites.txt") as list_of_sites:
            for each_site in list_of_sites:
                each_site = each_site.strip().lower()
                local_ip = socket.gethostbyname(each_site).strip()
                google_lookup = requests.get(
                    f"https://dns.google/resolve?name={each_site}"
                )
                google_ip = google_lookup.json()["Answer"][0]["data"].strip()
                cloudflare_url = f"https://cloudflare-dns.com/dns-query?name={each_site}&type=A&ct=application/dns-json"
                cloudflare_lookup = requests.get(cloudflare_url)
                cloudflare_ip = cloudflare_lookup.json()["Answer"][0]["data"].strip()

                print(
                    f"""
---

Site: {each_site}
Local DNS lookup:\t{local_ip}
Google DoH lookup:\t{google_ip}
Cloudflare DoH lookup:\t{cloudflare_ip}"""
                )
                if local_ip == google_ip and local_ip == cloudflare_ip:
                    print("All ip lookups match.")
                elif local_ip == google_ip and not local_ip == cloudflare_ip:
                    print("Local ip matches with Google, but not Cloudflare.")
                elif local_ip == cloudflare_ip and not local_ip == google_ip:
                    print("Local dns lookup matches with Cloudflare, but not Google.")
                else:
                    print(
                        "Local dns lookup does not match with either Google or Cloudflare."
                    )
    except:
        print(
            "Create a file 'dumpfile.txt' in the current directory with a list of domains; one domain per line"
        )


if __name__ == "__main__":
    main()
