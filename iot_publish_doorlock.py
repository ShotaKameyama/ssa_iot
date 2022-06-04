"""
iot_publish_doorlock.py without auth and tls
"""

import sys
from paho.mqtt import publish

HOST = ""
REQUEST = ""
certPath = 'certs/ca.crt'

if len(sys.argv) == 3:
    HOST = str(sys.argv[1])
    REQUEST = str(sys.argv[2])
else:
    # Missing arguments
    print("Missing arguments. Usage: iot_publish_doorlock.py <Host> <Request>")

if REQUEST in ("Open", "Close"):
    # Door Open / Close request
    tls = {'ca_certs': certPath}
    # auth = {'username': "<username>", 'password': "<password>"}
    # publish.single("Door_Request", REQUEST, qos=2, hostname=HOST, tls=tls)
    publish.single("Door_Request", payload="ON", qos=2, retain=False, hostname="localhost",
                   port=8883, tls=tls)
