import openpyxl
import pyperclip 
import pyautogui
import os

dir_path= os.path.dirname(os.path.abspath(__file__))

excel= os.path.join(dir_path, 'produtos_ficticios.xlsx')

workbook = openpyxl.load_workbook(excel)
sheet_produtos= workbook['Produtos']

for l in sheet_produtos.iter_rows(min_row=2):
    nome_produto= l[0].value
    pyperclip.copy(nome_produto)
    pyautogui.click(1170,382, duration=1)
    pyautogui.hotkey('ctrl', 'v')


    descricao= l[1].value
    pyperclip.copy(descricao)
    pyautogui.click(1169,439, duration=1)
    pyautogui.hotkey('ctrl', 'v')


    categoria= l[2].value
    pyperclip.copy(categoria)
    pyautogui.click(1172,549, duration=1)
    pyautogui.hotkey('ctrl', 'v')


    codigo_produto= l[3].value
    pyperclip.copy(codigo_produto)
    pyautogui.click(1175,618, duration=1)
    pyautogui.hotkey('ctrl', 'v')


    peso_produto= l[4].value
    pyperclip.copy(peso_produto)
    pyautogui.click(1173,683, duration=1)
    pyautogui.hotkey('ctrl', 'v')


    dimensoes_produto= l[5].value
    pyperclip.copy(dimensoes_produto)
    pyautogui.click(1177,742, duration=1)
    pyautogui.hotkey('ctrl', 'v')


    #botao-proximo
    pyautogui.click(1208,799, duration=1)



    preco_produto= l[6].value
    pyperclip.copy(preco_produto)
    pyautogui.click(1172,398, duration=1)
    pyautogui.hotkey('ctrl', 'v')


    quantidade_estoque_produto= l[7].value
    pyperclip.copy(quantidade_estoque_produto)
    pyautogui.click(1183,469, duration=1)
    pyautogui.hotkey('ctrl', 'v')


    data_validade_produto= l[8].value
    pyperclip.copy(data_validade_produto)
    pyautogui.click(1181,525, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    
    
    cor_produto= l[9].value
    pyperclip.copy(cor_produto)
    pyautogui.click(1190,587, duration=1)
    pyautogui.hotkey('ctrl', 'v')



    tamanho_produto= l[10].value
    pyperclip.copy(tamanho_produto)
    pyautogui.click(1182,656, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    material_produto= l[11].value
    pyperclip.copy(material_produto)
    pyautogui.click(1188,717, duration=1)
    pyautogui.hotkey('ctrl', 'v')


    #botao-proximo
    pyautogui.click(1188,768, duration=1)



    fabricante_produto= l[12].value
    pyperclip.copy(fabricante_produto)
    pyautogui.click(1177,405, duration=1)
    pyautogui.hotkey('ctrl', 'v')


    pais_origem_produto= l[13].value
    pyperclip.copy(pais_origem_produto)
    pyautogui.click(1170,472, duration=1)
    pyautogui.hotkey('ctrl', 'v')


    observacoes_produto= l[14].value
    pyperclip.copy(observacoes_produto)
    pyautogui.click(1173,536, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    codigo_barras_produto= l[15].value
    pyperclip.copy(codigo_barras_produto)
    pyautogui.click(1176,649, duration=1)
    pyautogui.hotkey('ctrl', 'v')


    localizacao_armazem_produto= l[16].value
    pyperclip.copy(localizacao_armazem_produto)
    pyautogui.click(1173,714, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    #finalizar
    pyautogui.click(1197,766, duration=1)

    #inicio
    pyautogui.click(1440,585,
    duration=1)














