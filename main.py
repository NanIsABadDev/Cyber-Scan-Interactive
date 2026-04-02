import random
import time

print("Servidor iniciado...")
time.sleep(2)

print("Aguardando sinal de dispositivo...\n")
time.sleep(2)

# sinal inicial (detecção do IP)
print("Sinal detectado!")
print("Identificando dispositivo...")
time.sleep(random.uniform(1, 2))

print("Obtendo informações de rede...\n")
time.sleep(random.uniform(1, 2))

# geração do IP fake
ip_fake = "192.168." + str(random.randint(0,255)) + "." + str(random.randint(1,254))

# infos fake do dispositivo
porta = random.randint(1000, 9999)
status = "ONLINE"
tempo_resposta = round(random.uniform(1, 100), 2)

# resultado final (diagnóstico)
print("=== DISPOSITIVO IDENTIFICADO ===")
print("IP:", ip_fake)
print("Porta:", porta)
print("Status:", status)
print("Tempo de resposta:", tempo_resposta, "ms")
print("Protocolo: TCP/IP")
print("Segurança: Autenticação necessária")
print("=======================aa========")
