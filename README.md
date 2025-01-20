# python_mqtt_zabbix
Script Python para coleta de dados via Protocolo MQTT + Zabbix.

O script foi desenvolvido através da necessidade de monitorar as métricas de temperatura de uma sala de servidores, utilizando um Arduino como dispositivo de coleta de dados.

**Depêndencias: 
Broker configurado no seu sensor IoT.

**biblioteca paho.mqtt.client**

Instalação:
*pip install paho-mqtt*

*pip show paho-mqtt*
```
Name: paho-mqtt
Version: 2.1.0
Summary: MQTT version 5.0/3.1.1 client class
Home-page:
Author:
Author-email: Roger Light <roger@atchoo.org>
License: EPL-2.0 OR BSD-3-Clause
Location: /usr/local/lib/python3.9/site-packages
Requires:
Required-by:

```

Local do Script MQTT.py: */lib/zabbix/externalscripts*

Item Zabbix:

![Title](item.png)





