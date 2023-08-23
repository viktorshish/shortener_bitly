import argparse
import os

from dotenv import load_dotenv
import requests
from urllib.parse import urlparse


def is_bitlink(token, link):       
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(url, headers=headers)
    
    return response.ok


def count_clicks(token, link):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'units': -1}

    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()

    return response.json()['total_clicks']


def shorten_link(token, link):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': link}

    response = requests.post(url, headers=headers, json=payload)   
    response.raise_for_status()
    
    return response.json()['id']


def main():
    parser = argparse.ArgumentParser(
        description='Программа сокращает ссылки и показывает количество переходов по ссылке bitly'
        )
    parser.add_argument('link', help='Ваша ссылка для сокращения или bitly ссылка')
    args = parser.parse_args()
    link_args = args.link
    parsed_link = urlparse(link_args)
    bitly_link =  f'{parsed_link.netloc}{parsed_link.path}'
     
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
        
    try:
        if is_bitlink(token, bitly_link):
            clicks = count_clicks(token, bitly_link)
            print('Количество переходов по ссылке битли: ', clicks)
        else:
            bitlink = shorten_link(token, link_args)
            print(bitlink)
    except requests.exceptions.HTTPError:
        print('Введена некоректная ссылка или невалидный токен ')


if __name__ == '__main__':
    main()
    