import paho.mqtt.client as mqtt
from pyaml_env import parse_config, BaseConfig

config = BaseConfig(parse_config('./config/config.yml'))


def on_connect(client, userdata, flags, rc):
    client.subscribe('#', qos=0)
    client.subscribe('$SYS/#')


def on_message(client, userdata, message):
    print('Topic: %s | QOS: %s  | Message: %s'
          % (
              message.topic,
              message.qos,
              message.payload))


def main():
    client = mqtt.Client()
    # client.username_pw_set("client_camera", "12345678")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(
        config.mqtt.host,
        int(config.mqtt.port))
    client.loop_forever()


if __name__ == "__main__":
    main()
