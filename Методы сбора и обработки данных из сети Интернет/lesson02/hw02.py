import requests
import bs4
import json


class GeekHtmlPosts:
    def __init__(self):
        self.__base_url = 'https://geekbrains.ru'
        self.__url_start = 'https://geekbrains.ru/posts'
        self.__header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like '
                                       'Gecko) Chrome/80.0.3987.132 Safari/537.36'}
        self.posts = []

    def __get_posts_url(self) -> []:
        p_url = []
        [p_url.extend(self.__get_post_url(soap)) for soap in self.__get_page()]
        return p_url

    def __get_page(self):
        url = self.__url_start
        while url:
            soap = bs4.BeautifulSoup(requests.get(url, headers=self.__header).text, 'lxml')
            yield soap
            url = self.__get_next_page(soap)

    def __get_next_page(self, soap: bs4.BeautifulSoup) -> str:
        a = soap.find("a", text="›")
        return f'{self.__base_url}{a["href"]}' if a else None

    def __get_post_url(self, soap: bs4.BeautifulSoup) -> []:
        return [f'{self.__base_url}{i["href"]}' for i in soap.select(".post-item__title")]

    def get_posts_data(self):
        p_struct = {}
        for url in self.__get_posts_url():
            soap = bs4.BeautifulSoup(requests.get(url, headers=self.__header).text, 'lxml')
            p_struct['url'] = url
            p_struct['image'] = soap.select_one('img')['src']
            p_struct['title'] = soap.select_one('.blogpost-title').text
            p_struct['writer'] = {'name': soap.find(attrs={"itemprop": "author"}).text,
                                  'url': f'{self.__base_url}{soap.select_one(".col-md-5 a")["href"]}'}
            p_struct['tags'] = {itm.text: f'{self.__base_url}{itm["href"]}' for itm in soap.select('a.small')}
            self.posts.append(p_struct.copy())

    def save_posts(self):
        for p in self.posts:
            with open(f'{p["url"].replace("/","_").replace("https:__", "").replace(".", "")}.json', 'w') as file:
                file.write(json.dumps(p))

    def save_tags(self):
        tags = {}
        for p in self.posts:
            for k, v in p['tags'].items():
                if not tags.get(k):
                    tags[k] = {'url': v, 'posts': [p['url']]}
                else:
                    tags[k]['posts'].append(p['url'])
        with open(f'tags.json', 'w') as file:
            file.write(json.dumps(tags))


if __name__ == '__main__':
    geek_post = GeekHtmlPosts()
    geek_post.get_posts_data()
    geek_post.save_posts()
    geek_post.save_tags()
