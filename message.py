import os
from slackclient import SlackClient
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
slack_client = SlackClient(SLACK_TOKEN)

my_channel_id = 'C97L01PHN'

def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None

def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None

def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='pythonbot',
        icon_emoji=':robot_face:'
    )


if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Authenticated")
        send_message(my_channel_id, "HELLO , it works")
    else:
        print("Unable to authenticate.")
