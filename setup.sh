#!/bin/bash

# prompt to input env variables. 
echo
read -rep "Enter MQTT host (e.g. localhost, 10.54.34.89): " host
read -rep "Enter MQTT port (e.g. 1883): " port
read -rep "Enter client_lock username for authentication (e.g. client_lock): " client_lock
read -s -p "Enter client_lock password: " client_lock_pass
echo
read -rep "Enter client_camera username for authentication (e.g. client_camera): " client_camera
read -s -p "Enter client_camera password: " client_camera_pass
echo
read -rep "Enter controller username for authentication (e.g. controller): " controller
read -s -p "Enter controller password: " controller_pass
echo

# input env variables into bash_profile
echo "export MQTT_HOST=${host}" >> ~/.bash_profile
echo "export MQTT_PORT=${port}" >> ~/.bash_profile
echo "export CLIENT_LOCK_USER=${client_lock}" >> ~/.bash_profile
echo "export CLIENT_LOCK_PASSWORD=${client_lock_pass}" >> ~/.bash_profile
echo "export CLIENT_CAMERA_USER=${client_camera}" >> ~/.bash_profile
echo "export CLIENT_CAMERA_PASSWORD=${client_camera_pass}" >> ~/.bash_profile
echo "export CONTROLLER_USER=${controller}" >> ~/.bash_profile
echo "export CONTROLLER_PASSWORD=${controller_pass}" >> ~/.bash_profile
source ~/.bash_profile

# Summary
echo "MQTT host: ${host}"
echo "MQTT port: ${port}"
echo "client_lock username for authentication: ${client_lock}"
echo "client_lock password: ${client_lock_pass}"
echo "client_camera username for authentication: ${client_camera}"
echo "client_camera password: ${client_camera_pass}"
echo "controller username for authentication: ${controller}"
echo "controller password: ${controller_pass}"

echo "All Set! if you need to edit, please run the same script again or edit ~/.bash_profile."

# Create ACL file
echo "------ Create ACL File Start -------"
echo "Creating an access control file"
touch ./config/mosquitto.acl
echo "user ${controller}" >> ./config/mosquitto.acl
echo "topic read device/${client_lock}/message/${controller}" >> ./config/mosquitto.acl
echo "topic read device/${client_camera}/message/${controller}" >> ./config/mosquitto.acl
echo "topic write device/${controller}/order/${client_lock}" >> ./config/mosquitto.acl
echo "topic write device/${controller}/order/${client_camera}" >> ./config/mosquitto.acl
echo "" >> ./config/mosquitto.acl

echo "user ${client_lock}" >> ./config/mosquitto.acl
echo "topic read device/${controller}/order/${client_lock}" >> ./config/mosquitto.acl
echo "topic write device/${client_lock}/message/${controller}" >> ./config/mosquitto.acl
echo "" >> ./config/mosquitto.acl

echo "user ${client_camera}" >> ./config/mosquitto.acl
echo "topic read device/${controller}/order/${client_camera}" >> ./config/mosquitto.acl
echo "topic write device/${client_camera}/message/${controller}" >> ./config/mosquitto.acl
echo "Created an access control file. Please look at ./config/mosquitto.acl"
echo "------ Create ACL File End -------"

# Create Mosquitto User
echo "------ Create Mosquitto User Start -------"
echo "Creating a Mosquitto user file"
mosquitto_passwd -c -b ./config/mosquitto.pass $controller $controller_pass
mosquitto_passwd -b ./config/mosquitto.pass $client_lock $client_lock_pass
mosquitto_passwd -b ./config/mosquitto.pass $client_camera $client_camera_pass
echo "Created a Mosquitto user file. Please look at ./config/mosquitto.pass"
echo "------ Create Mosquitto User END -------"
echo "------ Create Mosquitto Config File Start -------"
touch ./config/mosquitto.conf
echo "listener ${port}" >> ./config/mosquitto.conf
echo "allow_anonymous false" >> ./config/mosquitto.conf
echo "password_file ./config/mosquitto.pass" >> ./config/mosquitto.conf
echo "acl_file ./config/mosquitto.acl" >> ./config/mosquitto.conf
echo "------ Create Mosquitto Config File End -------"
echo "====== ALL OPERATION DONE ======"