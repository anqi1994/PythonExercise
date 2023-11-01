class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, author, pagecount, name):
        super().__init__(name)
        self.author = author
        self.pagecount = pagecount

    def print_information(self):
        print(f"The name of this Publication is {self.name}, "
              f"it has {self.pagecount} pages, its author is {self.author}.")


class Magazine(Publication):
    def __init__(self, chiefeditor, name):
        super().__init__(name)
        self.chiefeditor = chiefeditor

    def print_information(self):
        print(f"The name of this publication is {self.name}, "
              f"its chief editor is {self.chiefeditor}.")


pub1 = Magazine("Aki Hyyppä", "Donald Duck")
pub2 = Book("Rosa Liksom", 192, "Compartment No. 6")

pub1.print_information()
pub2.print_information()



