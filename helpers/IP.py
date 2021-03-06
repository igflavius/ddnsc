#!/usr/bin/env python3

import sys, requests

class IP:

    @staticmethod
    def getPublic():

        try:
            response = requests.get("https://ipinfo.io")
            if response.status_code == 200:
                ip = response.json()
                return ip['ip']
        except requests.exceptions.RequestException as e:
            print("ERROR: Unable to get public IP address!")
            print( e )
            sys,exit(1)
