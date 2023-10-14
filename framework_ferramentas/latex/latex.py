class LaTeX:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

        self.document = ''

        self._document_class = 'article'
        self._title = self.file_name
        self._author = ''
        self._date = r'\today'

    def change_document_class(self, nova_document_class: str):
        self._document_class = nova_document_class

    def change_title(self, new_title: str):
        self._title = new_title
    
    def change_author(self, new_author: str):
        self._author = new_author

    def document_class(self):
        self.document += f'\\documentclass{{{self._document_class}}}\n'

    def title(self):
        self.document += f'\\title{{{self._title}}}\n'

    def author(self):
        self.document += f'\\author{{{self._author}}}\n'

    def date(self):
        self.document += f'\\date{{{self._date}}}\n'
    
    def input(self, arquivo: str):
        self.document += f'\\input{{{arquivo}}}\n'

    def make_title(self):
        self.document += f'\\maketitle\n'

    def new_page(self):
        self.document += f'\\newpage\n'

    def table_of_contents(self):
        self.document += f'\\tableofcontents\n'

    def section(self, section_title: str):
        self.document += f'\\section{{{section_title}}}\n'

    def enumerate(self, items: list):
        command = f'\\begin{{enumerate}}\n'

        for item in items:
            command += f'\\item {item}\n'

        command += f'\\end{{enumerate}}\n'

        self.document += command

    def itemize(self, items: list):
        command = f'\\begin{{itemize}}\n'

        for item in items:
            command += f'\\item {item}\n'

        command += f'\\end{{itemize}}\n'

        self.document += command

    def begin_document(self):
        self.document += f'\\begin{{document}}\n'

    def end_document(self):
        self.document += f'\\end{{document}}\n'
    