from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador =p.chromium.launch(headless=False)#headless
    pagina=navegador.new_page()
    pagina.goto('https://pje.tjba.jus.br/pje/login.seam')
    time.sleep(5)
    pagina.locator('xpath = //*[@id="loginAplicacaoButton"]').click()
    time.sleep(10)
    pagina.locator('//*[@id="barraSuperiorPrincipal"]/div/div[2]/ul/li/a/span[2]/img').click()
    time.sleep(10)
    pagina.locator('//*[@id="papeisUsuarioForm:usuarioLocalizacaoDecoration:usuarioLocalizacao"]',has_text='5ª V DA FAZENDA PÚBLICA DE SALVADOR/Juiz de Direito Titular').click()
    time.sleep(15)
