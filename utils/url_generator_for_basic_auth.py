def generate_url(url: str, login: str, password: str) -> str:
    url_parts = url.split('://')
    protocol = url_parts[0]
    rest_of_url = url_parts[1]

    return f'{protocol}://{login}:{password}@{rest_of_url}'
