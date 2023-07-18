"""
DESCRIPTION:
Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"
"""


def remove_url_anchor(url):
    if "#" in url:
        return "#".join(url.split("#")[:-1])
    else:
        return url