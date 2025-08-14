import subprocess
from datetime import datetime

command = "yfm"
input_dir = r"source"
output_dir = r"miniature-painting"
log_file = "build_log.txt" 

def write_log(message, mode='w'):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, mode, encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

write_log(f"Начало выполнения команды: {' '.join([command, '-i', input_dir, '-o', output_dir])}")

try:

    result = subprocess.run(
        [command, "-i", input_dir, "-o", output_dir],
        check=True,
        shell=True,
        text=True,
        capture_output=True
    )
    
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Команда выполнена успешно!\n")
        f.write(f"Вывод:\n{result.stdout}\n")
    
    print("Команда выполнена успешно!")
    print(f"Вывод:\n{result.stdout}")

except subprocess.CalledProcessError as e:
    error_msg = f"Ошибка выполнения: {e}\nОшибка:\n{e.stderr}"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {error_msg}\n")
    print(error_msg)

except Exception as e:
    error_msg = f"Критическая ошибка: {type(e).__name__}: {e}"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {error_msg}\n")
    print(error_msg)

finally:
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Завершение работы\n")
    print(f"\nЛог сохранён в {log_file} (перезаписан)")