import json
import requests
from pathlib import Path

URL = "https://www.andybek.com/api/data/books"
ORIGINAL = Path("books-original.json")
CLEANED = Path("books-cleaned.json")

def main():
    # 1) Descargar datos
    resp = requests.get(URL, timeout=15)
    resp.raise_for_status()
    data = resp.json()  # debería ser una lista de dicts

    # 2) Guardar original
    with ORIGINAL.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # 3) Limpiar: quitar claves pedidas
    keys_to_remove = ("ranks", "release dates", "release_dates")
    if isinstance(data, list):
        for book in data:
            if isinstance(book, dict):
                for k in keys_to_remove:
                    book.pop(k, None)

    # 4) Guardar limpio
    with CLEANED.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Listo.\n- Original: {ORIGINAL.resolve()}\n- Limpio:   {CLEANED.resolve()}")

if __name__ == "__main__":
    main()
