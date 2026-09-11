import json
import os
import subprocess

# Путь к папке, куда скачан branch `rule-sets`
PUBLISH_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../publish'))

def process_rule_set(name: str, rules_list: list):
    """
    Принимает имя файла (без расширения) и список правил.
    Сравнивает с текущим JSON. Если есть изменения — компилирует SRS.
    """
    os.makedirs(PUBLISH_DIR, exist_ok=True)

    json_path = os.path.join(PUBLISH_DIR, f"{name}.json")
    srs_path = os.path.join(PUBLISH_DIR, f"{name}.srs")

    new_data = {
        "version": 2,
        "rules": rules_list
    }

    # Сравнение с существующим файлом
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            try:
                old_data = json.load(f)
                if old_data == new_data:
                    print(f"[{name}] Unchanged. Skipping compilation.")
                    return
            except json.JSONDecodeError:
                pass # Если файл поврежден, перезапишем его

    print(f"[{name}] Changes detected. Updating JSON and compiling SRS...")

    # Сохраняем новый JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=2, ensure_ascii=False)

    # Компилируем SRS через системный вызов
    result = subprocess.run(
        ["sing-box", "rule-set", "compile", json_path, "-o", srs_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"[{name}] Error compiling SRS: {result.stderr}")
        # Выбрасываем исключение, чтобы GitHub Actions отметил этот шаг как Failed
        raise RuntimeError(f"Failed to compile {name}.srs")

    print(f"[{name}] Success!")
