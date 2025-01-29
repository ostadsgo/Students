import requests


def get_data(url: str, key: str) -> dict[str, str]:
    """
    Get url and a key, send a request with url and return data based on key.
    :param url: url of the request.
    :param key: key of the dict
    :return: return a dict contain values.
    """
    r = requests.get(url)
    data = r.json()
    value = data[key]
    return value


def list_artists() -> list[str]:
    """
    Return artists list
    :return: A list contains name of artists.
    """
    url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
    artists = get_data(url, "artists")
    return artists


def get_artist_by_id(artist_id: str) -> dict[str, list[str]]:
    """
    Returns a dictionary describing the artist with id
    :param artist_id: id of the artist.
    :return: a dict contains artist's information.
    """
    url = f"https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/{artist_id}"
    artist = get_data(url, "artist")
    return artist


def get_artist(artist_name: str) -> dict[str, list[str]]:
    """
    Returns a dict describing the artist with name.
    :param artist_name: name of the artist.
    :return: a dict contains artist's information.
    """
    artists = list_artists()
    for artist in artists:
        if artist["name"].lower() == artist_name.lower():
            artist_info = get_artist_by_id(artist["id"])
            return {"status": "ok", "value": artist_info}
    return {"status": "error", "value": "ERROR: Artist not found."}
