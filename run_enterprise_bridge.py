# -*- coding: utf-8 -*-
import sys
import time
import threading
from colorama import init, Fore
from bridge_modules.minecraft_chunk_corruptor import corrupt_minecraft_chunks
from bridge_modules.gta_physics_nightmare import spawn_gta_vehicle_on_rails
from bridge_modules.satisfactory_conveyor_hell import start_conveyor_belt_panic

init(autoreset=True)

def cpu_meltdown_thread():
    """Фоновый поток: создает видимость того, что мост обрабатывает гигабайты данных"""
    while True:
        _ = [math_op ** 3 for math_op in range(200000)]
        time.sleep(0.02)

if __name__ == "__main__":
    heater = threading.Thread(target=cpu_meltdown_thread, daemon=True)
    heater.start()

    print(Fore.RED + "=" * 75)
    print(Fore.YELLOW + "🌉 MINECRAFT x GTA x SATISFACTORY MULTIVERSE BRIDGE v99.9-BETA 🚀")
    print(Fore.RED + "=" * 75)
    
    server_ip = input(Fore.GREEN + "Введите IP сервера для взлома (или 'говно'): ")
    if not server_ip:
        server_ip = "127.0.0.1:666"
        
    print(Fore.CYAN + f"\n[BRIDGE] Подключение к квантовому шлюзу {server_ip}...")
    time.sleep(1.0)
    
    # Запускаем адский конвейер модулей
    corrupt_minecraft_chunks()
    spawn_gta_vehicle_on_rails()
    start_conveyor_belt_panic()
    
    print(Fore.RED + "-" * 75)
    print(Fore.GREEN + "✅ МОСТ УСПЕШНО ПОСТРОЕН! Стив везет медь на тракторе из GTA по конвейеру в ад.")
    print(Fore.MAGENTA + "⚠️ ВНИМАНИЕ: Ваш компьютер начал пахнуть паленым пластиком.")
    print(Fore.RED + "=" * 75)
