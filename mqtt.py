
import paho.mqtt.client as mqtt

# Configurações do Broker MQTT
BROKER_IP = 'IP_SENSOR'  # Substitua pelo IP do seu broker MQTT
BROKER_PORT = 1883            # Porta padrão do MQTT
TOPIC = 'devices/nome_sensor/sensor/temperature' # Substitua pelo tópico que você está monitorando

# Função chamada quando uma mensagem é recebida
def on_message(client, userdata, message):
    payload = message.payload.decode()
    print(f"Recebido valor do sensor de temperatura: {payload}")

# Configuração do cliente MQTT
client = mqtt.Client()

# Definindo a função de callback
client.on_message = on_message

try:
    # Conectar ao broker
    print(f"Conectando ao broker MQTT em {BROKER_IP}:{BROKER_PORT}...")
    client.connect(BROKER_IP, BROKER_PORT, 60)

    # Inscrever-se no tópico
    print(f"Inscrevendo-se no tópico '{TOPIC}'...")
    client.subscribe(TOPIC)

    # Manter a conexão e aguardar mensagens
    print("Aguardando mensagens...")
    client.loop_forever()

except KeyboardInterrupt:
    # Encerrar a conexão em caso de interrupção (Ctrl+C)
    print("Interrompido pelo usuário. Desconectando...")
    client.disconnect()

except Exception as e:
    # Captura e exibe qualquer erro
    print(f"Erro: {e}")

~
