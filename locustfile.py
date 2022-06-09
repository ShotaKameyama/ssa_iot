'''
This file provides a performance testing against the
MQTT connected device using Locust and its plugin.
'''

# import os
# import ssl
import time

from locust import task, TaskSet
from locust.user.wait_time import between
from locust_plugins.users import MqttUser
from pyaml_env import parse_config, BaseConfig

config = BaseConfig(parse_config('./config/config.yml'))

# tls_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
# tls_context.load_verify_locations(os.environ["LOCUST_MQTT_CAFILE"])


class MyUser(MqttUser):
    '''
    apply MqttUser to the class
    '''
    host = config.mqtt.host
    port = int(config.mqtt.port)
    # tls_context = tls_context

    # We could uncomment below to use the WebSockets transport
    # transport = "websockets"
    # ws_path = "/mqtt/custom/path"

    # We'll probably want to throttle our publishing a bit: let's limit it to
    # 10-100 messages per second.
    wait_time = between(0.01, 0.1)

    @task
    class MyTasks(TaskSet):
        '''
        Define the actual actions when start locust
        and test scenarios.
        '''

        def on_start(self):
            '''
            Sleep for a while to allow the client time to connect.
            '''
            time.sleep(5)

        @task
        def pub(self):
            '''
            Locust task: publish messages.
            '''
            self.client.username_pw_set(
                config.client_camera.user,
                config.client_camera.password)
            self.client.publish(
                config.client_camera.publish.controller,
                config.qr.code[0],
                config.mqtt.qos)
