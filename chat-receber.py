import os
from datetime import datetime

from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

os.environ["pubsub_uuid"] = "LAPTOP-Dalazen"

pnconfig = PNConfiguration()
pnconfig.publish_key = os.getenv("pubsub_pub")
pnconfig.subscribe_key = os.getenv("pubsub_sub")
pnconfig.uuid = os.getenv("pubsub_uuid")

canal = "imedccso"

pubnub = PubNub(pnconfig)


class RecebeMensagem(SubscribeCallback):
    def presence(self, pubnub, event):
        pass

    def status(self, pubnub, event):
        pass

    def message(self, pubnub, event):
        print("{}: {}\n{}".format(event.message["usr"], event.message["msg"], datetime.now().strftime("%H:%M:%S")))


pubnub.add_listener(RecebeMensagem())
pubnub.subscribe().channels(canal).with_presence().execute()
