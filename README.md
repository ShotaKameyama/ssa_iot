# Prerequisite

The following should be installed already before setup.
- Python3
- Mosquitto Installed

## how to install mosquitto

- MacOS: `brew install mosquitto`
- Linux:
- Debian: `apt-get update && apt-get install mosquitto`
- Windows: 

# Getting Started

## Install Necessary Source Code and Libraries

```
git clone https://github.com/ShotaKameyama/ssa_iot.git`
cd ssa_iot
make install
```

## Change Config

Change `config/config.yml` as necessary.
If you need remote access against the MQTT braker, you need to change `mqtt.host`.

# Basic Inforamtion

This IoT system consists of 4 instances:
- MQTT braker
- IoT Controller
- IoT Camera
- IoT DoorLock

You should start 4 instances parallel.

Instance 1

```
mosquitto
```

Instance 2

```
python3 iot_controller.py
```

Instance 3

```
python3 iot_client_doorlock.py
```

Instance 4

```
python3 iot_client_camera.py
```

Then, start publishing the message to test the response. Please follow "IoT  Doorlock MQTT Publish" to see how to test.

# Virtualization

if you need a virtualization, you can use `venv`.

```
python3 -m venv pymyenv
. pymyenv/bin/activate
```

# IoT Client Doorlock MQTT Subscribe

```
python iot_client_doorlock.py
```

# IoT Doorlock MQTT Publish

```
Usage: iot_publish_doorlock.py <Host> <Request>
```
Publish Open Request Sample
```
python iot_publish_doorlock.py localhost Open
```

Publish Close Request Sample
```
python iot_publish_doorlock.py localhost Close
```

# How to force authentication on Mosquitto

1. Run `mosquitto_passwd -c file_name user_name `
2. `vim mosquitto.conf` and add the following lines

```
listener 1883
allow_anonymous false
password_file ./filename
```

3. run `mosquitto -c mosquitto.conf`

# How to do perf test

## Prerequisite

- MacOS: You need to install the following libraries to pass `make install`
  - `brew install postgresql`
  - `brew install librdkafka`
  - if M1 then run either of the following:
    - `C_INCLUDE_PATH=/opt/homebrew/Cellar/librdkafka/1.8.2/include LIBRARY_PATH=/opt/homebrew/Cellar/librdkafka/1.8.2/lib pip install confluent_kafka`
    - `CPATH=/opt/homebrew/Cellar/librdkafka/1.8.2/include pip install confluent-kafka`
    - Ref: [confluent-kafka-python github issue](https://github.com/confluentinc/confluent-kafka-python/issues/1190)

## How to run perf test

1. run `locust`
2. Open `http://0.0.0.0:8089/` on your browser
3. Set the values and start the test

# How to contribute

To contribute to this project, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
<!-- 3. Make your changes and check with: `make check` -->
4. Commit them: `git commit -m '<commit_message>'`
5. Push to the original branch: `git push origin ShotaKameyama/ssa_iot`
6. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
