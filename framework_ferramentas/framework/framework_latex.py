from latex.latex import LaTeX
from framework.section import SectionItem, Section


class FrameworkLaTeX:
    def __init__(self, file_name: str) -> None:
        self.latex = LaTeX(file_name)

        self.sections: list[Section] = []

    def add_section(self, section_title: str, section_items: list[str]):
        section = Section(section_title, section_items)
        self.sections.append(section)

    def initial_config(self):
        self.latex.change_author("Gustavo Azevedo Naldoni")
        self.latex.change_title("Ferramentas - Segurança Cibernética")

    def generate_tex(self):
        self.initial_config()

        self.latex.document_class()
        self.latex.input("pacotes.tex")

        self.latex.title()
        self.latex.author()
        self.latex.date()

        self.latex.begin_document()

        self.latex.make_title()
        self.latex.new_page()

        self.latex.table_of_contents()
        self.latex.new_page()

        for section in self.sections:
            title = section.title
            formatted_items = self._format_enumerate(section.items)

            self.latex.section(title)
            self.latex.enumerate(formatted_items)

        self.latex.end_document()

        with open(f"./{self.latex.file_name}.tex", mode="w") as file:
            file.write(self.latex.document)

    def _format_enumerate(self, section_items: list[SectionItem]) -> list[str]:
        result = []

        for section_item in section_items:
            result.append(f"\\href{{{section_item.url}}}{{{section_item.text}}}")

        return result
