"""
iot_publish_doorlock.py without auth and tls
"""

import sys
from paho.mqtt import publish

if len(sys.argv) == 1:
    # Missing arguments
    print("Missing arguments.")
elif str(sys.argv[1]) == "Open":
    # Door Open request
    publish.single("Door_Request", "Open", qos=2, hostname="localhost")
elif str(sys.argv[1]) == "Close":
    # Door Close request
    publish.single("Door_Request", "Close", qos=2, hostname="localhost")
