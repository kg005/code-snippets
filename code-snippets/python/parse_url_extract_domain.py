
from tldextract import extract


def domain_from_url(url:str)->str:
    # tsd, td, tsu = extract("http://abc.hostname.com/somethings/anything/") # gets abc, hostname, com
    if url:
        tsd, td, tsu = extract(url)
        return f'{td}.{tsu}' # hostname.com

dfu_udf = F.udf(domain_from_url,StringType())