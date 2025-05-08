import logging
from azure.iot.device import IoTHubDeviceClient, Message
import time
import random

# Substitua pela sua connection string do dispositivo gerado no IoT Hub
CONNECTION_STRING = "HostName=iothub-soda-vision-dev-scus-001.azure-devices.net;DeviceId=vm-op-0001;SharedAccessKey=8I7ryxGzxedZhSCyYfCunb6D+F8R9WpNSAIoTGVv/SY="

# Ativar logs detalhados para o MQTT
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def main():
    # Cria o cliente de dispositivo
    device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print("Conectando ao Azure IoT Hub...")
    try:
        device_client.connect()
        print("Conectado!")
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        logger.exception("Erro ao conectar ao IoT Hub")
        return

    try:
        while True:
            temperatura = round(random.uniform(20.0, 30.0), 2)
            mensagem = Message(f"Temperatura: {temperatura}°C")
            mensagem.content_encoding = "utf-8"
            mensagem.content_type = "text/plain"

            print(f"Enviando mensagem: {mensagem}")
            device_client.send_message(mensagem)
            time.sleep(5)

    except KeyboardInterrupt:
        print("Encerrando conexão...")

    finally:
        device_client.shutdown()

if __name__ == "__main__":
    main()
