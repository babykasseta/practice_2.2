import psutil
import time

while True:
    #загрузка CPU (в процентах)
    cpu_usage = psutil.cpu_percent(interval=1)

    #использование оперативной памяти
    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    #использование диска
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    print(f"CPU: {cpu_usage}%")
    print(f"RAM: {memory_usage}%")
    print(f"Disk: {disk_usage}%")
    print("-" * 20)

    time.sleep(2)