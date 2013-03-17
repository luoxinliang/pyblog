from string import join
import random
import urllib

def get_client_ip(request,ip=""):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_html(url):
    try:
        f = urllib.urlopen(url)
        data = f.read()
    except:
        return None
    finally:
        f.close() 
    return data

def get_jifen(jine):
    if jine <= 0:
        return 0
    return int(jine * 0.28 * 100)

def gen_random_str(size=8):
    return join(random.sample([chr(i) for i in range(97, 122)], size)).replace(" ","")

