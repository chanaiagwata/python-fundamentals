text_file = "test.txt"
def read_file(text_file):
    """
    Function that reads a text file and returns the data from the test file
    Rises:
        FileNotFoundError if cannot find file
    """
    try:
        with open(text_file, "r") as handle:
            data = handle.read()
            return data
    except FileNotFoundError:
        return None
