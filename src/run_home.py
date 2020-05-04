import os
from tools import load_config
import subprocess
import time
from co2 import get_co2

def get_ip_and_token(tool, config):
    return config[tool]['ip'], config[tool]['token']


def run_command(params, command):
    cmd = f"""miplug --ip {params[0]} --token {params[1]} {command}"""
    print(cmd)
    subprocess.run(cmd.split(' '))
 
PROJECT_PATH = os.path.abspath(os.getcwd())
#PROJECT_PATH = '/users/test/Documents/proj_smart_home'
CONFIG_PATH = 'configs'
config = load_config(os.path.join(PROJECT_PATH, CONFIG_PATH, 'tokens.yaml'))

for i in config.keys():
    globals()[i] = get_ip_and_token(i, config)

print(floor_lamp, humidifier, recirculator, chandelier_1, chandelier_2)
co2 = get_co2()
print(co2)
# run_command(humidifier, 'on')
# time.sleep(7)
# run_command(humidifier, 'off')
