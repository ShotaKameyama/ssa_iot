"""
iot_publish_doorlock.py without auth and tls
"""

import sys
from paho.mqtt import publish

HOST = ""
REQUEST = ""

if len(sys.argv) == 3:
    HOST = str(sys.argv[1])
    REQUEST = str(sys.argv[2])
else:
    # Missing arguments
    print("Missing arguments. Usage: iot_publish_doorlock.py <Host> <Request>")

if REQUEST in ("Open", "Close"):
    # Door Open / Close request
    publish.single("Door_Request", REQUEST, qos=2, hostname=HOST)
