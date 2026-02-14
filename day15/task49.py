from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_content(self):
        pass

class PDFDocument(Printable):
    def print_content(self):
        return "Printing PDF Document"

class Image(Printable):
    def print_content(self):
        return "Printing Image File"

pdf = PDFDocument()
print( pdf.print_content())