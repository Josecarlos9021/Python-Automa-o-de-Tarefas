# Passo 1 - entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2 - fazer login
# Passo 3 - importar a base de dados
# Passo 4 - cadastrar um produto
# Passo 5 - repetir o passo 4 até cadastrar todos os produtos

# pip install pyautogui
# pip install pandas openpyxl numpy

import pyautogui
import time

# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar uma tecla
# pyautogui.hotkey - combinação de tecla (Ctrl C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5

# Passo 1 - entrar no sistema da empresa
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2 - fazer login
pyautogui.click(x=763, y=380)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("j84958451@gmail.com")

# passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.click(x=954, y=539)

time.sleep(3)

# Passo 3 - importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4 - cadastrar um produto
# Para cada linha da minha tabela:
for linha in tabela.index:
    # Código
    pyautogui.click(x=760, y=258)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    # Marca
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    # Tipo
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    # Categoria
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    # Preco_unitario
    pyautogui.press("tab")
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)

    # Custo
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    # Obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    # Clicar no botão enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

# Passo 5 - repetir o passo 4 até cadastrar todos os produtos
    # Voltar a tela pra cima
    pyautogui.scroll(5000)