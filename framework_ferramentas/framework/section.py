class SectionItem:
    def __init__(self, url: str, text: str) -> None:
        self.url = url
        self.text = text

class Section:
    def __init__(self, title: str, items: list[SectionItem]) -> None:
        self.title = title
        self.items = items