#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import urlparse
import logging

from endpoints import ORGANISATIONS


logger = logging.getLogger(__name__)
console = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

ADDRESS = "lobid.org"
PARAMETERS = ('name', 'q', 'format')


class Client:

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get(self, id=None, **kwargs):
        # http://lobid.org/organisations/DE-6?format=json
        url = self._make_rest_uri(id)
        r = requests.get(url, params=kwargs)
        status = r.status_code
        logger.debug("%s %s" % (url, status))
        if status == 200:
            return r.json()
        else:
            return None

    def _make_rest_uri(self, id=None):
        """Return the URL for the api request."""
        if id:
            path = '/'.join((self.endpoint, id))
        else:
            path = self.endpoint

        rest_uri = urlparse.urlunparse(('https', ADDRESS, path, '', '', ''))
        return rest_uri


if __name__ == '__main__':
    logger.setLevel(logging.INFO)
    x = Client(ORGANISATIONS)
    print x.get(id="DE-605", format="xml")
