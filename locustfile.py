# import os
# import ssl
import time

from locust import task, TaskSet
from locust.user.wait_time import between
from locust_plugins.users import MqttUser


# tls_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
# tls_context.load_verify_locations(os.environ["LOCUST_MQTT_CAFILE"])


class MyUser(MqttUser):
    host = "localhost"
    port = 1883
    # tls_context = tls_context

    # We could uncomment below to use the WebSockets transport
    # transport = "websockets"
    # ws_path = "/mqtt/custom/path"

    # We'll probably want to throttle our publishing a bit: let's limit it to
    # 10-100 messages per second.
    wait_time = between(0.01, 0.1)

    @task
    class MyTasks(TaskSet):
        # Sleep for a while to allow the client time to connect.
        def on_start(self):
            time.sleep(5)

        @task
        def pub(self):
            self.client.publish("Door_Request", b"Open", 2)
