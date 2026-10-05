G = "\033[32m"
DG = "\033[90m"
C = "\033[36m"
R = "\033[0m"
B = "\033[1m"

BANNER = f"""
{G}╔══════════════════════════════════════════════════════╗
║  {B}ReACT Agent v1.0{R}{G}                                    ║
║  {DG}Powered by qwen3:8b | LangGraph{R}{G}                     ║
║  {DG}Type 'quit' to terminate session{R}{G}                     ║
╚══════════════════════════════════════════════════════╝{R}
"""

def print_banner():
    print(BANNER)

def print_loading():
    print(f"{DG}[*] Loading graph...{R}")

def print_ready():
    print(f"{G}[+] Agent ready. Awaiting input.{R}")

def print_processing():
    print(f"{DG}[*] Processing...{R}")

def print_response(content):
    print(f"\n{G}[agent]{R} {content}")

def print_exit():
    print(f"\n{DG}[*] Session terminated.{R}")

def prompt():
    return input(f"\n{C}{B}root@react>{R} ")
