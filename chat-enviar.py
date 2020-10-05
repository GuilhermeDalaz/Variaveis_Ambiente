import os

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

os.environ["pubsub_uuid"] = "feerposser-pc"

pnconfig = PNConfiguration()
pnconfig.publish_key = os.getenv("pubsub_pub")
pnconfig.subscribe_key = os.getenv("pubsub_sub")
pnconfig.uuid = os.getenv("pubsub_uuid")

canal = "imedccso"
usr = input("Seu nome: ")
print("-"*50)

pubnub = PubNub(pnconfig)

while True:
    msg = input("Fala ae: ")
    envelope = pubnub.publish().channel(canal).message({"msg": msg, "usr": usr}).sync()

    if envelope.status.is_error():
        print("->>>>> DEU PAU")
