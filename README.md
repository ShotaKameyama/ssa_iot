# Prerequisite

The following should be installed already before setup.
- Python3

# Getting Started

```
git clone https://github.com/ShotaKameyama/ssa_iot.git
```

## MacOS

```
brew install mosquitto
make install
```

## Linux


## Windows

## Virtualization

```
python3 -m venv pymyenv
. pymyenv/bin/activate
make install
```


# How to force authentication on Mosquitto

1. Run `mosquitto_passwd -c file_name user_name `
2. `vim mosquitto.conf` and add the following lines

```
allow_anonymous false
password_file ./filename
```

3. run `mosquitto -c mosquitto.conf`

# How to contribute

To contribute to this project, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
<!-- 3. Make your changes and check with: `make check` -->
4. Commit them: `git commit -m '<commit_message>'`
5. Push to the original branch: `git push origin ShotaKameyama/ssd_u6`
6. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).