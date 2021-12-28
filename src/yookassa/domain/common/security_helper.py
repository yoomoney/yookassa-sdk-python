# -*- coding: utf-8 -*-
from netaddr import IPNetwork, IPAddress


class SecurityHelper:
    """
    """

    def __init__(self):
        pass

    YOOKASSA_NETWORKS = [
        '77.75.153.0/25',
        '77.75.156.11',
        '77.75.156.35',
        '77.75.154.128/25',
        '185.71.76.0/27',
        '185.71.77.0/27',
        '2a02:5180:0:1509::/64',
        '2a02:5180:0:2655::/64',
        '2a02:5180:0:1533::/64',
        '2a02:5180:0:2669::/64'
    ]

    @staticmethod
    def is_ip_in_network(ip, network):
        return IPAddress(ip) in IPNetwork(network)

    def is_ip_trusted(self, ip):
        for item in self.YOOKASSA_NETWORKS:
            if '/' in item:
                if self.is_ip_in_network(ip, item):
                    return True
            else:
                if ip == item:
                    return True

        return False
