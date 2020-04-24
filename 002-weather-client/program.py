import requests
import bs4
import collections

# creating a named tuple so that i can actually refer to names and temperatures easier
weather_report_builder = collections.namedtuple(
    "weather_report", "area, temperatureinc"
)


def main():
    """
    gets the area name from the user
    goes to wunderground and attempts to get the webpage
    parses the webpage
    and then gets the temperature and displays it.
    """
    print_header()
    area_name = input("What area in India do you want the weather for? ")
    area_weather_raw_data = get_html_from_web(area_name)
    weather_report = get_weather_from_html(area_weather_raw_data)
    print(
        f"The area closest is {weather_report.area} and the temperature is {weather_report.temperatureinc}° C."
    )
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
    """
    Runs beautiful soup on the raw requests date and extracts the approximate place found along with it’s temperature and returns those as a tuple.

    :param some_raw_requests_data: requests library object
    :type some_raw_requests_data: string
    :return: name of the closest matched place and the temperature found.
    :rtype: tuple
    """
    soup = bs4.BeautifulSoup(some_raw_requests_data, features="html.parser")
    city_detected = (
        soup.find("h1")
        .get_text()
        .replace("Weather Conditions", "")
        .replace("star_ratehome", "")
    )
    temperaturef = soup.find(class_="wu-value wu-value-to").get_text()
    temperaturec = round(((int(temperaturef) - 32) * 5 / 9), 2)
    wu_report = weather_report_builder(area=city_detected, temperatureinc=temperaturec)
    return wu_report


if __name__ == "__main__":
    main()
