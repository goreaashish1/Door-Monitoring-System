from datetime import timedelta
import time

from timeloop import Timeloop

from gateway_client import get_gateway_cilent, send_status_event, send_android_device_event
from udp_listener import listen_sensor_data


client = get_gateway_cilent('gateway_config.yml')
client.connect()
time.sleep(2)
tl = Timeloop()

devices_data = {}


@tl.job(interval=timedelta(seconds=5))
def send_gateway_status():
    send_status_event(client)


@tl.job(interval=timedelta(milliseconds=200))
def send_device_readings():
    for device_addr, data in devices_data.items():
        send_android_device_event(client, device_addr, "status", data)
    devices_data.clear()


def gateway_command_callback(cmd):
    print("Command received for {}:{}: {}".format(cmd.typeId, cmd.deviceId, cmd.data))
    if cmd.typeId == 'reset':
        reset_data(devices_data)
    else:
        print("Unknown command type received")


def reset_data():
    devices_data.clear()
    # Add more custom logic here.
    pass


tl.start()

# Subscribing to commands
client.subscribeToCommands(commandId="reset")
# Registering a callback
client.commandCallback = gateway_command_callback


for data, device_addr in listen_sensor_data():
    devices_data[device_addr[0]] = data
