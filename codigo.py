# P1.2
import pyautogui

# P1.10
import time

# P1.9
pyautogui.PAUSE = 3.0

# P1.4
pyautogui.press("win")
# P1.5
pyautogui.write("chrome")
# P1.6
pyautogui.press("enter")
# P1.7
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
# P1.8
pyautogui.press("enter")

# P1.10.1
time.sleep(4.0)

# P2.1 
pyautogui.click(x=388, y=375)

# P2.2
pyautogui.write("email.maio2024@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4.0)

# P3.1

import pandas as pd

# P3.2
tabela = pd.read_csv("produtos.csv")

# P5.2
for linha in tabela.index:
    pyautogui.click(x=389, y=258)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = (str(tabela.loc[linha, "obs"]))
    if obs != "nan":
        pyautogui.write(obs) 
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)