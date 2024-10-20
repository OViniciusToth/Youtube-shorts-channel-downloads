import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import yt_dlp
import tkinter as tk
from tkinter import filedialog

def scroll_to_end(driver):
    print("Rolando para o final da página...")

    last_height = driver.execute_script("return document.documentElement.scrollHeight")  # Altura inicial da página

    while True:
        # Rola para o final da página
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        # Aguarda um tempo para a nova parte da página carregar
        time.sleep(5)  # Ajuste esse tempo se necessário

        # Verifica a nova altura da página
        new_height = driver.execute_script("return document.documentElement.scrollHeight")

        # Se a altura não mudar, é porque chegamos ao final
        if new_height == last_height:
            print("Não há mais conteúdo para carregar.")
            break

        last_height = new_height  # Atualiza a altura anterior

    print("Rolagem para o final concluída.")

def get_short_video_links(shorts_url):
    video_links = []
    
    print(f"Inicializando o Selenium para acessar a URL: {shorts_url}")

    # Configurações do Selenium para usar o Chrome
    options = Options()
    options.headless = True  # Mude para False se você quiser ver o navegador
    service = Service('chromedriver.exe')  # Nome do arquivo apenas, já que está na mesma pasta
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(shorts_url)
        time.sleep(5)  # Espera a página carregar completamente

        # Rola para o final da página
        scroll_to_end(driver)

        print("Requisição bem-sucedida! Analisando a página com Selenium...")

        # Captura todos os links de vídeos curtos
        videos = driver.find_elements(By.TAG_NAME, 'a')
        for video in videos:
            href = video.get_attribute('href')
            if href and '/shorts/' in href:
                if href not in video_links:
                    video_links.append(href)
                    print(f"Link encontrado: {href}")

        print(f"Total de links únicos encontrados: {len(video_links)}")
    finally:
        driver.quit()  # Fecha o navegador

    return video_links

def download_video(url, save_path):
    try:
        print(f"Iniciando o download do vídeo: {url}")
        
        def progress_hook(d):
            if d['status'] == 'finished':
                print(f"\nVídeo baixado: {d['filename']}")
            if d['status'] == 'downloading':
                total_size = d['total_bytes'] if 'total_bytes' in d else 0
                downloaded_size = d['downloaded_bytes']
                if total_size > 0:
                    percent = downloaded_size / total_size * 100
                    # Limpa a linha anterior antes de imprimir a nova
                    print(f"\rProgresso do download: {percent:.2f}% para {d['filename']}", end='')

        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Baixa o vídeo
    except Exception as e:
        print(f"Ocorreu um erro ao baixar {url}: {e}")

def open_file_dialogue():
    print("Abrindo o diálogo para seleção de pasta...")
    folder = filedialog.askdirectory()  # Abre o diálogo para seleção de diretório
    if folder:
        print(f"Pasta selecionada: {folder}")
    else:
        print("Nenhuma pasta selecionada.")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    shorts_url = input("Digite a URL da seção de Shorts do YouTube (ex: https://www.youtube.com/@Name/shorts): ")
    save_path = open_file_dialogue()

    if not save_path:
        print("Local de salvamento inválido. Encerrando o programa.")
    else:
        print("Iniciando download dos vídeos curtos...")
        video_links = get_short_video_links(shorts_url)

        if not video_links:
            print("Nenhum vídeo encontrado. Tente verificar se a URL está correta.")
        else:
            # Para cada link encontrado, inicia o download
            for video_url in video_links:
                download_video(video_url, save_path)

            print("Todos os downloads foram iniciados. Verifique a pasta selecionada para os vídeos.")
