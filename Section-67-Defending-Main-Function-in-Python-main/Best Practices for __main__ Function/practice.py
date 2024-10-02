print('This is my practice file')


def process_execution(data):
    print("Beginning the execution")
    print("Data is processing..", data)
    print("Data processing is finished")


def write_data(data):
    print(data, "is written to database")


def main():
    data = "Sample data"
    process_execution(data)
    write_data(data)


if __name__ == "__main__":
    main()