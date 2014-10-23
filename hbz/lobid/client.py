#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import urlparse
import logging
try:
    import json
except ImportError:
    import simplejson as json

import endpoints
import node_types



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

ADDRESS = "lobid.org"
PARAMETERS = ('id', 'name', 'q', 'format')
RDF_SERIALIZATION = "application/json"


class Client:
    
    def __init__(self):
        pass
      

    def _make_rest_uri(self, endpoint, **kwargs):
        
        query = []
        for name, value in kwargs.items():
            if name in PARAMETERS:
                query.append("%s=%s" % (name, value))
        uri = urlparse.urlunparse(('http', ADDRESS, endpoint,'' ,'&'.join(query),''))
        logger.info(uri)
        return uri
    
    def get_info(self, isil):
        
        h = httplib2.Http()
        endpoint = endpoints.ORGANISATION
        uri = self._make_rest_uri(endpoint, id=isil, format='negotiate')
        method = 'GET'
        headers = {
            'Accept':RDF_SERIALIZATION,
            }   
        response, content = h.request(uri, method, headers=headers)
        logger.info(response['status'])
        return content

    def get_graphs(self, content):
        results = json.loads(content)
        graphs = []
        for result in results:
            graph = result.get('@graph', None)
            if graph:
                graphs.append(graph)
        return graphs
        
        
    def parse_organizations(self, graphs):
        organizations = []
        for graph in graphs:
            # graph is a list of dictionaries with a key @id
            organization = {}
            for node in graph:
                node_id = node.get('@id', {})
                node_type = node.get('@type', {})
                if node_type == node_types.ORGANIZATION:
                    orga_node = node
                else:
                    organization[node_id] = node

            for key, value in orga_node.iteritems():
                if value in organization.keys():
                    orga_node[key] = organization[value] 
            organizations.append(orga_node)
        
        return organizations
    

if __name__ == '__main__':
    
    x = Client()
    #answer =  x.get_info('DE-605')
    answer =  x.get_info('DE-A96')
    graphs = x.get_graphs(answer)
    organizations = x.parse_organizations(graphs)
    print "====\n", organizations

