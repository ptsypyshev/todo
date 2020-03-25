import requests

def get_reddit():
    r = requests.get('https://www.reddit.com/r/Python/')
    print(r.status_code)
    print(r.headers)
    with open('reddit.json', mode='w') as f:
        # f.write(str(r.json()))
        print(r.json())


if __name__ == '__main__':
    get_reddit()
