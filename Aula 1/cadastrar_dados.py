import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.5

#Acessando o sistema
pyautogui.press("win")
pyautogui.write("opera gx")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.click(2792, 456)
pyautogui.write("nome.sobrenome@gmail.com")
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")

time.sleep(2) #Esperando a nova página carregar

#Inserindo dados no sistema
tabela = pandas.read_csv("produtos.csv") #Trazendo os dados do csv

for linha in tabela.index: #Inserindo os dados da tabela no sistema
    pyautogui.click(2525, 335)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))

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
    if not pandas.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("home")
    time.sleep(0.5)

print(f"Dados cadastrados com sucesso!")
