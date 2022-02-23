def domain_name(url):

    exclusion = ["http://", "https://", "www.", "https://www.", "http://www."]
    for e in exclusion:
        if e in url:
            url = url.replace(e, "")
    res = url.split(".")
    return res[0]




    # from urllib.parse import urlparse
    # import re
    #
    # n = "www"
    # if n in url:
    #     result = re.findall(r"\.([\w\-]+)\.", url)
    # else:
    #     result = urlparse(url).netloc.split(".")
    #
    # return result[0]



print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))