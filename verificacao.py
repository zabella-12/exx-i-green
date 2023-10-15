import psutil
import time

# Função para obter informações de energia
def get_energy_info():
    # Use psutil para obter informações de energia
    battery = psutil.sensors_battery()
    if battery is not None:
        percent = battery.percent
        power_plugged = battery.power_plugged
        print(f"Status da Bateria: {'Conectada' if power_plugged else 'Desconectada'}")
        print(f"Nível de Bateria: {percent}%")
        time.sleep(10) 
    else:
        print("Informações da bateria não disponíveis neste sistema.")

# Função para monitorar o tempo de execução do sistema
def monitor_system_runtime():
    while True:
        uptime = time.time() - psutil.boot_time()
        print(f"Tempo de Execução do Sistema: {uptime / 3600:.2f} horas")
        time.sleep(60)  # Atualizar a cada minuto

# Função para monitorar o uso da rede
def monitor_network_usage():
    while True:
        net_io = psutil.net_io_counters()
        sent = net_io.bytes_sent
        received = net_io.bytes_recv
        print(f"Uso de Rede - Enviado: {sent / (1024 * 1024):.2f} MB | Recebido: {received / (1024 * 1024):.2f} MB")
        time.sleep(60)  # Atualizar a cada minuto

if __name__ == "__main__":
    # Inicie as funções de monitoramento em threads separadas
    import threading

    energy_thread = threading.Thread(target=get_energy_info)
    system_runtime_thread = threading.Thread(target=monitor_system_runtime)
    network_usage_thread = threading.Thread(target=monitor_network_usage)

    energy_thread.start()
    system_runtime_thread.start()
    network_usage_thread.start()

    # Aguarde as threads para sempre manter o monitoramento ativo
    energy_thread.join()
    system_runtime_thread.join()
    network_usage_thread.join()
