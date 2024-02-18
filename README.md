# MQTT Toggle Switch Automation

This repository contains a Python script and a Dockerfile to create a Docker image for a simple MQTT toggle switch automation. The application uses the Paho MQTT library to interact with an MQTT broker and toggle a switch based on incoming messages from a remote switch.

I have developed a simple application to ensure smooth and uninterrupted operation between a wall switch and a remote switch. Binding them together via Zigbee is not possible, and using a Home Assistant automation introduces the risk of automation not working during updates or system failures. This script runs on the same machine as the Zigbee network, minimizing downtime risks.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Docker Image](#docker-image)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Prerequisites

Ensure you have Docker installed on your system.

## Docker Image

The Docker image is configured to run the MQTT Toggle Switch application. It includes the necessary dependencies and sets up the environment for the Python script.

To build the Docker image:

```bash
docker build -t mqtt-toggle-switch .
```

To run the Docker container:

```bash
docker run -e MQTT_USERNAME=<your_username> -e MQTT_PASSWORD=<your_password> -e MQTT_REMOTE_TOPIC=<remote_topic> -e MQTT_SWITCH_TOPIC=<switch_topic> mqtt-toggle-switch
```

## Usage

The ToggleSwitch.py script subscribes to specified MQTT topics and toggles a switch based on incoming messages. It continuously listens for messages in the MQTT broker and reacts accordingly.

## Configuration

The behavior of the MQTT Toggle Switch can be customized using environment variables in the Dockerfile. Here are the available configuration options:
- **MQTT_HOSTNAME**: MQTT broker hostname (default: mqtt).
- **MQTT_PORT**: MQTT broker port (default: 1883).
- **MQTT_USERNAME**: MQTT broker username (required).
- **MQTT_PASSWORD**: MQTT broker password (required).
- **MQTT_REMOTE_TOPIC**: MQTT topic to subscribe to for remote actions (comma-separated if multiple).
- **MQTT_REMOTE_ACTION**: Comma-separated list of remote actions to trigger the switch.
- **MQTT_SWITCH_TOPIC**: MQTT topic to publish switch actions (comma-separated if multiple).
- **MQTT_SWITCH_ACTION**: JSON payload to send when toggling the switch.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
