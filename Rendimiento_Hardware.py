import psutil

def obtener_porcentaje_uso_cpu():
    porcentaje = psutil.cpu_percent(interval=1)  # Lee el porcentaje de uso de la CPU durante 1 segundo
    return porcentaje

if __name__ == "__main__":
    while True:
        porcentaje_uso_cpu = obtener_porcentaje_uso_cpu()
        print(f"Porcentaje de uso de CPU: {porcentaje_uso_cpu}%")
        import psutil

def obtener_porcentaje_uso_cpu():
    porcentaje = psutil.cpu_percent(interval=1)  # Lee el porcentaje de uso de la CPU durante 1 segundo
    return porcentaje

if __name__ == "__main__":
    while True:
        porcentaje_uso_cpu = obtener_porcentaje_uso_cpu()
        print(f"Porcentaje de uso de CPU: {porcentaje_uso_cpu}%")
        from memory_profiler import profile

@profile
def my_function():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == "__main__":
    my_function()
    
    import psutil
import time

def monitor_network(interval=1, duration=10):
    print("Monitoring network performance...")

    end_time = time.time() + duration

    while time.time() < end_time:
        net_stats = psutil.net_io_counters()
        print(f"Bytes enviados: {net_stats.bytes_sent} | Bytes recibidos: {net_stats.bytes_recv}")
        time.sleep(interval)

if __name__ == "__main__":
    monitor_network()
    
    import psutil
import os
import time

def monitor_cpu(interval=1, duration=10):
    print("Monitoring CPU performance...")

    end_time = time.time() + duration

    while time.time() < end_time:
        cpu_percent = psutil.cpu_percent(interval=interval)
        print(f"Uso de CPU: {cpu_percent}%")
        time.sleep(interval)

if __name__ == "__main__":
    monitor_cpu()
        
