class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r},{self.weight})'


tools = [
    Tool('수준계', 3.5),
    Tool('해머', 1.25),
    Tool('스크류드라이버', .5),
    Tool('끌', .25)
]
print(repr(tools))
tools.sort(reverse=True, key=lambda x: len(x.name))
print(tools)