from sensors.dht11 import DHT11
from sensors.mcp3008 import MCP3008
import RPi.GPIO
import time
import threading
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json, os

class Sensors:


    def __init__(self):
        self.kafka_url = os.getenv("CX_KAFKA_URL")
        RPi.GPIO.setwarnings(False)
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        self.dht_instance = DHT11(18)
        self.mcp3008_instance = MCP3008(16)
        self.producer = KafkaProducer(bootstrap_servers=self.kafka_url,value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def start_temp(self):
        while True:
            dht = self.dht_instance.read_temp()
            if(dht['temperature']>-99):
                self.producer.send('temperature', value=dht)
                # read the temperature every 10 minutes.
                time.sleep(600)
            else:
                # keep polling until a temperature is correctly read
                time.sleep(3)

    def start_dust(self):
        while True:
            dust = self.mcp3008_instance.read_dust()
            if(dust['density']>=0):
                self.producer.send('dust', value=dust)
                #print(f'Dust: {dust}', end='\r')
            time.sleep(0.5)

    def start_noise(self):
        while True:
            noise = self.mcp3008_instance.read_noise()
            self.producer.send('noise', value=noise)
            # print(f'Noise:{noise}', end='\r')
            time.sleep(0.0001)

    def start(self):
        t_1 = threading.Thread(target=self.start_temp)
        t_2 = threading.Thread(target=self.start_dust)
        t_3 = threading.Thread(target=self.start_noise)
        t_1.start()
        t_2.start()
        t_3.start()

        t_1.join()
        t_2.join()
        t_3.join()
        print('Threads started')


s = Sensors()
s.start()
