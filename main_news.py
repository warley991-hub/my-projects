from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep


'''
Passo a passo:

    Importar as bibliotecas
    Abrir o navegador no site.

    Para cada categoria:
        Entra na categoria
        Captura a manchete e o link da notícia e guarda em dicionários
'''


# Manter o navegador aberto
opcoes = Options()
opcoes.add_experimental_option("detach", True)


# Iniciando o navegador e acessando o link
navegador = webdriver.Chrome(options=opcoes)
navegador.get('https://www.cnnbrasil.com.br/')


# Função de clique
def clique(elemento):
    """
    Tenta clicar no elemento e fecha o pop-up se ele aparecer, independente do momento que ele apareça.

    Arg: 
        elemento --> O elemento web que será clicado.

    Erros:
        ElementClickInterceptedException: Caso o clique seja bloqueado por outro motivo que não seja o pop_up.
    """
    try:
        elemento.click()
    except ElementClickInterceptedException as e:
        try:
            sleep(3)
            pop_up = navegador.find_element('id','onesignal-slidedown-dialog')
            fechar_pop_up = navegador.find_element('id','onesignal-slidedown-cancel-button')
            print(f'''
===================
POP UP ENCONTRADO!
===================
\n {pop_up}\n
===================
FECHANDO...
===================''')

            # Fecha o pop up
            fechar_pop_up.click()

            print(f'''
==============================
POP UP FECHADO! CONTINUANDO EM 3s...
==============================''')

            sleep(3)
            # Tenta o clique no elemento novamente
            elemento.click()
            # Sai da função
            return

        except NoSuchElementException:
            print(f'''
===================================
POP-UP NÃO ENCONTRADO...CONTINUANDO
===================================''')

        try:
            ad = navegador.find_element('id','ad_position_box')\
                          .find_element('id','card')\
                          .find_element('class name','dismiss-button')
            print(f'''
=========================================
JANELA DE ANÚNCIO ENCONTRADA, FECHANDO...
=========================================''')

            # Fecha o anúncio
            ad.click()
            
        except NoSuchElementException:
            print(f'''
====================================================
ERRO: JANELA DE ANÚNCIO TAMBÉM NÃO FOI ENCONTRADA...
====================================================''')
            # Dispara o erro
            raise e


# Menus - Política | Money | Infra | I.A
def politica():
    menu_politica = navegador.find_element(By.XPATH,'/html/body/header/div/div/ul/li[3]/a')
    sleep(2)
    clique(menu_politica)
    noticias = navegador.find_elements('css selector', '[data-section="article_list"] li')
    
    politica_noticias = {}
    
    for i in range(1,5):
        elemento_link = noticias[i-1].find_element('css selector', 'h3 a')
        politica_noticias[f'noticia_{i}'] = {'manchete': elemento_link.text, 'link': elemento_link.get_attribute('href')}
            
    print(f'''
==============================
MANCHETES DAS NOTÍCIAS (POLITICA):
==============================
''')
            
    for noticia in politica_noticias:
        print(f'{politica_noticias[noticia]}\n')
        
    navegador.back()


def money():
    menu_money = navegador.find_element(By.XPATH, '/html/body/header/div/div/ul/li[4]/a')
    sleep(2)
    clique(menu_money)
    elemento_pai = navegador.find_element('id', 'block11014636')\
                        .find_element('css selector','.relative.w-full')\
                        .find_element('class name','relative')\
                        .find_element('class name','carouselWrapBlocks')\
                        .find_element('css selector','.relative.flex.w-full.touch-auto.select-none.content-start.overflow-hidden')
    
    noticias = elemento_pai.find_elements('css selector','.keen-slider__slide.fader__slide')


    money_noticias = {}
    
    for i in range(1,5):
        money_noticias[f'noticia_{i}'] = noticias[i-1].find_element('css selector', 'h3.text-base')\
                                                      .get_attribute('textContent')
                                                                
    print(f'''
==============================
MANCHETES DAS NOTÍCIAS (MONEY):
==============================
''')
    
    for noticia in money_noticias:
        print(f'{money_noticias[noticia]}\n')

    navegador.back()


def infra():
    menu_infra = navegador.find_element('link text', 'Infra')
    
    sleep(2)
    clique(menu_infra)

    sleep(2)
    noticias = navegador.find_elements('css selector', '[data-section="article_list"] li')

    infra_noticias = {}

    for i in range(1,5):
        elemento_link = noticias[i-1].find_element('css selector', 'h3 a')
        infra_noticias[f'noticia_{i}'] = {'manchete': elemento_link.text, 'link': elemento_link.get_attribute('href')}
        
    print(f'''
==============================
MANCHETES DAS NOTÍCIAS (INFRA):
==============================
''')
        
    for noticia in infra_noticias:
        print(f'{infra_noticias[noticia]}\n')
    
    navegador.back()

    
def ia():
    menu_ia = navegador.find_element(By.XPATH, '/html/body/header/div/div/ul/li[8]/a')

    sleep(2)
    clique(menu_ia)

    sleep(2)
    noticias = navegador.find_elements('css selector', '[data-section="article_list"] li')

    ia_noticias = {}

    for i in range(1,5):
        elemento_link = noticias[i-1].find_element('css selector', 'h3 a')
        ia_noticias[f'noticia_{i}'] = {'manchete': elemento_link.text, 'link': elemento_link.get_attribute('href')}
        
    print(f'''
==============================
MANCHETES DAS NOTÍCIAS (IA):
==============================
''')
        
    for noticia in ia_noticias:
        print(f'{ia_noticias[noticia]}\n')
    
    navegador.back()


def main():   
    politica()
    sleep(2)
    money()
    sleep(2)
    infra()
    sleep(2)
    ia()


if __name__ == '__main__':
    main()