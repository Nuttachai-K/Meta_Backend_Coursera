class myFirstClass():
    def __init__(self) -> None:
        print("Who wrote this?")
        self.index = "Author-Book"

    def hand_list(self,philosopher,book):
        print(f"{philosopher} wrote the book: {book}")

whodunit = myFirstClass()
whodunit.hand_list("Sunzhu","The Art of War")

