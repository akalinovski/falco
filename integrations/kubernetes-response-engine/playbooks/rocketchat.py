import sys
import os.path
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__))))
import os
import requests
import json
import playbooks
from playbooks import infrastructure

playbook = playbooks.AddMessageToRocketChat(
    infrastructure.RocketChatClient("http://rocketchat-rocketchat.cicd-tools:3000")
)

def handler(event, context):
    playbook.run(event['data'])
