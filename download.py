import requests
from bs4 import BeautifulSoup


#fonction pour telecharger une image a partir dune chainde de characteres et dun path
def download_logo(channel_name, path):

    if len(channel_name)>2:
        if channel_name[-3] == '.':
            google_search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={channel_name.replace(' ', '+')[:-3]}+logo"
        else:
            google_search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={channel_name.replace(' ', '+')}+logo"

    response = requests.get(google_search_url)
    #prends la page html et recherche ou la premiere image se trouve
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.findAll('img')

    for image in images:
        #prend limage wikipedia si elle existe pour une meilleur qualite
        if 'wikipedia' in image['src']:
            current_image_url = image['src']
            break

    # si pas trouve prend la premiere
    if 'current_image_url' not in locals():
        current_image_url = images[1]['src']

    #la telecharge
    image_response = requests.get(current_image_url)
    if image_response.status_code == 200:
        with open(f'{path}/{channel_name}.png', 'wb') as file:
            file.write(image_response.content)



#fonction pour ecrire du contenue dans un fichier
def write_to_file(file, content):
    with open(file, 'a') as file:
        file.write(content)
        file.write('\n')