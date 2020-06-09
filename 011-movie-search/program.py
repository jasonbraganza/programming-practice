import movie_svc
import requests.exceptions


def main():
    header_print()
    search_event_loop()


def header_print():
    print("----------------")
    print("MOVIE SEARCH APP")
    print("----------------")
    print()


def search_event_loop():
    search = "ONCE_THROUGH_LOOP"

    while search != "x":
        try:
            search = input("Movie search text (x to exit): ")
            if search != "x":
                results = movie_svc.find_movies(search)
                print(f"Found {len(results)} result(s).")
                for r in results:
                    print(f"{r.year} -- {r.title}")
                print()
        except ValueError:
            print("Error: Search text is required")
        except requests.exceptions.ConnectionError:
            print("Error: Your network is down.")
        except Exception as x:
            print("Unexpected error. Details: {}".format(x))

    print("exiting...")


if __name__ == "__main__":
    main()
