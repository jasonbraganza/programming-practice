import csv
import os
import statistics

from data_types import Purchase


def main():
    header_print()
    file_to_process = get_data_file()
    data = load_file(file_to_process)
    query_data(data)


def header_print():
    """
    Prints the header for the program
    """
    print("===============================")
    print("The Real Estate Data Miner App!")
    print("===============================")
    print()


def get_data_file():
    base_folder = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(
        base_folder, "data", "SacramentoRealEstateTransactions2008.csv"
    )
    return data_file


def load_file(some_filename):
    with open(some_filename, "r", encoding="utf-8") as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        return purchases


def query_data(some_data):
    some_data.sort(key=lambda p: p.price)
    high_purchase = some_data[-1]
    low_purchase = some_data[0]
    print(
        f"The mose expensive house is {high_purchase.price},  with {high_purchase.beds} beds and {high_purchase.baths} baths"
    )
    print(
        f"The mose expensive house is {low_purchase.price},  with {low_purchase.beds} beds and {low_purchase.baths} baths"
    )

    price_list = [p.price for p in some_data]
    # for price in some_data:
    #     price_list.append(price.price)
    average_price = statistics.mean(price_list)
    print(f"The average price of a house is {int(average_price):,}")

    two_bed_homes = [p for p in some_data if p.beds == 2]
    average_price_2bhk = statistics.mean([p.price for p in two_bed_homes])
    average_baths = statistics.mean([p.baths for p in two_bed_homes])
    average_sq_feet = statistics.mean([p.sq__ft for p in two_bed_homes])
    print(
        f"The average two bedroom home costs {int(average_price_2bhk):,}, has {int(average_baths)} bathrooms and is {int(average_sq_feet)} sq. feet"
    )


if __name__ == "__main__":
    main()
