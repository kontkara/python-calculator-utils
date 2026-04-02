import os
import time
import random
import re
import subprocess
from datetime import datetime

TARGET_FILE = "calculator.py"

def ask_local_ai(prompt, current_code):
    full_prompt = f"{prompt}\n\nCurrent code:\n{current_code}"
    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama3', full_prompt],
            capture_output=True, text=True
        )
        return result.stdout
    except Exception as e:
        print(f"Ollama hatası: {e}")
        return ""

def extract_code(llm_output):
    # 1. İhtimal: Markdown bloğu kullanmışsa yakala
    match = re.search(r'```[a-zA-Z]*\n(.*?)\n```', llm_output, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # 2. İhtimal: Markdown kullanmamış ama direkt kod yazmışsa
    if "def " in llm_output or "import " in llm_output or "class " in llm_output:
        lines = llm_output.split('\n')
        # Gevezelikleri temizle
        code_lines = [line for line in lines if not line.lower().startswith(("here is", "sure", "i added", "this code", "note:", "```"))]
        return "\n".join(code_lines).strip()
        
    return None

def run():
    if not os.path.exists(TARGET_FILE):
        with open(TARGET_FILE, "w") as f:
            f.write("def add(a, b):\n    return a + b\n")
    
    prompt = open("agent_prompt.txt").read()

    while True:
        daily_commits = random.randint(1, 3)
        print(f"[{datetime.now().strftime('%H:%M')}] Bugün {daily_commits} adet iş (commit) yapılacak.")

        for i in range(daily_commits):
            with open(TARGET_FILE, "r") as f:
                current_code = f.read()

            output = ask_local_ai(prompt, current_code)
            valid_code = extract_code(output)

            if valid_code and len(valid_code) > 20:
                with open(TARGET_FILE, "w") as f:
                    f.write(valid_code)

                commit_msgs = [
                    "Refactored calculator logic", 
                    "Added error handling routines", 
                    "Improved type hinting and docs", 
                    "Optimized main functions", 
                    "Cleaned up redundant code"
                ]
                msg = random.choice(commit_msgs)
                
                os.system("git add .")
                os.system(f'git commit -m "{msg}"')
                os.system("git push origin main")
                print(f"[{datetime.now().strftime('%H:%M')}] Başarılı: '{msg}' commiti atıldı.")
            else:
                # EĞER HATA VERİRSE LLAMA'NIN NE DEDİĞİNİ EKRANA BASACAK
                print("\n--- DİKKAT: Geçerli kod bulunamadı ---")
                print(f"Llama 3'ün ham cevabı:\n{output[:300]}...\n---------------------------------------")
                print("Bu adım atlandı.\n")

            if i < daily_commits - 1:
                pause = random.randint(2700, 10800)
                print(f"Mola veriliyor... {pause//60} dakika sonra devam edilecek.")
                time.sleep(pause)

        sleep_until_tomorrow = random.randint(50400, 72000)
        print(f"Günlük mesai bitti. {sleep_until_tomorrow//3600} saat uyunuyor...")
        time.sleep(sleep_until_tomorrow)

if __name__ == "__main__":
    run()
