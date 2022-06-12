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
git clone https://github.com/ShotaKameyama/ssa_iot.git
cd ssa_iot
make install
```

## Setup env variables and mosquitto config files.

As we use access controll using username and password, hence we use env variables to avoid info leakage by the source code.

```
chmod +x setup.sh 
./setup.sh
```

This shell script will take care of the following:
1. Create Mosquitto Access Control List File: `./config/mosquitto.acl`
2. Create Mosquitto User Credential File: `./config/mosquitto.pass`
3. Create Mosquitto Config File: `./config/mosquitto.conf`
4. Add Environment Variables to `~/.bash_profile`


# Basic Information

This IoT system consists of 4 instances:
- MQTT broker
- IoT Controller
- IoT Camera
- IoT DoorLock

You should start 4 instances parallel.

Instance 1
```
brew install librdkafka

make install

git log
git pull

mosquitto -c config/mosquitto.conf

```

Instance 2
```
cd ssa_iot

source ~/.bash_profile

python3 iot_controller.py
```

Instance 3
```
cd ssa_iot 

source ~/.bash_profile

python3 iot_client_doorlock.py
```

Instance 4
```
First run these commands:

pip install pyaml-env

pip install pyzbar

brew install zbar

vim config/config.yml

brew install opencv 
(This command can take some time to install, please be patient)

python3 iot_client_camera.py
```

## How to read QR code?

Once you configured 4 instances, then you can start reading qr code using your USB camera.

```
python3 qr_read.py
```

Then read a qr file under `static/qr` 

## IoT Doorlock MQTT Publish

Alternatively, you can do the following to do the same.

```
Usage: iot_publish_doorlock.py <Request>
```
Publish Open Request Sample
```
python iot_publish_doorlock.py Open
```

Publish Close Request Sample
```
python iot_publish_doorlock.py Close
```


# Virtualization

if you need a virtualization, you can use `venv`.

```
python3 -m venv pymyenv
. pymyenv/bin/activate
```

# How to force authentication on Mosquitto

1. run `mosquitto -c mosquitto.conf`

if you don't have the `mosquitto.conf` file, make sure that you have run `./setup.sh`.

# How to enable TLS on Mosquitto

Requirement:
Certificate Authority (CA) server – OpenSSL for the self-sign certificate in this case. It could be signed by an online CA server for the public trust certificate.

## In the CA server:
Generate a CA server key pair with password protection.
```
openssl genrsa -des3 -out ca.key 4096
```
Request the certificate with the required information, including Country Name, State, Locality, Organization, Unit Name, CA server hostname (Common Name) and Email address.
```
openssl req -x509 -new -key ca.key -sha256 -days 365 -out ca.crt
```
## In the Broker server:
Generate a broker server key pair with password protection.
```
openssl genrsa -out server.key 4096
```
Request the certificate with the required information, including Country Name, State, Locality, Organization, Unit Name, broker server hostname (Common Name) and Email address.
```
openssl req -new -key server.key -sha256 -days 365 -out server.csr
```
## In the CA server (self-sign):
Copy the request file server.csr to the CA server to verify and sign the certificate.
```
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365 -sha256
```
## In the Broker server
Copy the signed certificate file server.crt and CA server certificate ca.crt to the Broker server to the Keystore. Update the mosquito configuration file and the related IoT device to use TLS for the MQTT transaction.


# How to run tests

## Test Report Repository

The exported documents are published below:
- Locust Result at [static/reports/locust_report](https://shotakameyama.github.io/ssa_iot/static/reports/locust_report)
- Flake8 result at [static/reports/flake8_report](https://shotakameyama.github.io/ssa_iot/static/reports/flake8_report)
- Bandit result at [static/reports/bandit_report](https://shotakameyama.github.io/ssa_iot/static/reports/bandit_report)


## Guide Enforcement & SAST

PyLint/Flake8/Bandit are used for the test.

```
make lint
make flake8
make bandit
```

## Perf Test

1. run `locust`
2. Open `http://0.0.0.0:8089/` on your browser
3. Set the values and start the test

### Prerequisite

- MacOS: You need to install the following libraries to pass `make install`
  - `brew install postgresql`
  - `brew install librdkafka`
  - `brew install zbar`
  - if M1 then run either of the following:
    - `C_INCLUDE_PATH=/opt/homebrew/Cellar/librdkafka/1.8.2/include LIBRARY_PATH=/opt/homebrew/Cellar/librdkafka/1.8.2/lib pip install confluent_kafka`
    - `CPATH=/opt/homebrew/Cellar/librdkafka/1.8.2/include pip install confluent-kafka`
    - Ref: [confluent-kafka-python github issue](https://github.com/confluentinc/confluent-kafka-python/issues/1190)
    - ` mkdir ~/lib && ln -s $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib`


# How to contribute

To contribute to this project, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and check with: `make check`
4. Commit them: `git commit -m '<commit_message>'`
5. Push to the original branch: `git push origin <branch>`
6. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
