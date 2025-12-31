import pyautogui
import time

# Configurações do Robô
# ---------------------
# PAUSE: Tempo de espera entre os comandos do PyAutoGUI (0 para máxima velocidade)
pyautogui.PAUSE = 0

# Coordenadas do botão de like (ajuste usando o script get_coords.py)
# No vídeo original, as coordenadas eram (1326, 683)
TARGET_X, TARGET_Y = 1326, 683 

# Número total de cliques que o robô deve realizar
NUM_CLIQUES = 500

# Intervalo entre cada clique (em segundos)
# 0.05 (50ms) é um valor seguro para não travar o navegador
INTERVALO_CLIQUES = 0.05

def iniciar_automacao():
    print("--- Robo de Likes Iniciado ---")
    print(f"Preparando para clicar {NUM_CLIQUES} vezes em ({TARGET_X}, {TARGET_Y})")
    print("Você tem 5 segundos para mudar para a janela da Live...")
    
    # Contagem regressiva
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)

    # Opcional: Alt+Tab automático (descomente se quiser que ele troque de janela sozinho)
    # print("Trocando de janela...")
    # pyautogui.keyDown('alt')
    # pyautogui.press('tab')
    # pyautogui.keyUp('alt')
    # time.sleep(1)

    print("Iniciando cliques! Mova o mouse para o canto da tela para parar (Fail-safe).")
    
    try:
        for i in range(NUM_CLIQUES):
            pyautogui.click(TARGET_X, TARGET_Y)
            time.sleep(INTERVALO_CLIQUES)
            
            # Mostra progresso a cada 50 cliques
            if (i + 1) % 50 == 0:
                print(f"Progresso: {i + 1}/{NUM_CLIQUES} cliques realizados.")
                
    except pyautogui.FailSafeException:
        print("\n[AVISO] Fail-safe ativado! O robô foi interrompido porque o mouse foi movido para o canto.")
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro inesperado: {e}")
    finally:
        print("\n--- Automação Concluída ---")

if __name__ == "__main__":
    iniciar_automacao()
