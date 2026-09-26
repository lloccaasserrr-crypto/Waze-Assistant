import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def ask_ollama(question):
    payload = {
        "model": MODEL,
        "prompt": question,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "Нет ответа от модели.")
    except Exception as e:
        return f"Ошибка: {e}. Убедись, что Ollama запущена и модель установлена."

print("Привет! Я Waze. Напиши 'выход', чтобы закрыть программу.")

while True:
    user_input = input("Ты: ")

    if user_input.strip().lower() in ["выход", "exit", "quit"]:
        print("Waze: Пока!")
        break

    prompt = f"""
Ты — Waze, персональный AI-помощник.
Отвечай кратко, понятно и по-русски.
Пользователь спрашивает: {user_input}
"""
    answer = ask_ollama(prompt)
    print(f"Waze: {answer}")
