# Robo de Likes 🤖❤️

Uma automação simples e eficiente em Python para realizar cliques automáticos em lives (TikTok, Instagram, etc.). Este projeto foi criado para facilitar a interação em transmissões ao vivo, simulando cliques no botão de "curtir" ou "amei".

## 🚀 Funcionalidades

- **Cliques em Massa:** Realiza centenas de cliques em segundos.
- **Configuração Fácil:** Ajuste o número de cliques e a velocidade.
- **Segurança (Fail-Safe):** Se você mover o mouse para qualquer canto da tela, o robô para instantaneamente.
- **Multi-plataforma:** Funciona em qualquer rede social que use cliques para dar likes.

## 🛠️ Pré-requisitos

Antes de começar, você precisará ter o [Python](https://www.python.org/) instalado em sua máquina.

## 📦 Instalação

1. Clone este repositório ou baixe os arquivos.
2. Abra o terminal na pasta do projeto.
3. Instale a biblioteca necessária:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Como Usar

### 1. Descobrir as Coordenadas
Como cada monitor tem um tamanho diferente, você precisa dizer ao robô onde clicar:
1. Execute o script de captura:
   ```bash
   python get_coords.py
   ```
2. Posicione o mouse sobre o botão de like da live e espere 5 segundos.
3. O script mostrará os valores de **X** e **Y**.

### 2. Configurar o Robô
1. Abra o arquivo `main.py` em um editor de texto.
2. Altere as variáveis `TARGET_X` e `TARGET_Y` com os valores que você obteve.
3. (Opcional) Ajuste `NUM_CLIQUES` para a quantidade desejada.

### 3. Executar
```bash
python main.py
```
Você terá 5 segundos para alternar para a janela da live antes dos cliques começarem.

## ⚠️ Aviso Legal
Este projeto tem fins educacionais. O uso de automações pode violar os Termos de Serviço de algumas plataformas. Use com responsabilidade e moderação.

---
Projeto desenvolvido para melhorar o GitHub! ⭐

Se curtiu da aquela força 💪
