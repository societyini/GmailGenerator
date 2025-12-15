import random
import string
import configparser
import os
import time

# =========================
# COLORES
# =========================
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# =========================
# BANNER
# =========================
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Colors.CYAN}{Colors.BOLD}
   ██████╗ ███╗   ███╗ █████╗ ██╗██╗     
  ██╔════╝ ████╗ ████║██╔══██╗██║██║     
  ██║  ███╗██╔████╔██║███████║██║██║     
  ██║   ██║██║╚██╔╝██║██╔══██║██║██║     
  ╚██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗
   ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝

            SOCIETY.INI
        Gmail Generator Tool
        discord.gg/7ZHueg8gWZ
{Colors.RESET}""")

# =========================
# CONFIG
# =========================
def load_config():
    config = configparser.ConfigParser()

    defaults = {
        "length": 10,
        "domain": "gmail.com",
        "save_to_file": False,
        "output_file": "correos.txt"
    }

    if os.path.exists("society.ini"):
        config.read("society.ini")
        settings = config["SETTINGS"]
        return {
            "length": int(settings.get("length", defaults["length"])),
            "domain": settings.get("domain", defaults["domain"]),
            "save_to_file": settings.getboolean("save_to_file", defaults["save_to_file"]),
            "output_file": settings.get("output_file", defaults["output_file"])
        }
    return defaults

# =========================
# GENERADOR
# =========================
def generate_email(length, domain):
    chars = string.ascii_lowercase + string.digits + "."
    name = ''.join(random.choice(chars) for _ in range(length))
    name = name.strip(".").replace("..", ".")
    return f"{name}@{domain}"

# =========================
# MAIN
# =========================
def main():
    while True:
        banner()
        config = load_config()

        # BUCLE DE VALIDACIÓN
        while True:
            user_input = input(
                f"{Colors.YELLOW}¿Cuántos correos quieres generar? (1–100): {Colors.RESET}"
            )

            if not user_input.isdigit():
                print(f"{Colors.RED}Debes introducir un número.{Colors.RESET}")
                time.sleep(1.5)
                continue

            amount = int(user_input)

            if amount == 0:
                print(f"{Colors.RED}No se puede generar 0 correos.{Colors.RESET}")
                time.sleep(1.5)
                continue

            if amount > 100:
                print(f"{Colors.RED}El máximo permitido es 100.{Colors.RESET}")
                time.sleep(1.5)
                continue

            break  # ← número válido

        print(f"\n{Colors.GREEN}Generando correos...\n{Colors.RESET}")
        time.sleep(0.5)

        emails = []
        for _ in range(amount):
            email = generate_email(config["length"], config["domain"])
            emails.append(email)
            print(f"{Colors.CYAN}{email}{Colors.RESET}")
            time.sleep(0.03)

        if config["save_to_file"]:
            with open(config["output_file"], "w", encoding="utf-8") as f:
                for e in emails:
                    f.write(e + "\n")

            print(f"\n{Colors.GREEN}✔ Guardados en {config['output_file']}{Colors.RESET}")

        # ¿REPETIR?
        choice = input(
            f"\n{Colors.YELLOW}¿Quieres generar más correos? (s/n): {Colors.RESET}"
        ).lower()

        if choice != "s":
            print(f"\n{Colors.BOLD}Proceso finalizado.{Colors.RESET}")
            break

# =========================
# START
# =========================
if __name__ == "__main__":
    main()
