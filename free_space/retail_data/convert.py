import csv
import time
import pandas as pd

data = pd.read_csv("retail_data.csv")


def get_persons_1_book(book: int):
    book1_rows = data[data["book_id"] == book]
    return book1_rows.size


# Task 5.a - 0.02 seconds
def get_persons_2_book(book1: int, book2: int) -> int:
    book1_rows = data[data["book_id"] == book1]
    book2_rows = data[data["book_id"] == book2]

    merged_data = pd.merge(book1_rows, book2_rows, on='person_id', suffixes=('_1', '_2'))
    return merged_data.size


# Task 5.b - 949 seconds
def get_all_persons():
    values = data['book_id'].unique()
    pairs = zip(values[:-1], values[1:])

    for pair in pairs:
        persons_count = get_persons_2_book(pair[0], pair[1])
        print(f"Book: {pair[0]} and Book: {pair[1]} have: {persons_count}")


# Task 5.c
def get_book_percentage():
    values = data['book_id'].unique()
    pairs = zip(values[:-1], values[1:])

    for pair in pairs:
        book1_data_size = get_persons_1_book(pair[0])
        book2_data_size = get_persons_2_book(pair[0], pair[1])
        percentage = book2_data_size / book1_data_size
        print(f"Book: {pair[0]} and then buy book: {pair[1]} only: {percentage:.2f} %")


if __name__ == '__main__':
    start_time = time.time()
    print(get_persons_2_book(19, 38))
    # print(get_all_persons())
    # print(get_book_percentage())
    end_time = time.time()

    elapsed_time = end_time - start_time
    print("Time of executing: " + str(elapsed_time))
