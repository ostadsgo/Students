import requests


def get_data(url: str, key: str) -> list[dict[str, str]]:
    """
    Send request to url and extract the key from retrived data and return it.
    :param url: url of the request.
    :param key: key of the dict
    :return: return a dict contain values.
    """
    request = requests.get(url)
    data = request.json()
    value = data.get(key)
    return value


def list_artists() -> list[dict[str, str]]:
    """
    Return list of artists.
    :return: return a dict contain values.
    """
    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    return get_data(url, "artists")


def get_artist_by_id(artist_id: str) -> dict[str, list[str]]:
    """Return data for an specific artist."""
    url = f"https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/{artist_id}"
    return get_data(url, "artist")


def get_artist(artist_name: str) -> dict[str, list[str]]:
    """
    Returns a dict describing the artist with name.
    :param artist_name: name of the artist.
    :return: a dict contains artist's information.
    """
    resume = {}
    for artist in list_artists():
        if artist["name"].lower() == artist_name.lower():
            resume = get_artist_by_id(artist["id"])
    return resume
