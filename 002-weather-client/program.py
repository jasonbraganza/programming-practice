import requests
import bs4


def main():
    """
    Kicks things off by launching stuff
    """
    print_header()
    area_name = input("What area in India do you want the weather for? ")
    area_weather_raw_data = get_html_from_web(area_name)
    get_weather_from_html(area_weather_raw_data)
    # display forecast


def print_header():
    """
    Prints the header for the program
    """
    print("==========================")
    print("Welcome to the weather app")
    print("==========================")
    print()


def get_html_from_web(some_area_name):
    """
    takes in the name of a place, tacks it on to the end of the wunderground url, fetches the page via requests and returns the text

    :param some_area_name: name of a specific place, which you want the weather for
    :type some_area_name: string
    :return: the webpage of the place queried at weather underground as a requests object
    :rtype: string
    """
    weather_site_url = f"https://www.wunderground.com/weather/in/{some_area_name}/"
    wu_response = requests.get(weather_site_url)
    return wu_response.text


def get_weather_from_html(some_raw_requests_data):
    soup = bs4.BeautifulSoup(some_raw_requests_data, features="html.parser")


if __name__ == "__main__":
    main()
