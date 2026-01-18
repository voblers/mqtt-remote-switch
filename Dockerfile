FROM python:3-alpine

ADD VERSION .

# Set args for the program
ARG MQTT_HOSTNAME=mqtt
ARG MQTT_USERNAME=mqtt

ARG MQTT_REMOTE_TOPIC
ARG MQTT_REMOTE_ACTION=single

ARG MQTT_SWITCH_TOPIC
ARG MQTT_SWITCH_ACTION="{'state': 'toggle'}"

# Install paho python library
RUN pip install paho-mqtt

# Set workdir
WORKDIR /app

# Copy onver the python script
COPY src/ToggleSwitch.py .

CMD ["python", "-u", "ToggleSwitch.py"]
