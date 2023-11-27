import psutil

def obtener_porcentaje_uso_cpu():
    porcentaje = psutil.cpu_percent(interval=1)  # Lee el porcentaje de uso de la CPU durante 1 segundo
    return porcentaje

if __name__ == "__main__":
    while True:
        porcentaje_uso_cpu = obtener_porcentaje_uso_cpu()
        print(f"Porcentaje de uso de CPU: {porcentaje_uso_cpu}%")
        