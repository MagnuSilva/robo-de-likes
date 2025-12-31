import pyautogui
import time

def capturar_coordenadas():
    print("--- Capturador de Coordenadas ---")
    print("Posicione o mouse sobre o botão de LIKE e aguarde...")
    print("A captura será feita em 5 segundos.")
    
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    x, y = pyautogui.position()
    print("\n" + "="*30)
    print(f"COORDENADAS CAPTURADAS!")
    print(f"X: {x}")
    print(f"Y: {y}")
    print("="*30)
    print(f"\nAgora, abra o arquivo 'main.py' e atualize as variáveis:")
    print(f"TARGET_X = {x}")
    print(f"TARGET_Y = {y}")

if __name__ == "__main__":
    capturar_coordenadas()
