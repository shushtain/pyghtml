# class _Global:
#     _tag = None

#     def __init__(self, *, anchor: str = None, dir: str = None):
#         self.anchor = anchor
#         self.dir = dir


# class _Container(_Global):
#     def __init__(self, *, innerHTML: list = [], **kwargs):
#         super().__init__(**kwargs)
#         self.innerHTML = innerHTML


# tag = _Container(anchor="auto")
# print(tag.innerHTML)

from dataclasses import dataclass


@dataclass
class innerHTML:
    innerHTML: str = None

    @property
    def innerHTML(self):
        return self._innerHTML[1]

    @innerHTML.setter
    def innerHTML(self, innerHTML):
        self._innerHTML = [None, innerHTML, "innerHTML"]


@dataclass
class autofocus:
    autofocus: bool = False
    enabled: bool = True


@dataclass
class _Container(autofocus, innerHTML):
    def __str__(self):
        out = ""
        for key, value in self.__dict__.items():
            if isinstance(value, bool):
                out += f" {value} "
            else:
                out += f" {key}={value} "
        return out
