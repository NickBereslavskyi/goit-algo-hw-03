import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Копіювання і сортування файлів за розширенням")
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()

def copy_and_sort_files(source, destination):
    try:
        if not os.path.exists(source):
            raise FileNotFoundError(f"Директорія '{source}' не існує.")

        for item in os.listdir(source):
            full_path = os.path.join(source, item)
            if os.path.isdir(full_path):
                # Рекурсивно обробити піддиректорії
                copy_and_sort_files(full_path, destination)
            elif os.path.isfile(full_path):
                try:
                    ext = os.path.splitext(item)[1].lower().lstrip('.')
                    if not ext:
                        ext = "no_extension"
                    target_dir = os.path.join(destination, ext)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.copy2(full_path, target_dir)
                    print(f"[+] Копійовано: {full_path} → {target_dir}")
                except Exception as file_error:
                    print(f"[!] Помилка копіювання файлу '{full_path}': {file_error}")
    except Exception as dir_error:
        print(f"[!] Помилка при доступі до директорії '{source}': {dir_error}")

def main():
    args = parse_arguments()
    copy_and_sort_files(args.source, args.destination)
    print("\n Завершено.")

if __name__ == "__main__":
    main()


# Як запустити:
# python Copy_sort.py /шлях/до/вихідної/директорії /шлях/до/папки/призначення