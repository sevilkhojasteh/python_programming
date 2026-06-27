import re

url = input("URL: ").strip()

# username = url.removeprefix("https://twitter.com/", "")


# print(f"Username: {username}")


username = re.sub(r"(https?://)?(www\.)?twitter\.com/", "", url)

print(f"Username: {username}")

matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url)

if matches:
    print(f"Username: {matches.group(1)}")


# (...) a group
# (?: ...) non-capturing version

# if we don't write (?:www\.) we can get the usename from matches.group(2)



