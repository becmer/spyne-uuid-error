#!/usr/bin/env python

from suds.client import Client

c = Client("http://localhost:8000/uuid/?wsdl")


