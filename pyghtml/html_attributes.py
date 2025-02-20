from dataclasses import dataclass, field


@dataclass
class _Attr:
    def __str__(self, html_name, default_value) -> str:
        str_out = ""
        for attr_key, attr_value in self.__dict__.items():

            if attr_value == default_value:
                continue

            if isinstance(attr_value, bool):
                if attr_value:
                    str_out += f" {html_name}"
                continue

            if isinstance(attr_value, (str, int, float)):
                str_out += f' {html_name}="{str(attr_value)}"'
                continue

            if isinstance(attr_value, dict):
                for k, v in attr_value.items():
                    if isinstance(v, bool):
                        if v:
                            str_out += f" {k}"
                    elif isinstance(v, (str, int, float)):
                        str_out += f' {k}="{str(v)}"'
                continue

            if isinstance(attr_value, list):
                temp = " ".join(str(x) for x in attr_value)
                str_out += f' {html_name}="{temp}"'
                continue

        return str_out.strip()


@dataclass
class _Enum(_Attr): ...


@dataclass
class _Bool(_Attr): ...


@dataclass
class _Dict(_Attr): ...


@dataclass
class _List(_Attr): ...


@dataclass
class Accesskey(_Enum):
    accesskey: str = None

    def __str__(self) -> str:
        return super().__str__("accesskey", None)


@dataclass
class Alt(_Enum):
    alt: str = None

    def __str__(self) -> str:
        return super().__str__("alt", None)


@dataclass
class Anchor(_Enum):
    anchor: str = None

    def __str__(self) -> str:
        return super().__str__("anchor", None)


@dataclass
class Aria_attrs(_Dict):
    aria_attrs: dict = None

    def __str__(self) -> str:
        return super().__str__("aria-", None)


@dataclass
class Attributionsrc(_Enum):
    attributionsrc: bool | str = None

    def __str__(self) -> str:
        return super().__str__("attributionsrc", None)


@dataclass
class Autocapitalize(_Enum):
    autocapitalize: str = "none"

    def __str__(self) -> str:
        return super().__str__("autocapitalize", "none")


@dataclass
class Autocorrect(_Enum):
    autocorrect: str = "on"

    def __str__(self) -> str:
        return super().__str__("autocorrect", "on")


@dataclass
class Autofocus(_Bool):
    autofocus: bool = False

    def __str__(self) -> str:
        return super().__str__("autofocus", False)


@dataclass
class Autoplay(_Bool):
    autoplay: bool = False

    def __str__(self) -> str:
        return super().__str__("autoplay", False)


@dataclass
class Cite(_Enum):
    cite: str = None

    def __str__(self) -> str:
        return super().__str__("cite", None)


@dataclass
class Class_attr(_Enum):
    class_attr: str = None

    def __str__(self) -> str:
        return super().__str__("class", None)


@dataclass
class Command(_Enum):
    command: str = None

    def __str__(self) -> str:
        return super().__str__("command", None)


@dataclass
class Commandfor(_Enum):
    commandfor: str = None

    def __str__(self) -> str:
        return super().__str__("commandfor", None)


@dataclass
class Contenteditable(_Enum):
    contenteditable: str = None

    def __str__(self) -> str:
        return super().__str__("contenteditable", None)


@dataclass
class Controls(_Bool):
    controls: bool = False

    def __str__(self) -> str:
        return super().__str__("controls", False)


@dataclass
class Controlslist(_Enum):
    controlslist: str = None

    def __str__(self) -> str:
        return super().__str__("controlslist", None)


@dataclass
class Coords(_Enum):
    coords: str = None

    def __str__(self) -> str:
        return super().__str__("coords", None)


@dataclass
class Crossorigin(_Enum):
    crossorigin: str = None

    def __str__(self) -> str:
        return super().__str__("crossorigin", None)


@dataclass
class Custom_attrs(_Dict):
    custom_attrs: dict = None

    def __str__(self) -> str:
        return super().__str__("", None)


@dataclass
class Data_attrs(_Dict):
    data_attrs: dict = None

    def __str__(self) -> str:
        return super().__str__("data-", None)


@dataclass
class Datetime(_Enum):
    datetime: str = None

    def __str__(self) -> str:
        return super().__str__("datetime", None)


@dataclass
class Dir(_Enum):
    dir: str = None

    def __str__(self) -> str:
        return super().__str__("dir", None)


@dataclass
class Disabled(_Bool):
    disabled: bool = False

    def __str__(self) -> str:
        return super().__str__("disabled", False)


@dataclass
class Disableremoteplayback(_Bool):
    disableremoteplayback: bool = False

    def __str__(self) -> str:
        return super().__str__("disableremoteplayback", False)


@dataclass
class Download(_Enum):
    download: bool | str = False

    def __str__(self) -> str:
        return super().__str__("download", False)


@dataclass
class Draggable(_Enum):
    draggable: str = None

    def __str__(self) -> str:
        return super().__str__("draggable", None)


@dataclass
class Enterkeyhint(_Enum):
    enterkeyhint: str = None

    def __str__(self) -> str:
        return super().__str__("enterkeyhint", None)


@dataclass
class Event_attrs(_Dict):
    event_attrs: dict = None

    def __str__(self) -> str:
        return super().__str__("", None)


@dataclass
class Exportparts(_Enum):
    exportparts: str = None

    def __str__(self) -> str:
        return super().__str__("exportparts", None)


@dataclass
class Form(_Enum):
    form: str = None

    def __str__(self) -> str:
        return super().__str__("form", None)


@dataclass
class Formaction(_Enum):
    formaction: str = None

    def __str__(self) -> str:
        return super().__str__("formaction", None)


@dataclass
class Formenctype(_Enum):
    formenctype: str = None

    def __str__(self) -> str:
        return super().__str__("formenctype", None)


@dataclass
class Formmethod(_Enum):
    formmethod: str = None

    def __str__(self) -> str:
        return super().__str__("formmethod", None)


@dataclass
class Formnovalidate(_Bool):
    formnovalidate: bool = False

    def __str__(self) -> str:
        return super().__str__("formnovalidate", False)


@dataclass
class Formtarget(_Enum):
    formtarget: str = None

    def __str__(self) -> str:
        return super().__str__("formtarget", None)


@dataclass
class Height(_Enum):
    height: str = None

    def __str__(self) -> str:
        return super().__str__("height", None)


@dataclass
class Hidden(_Bool):
    hidden: bool = False

    def __str__(self) -> str:
        return super().__str__("hidden", False)


@dataclass
class Href(_Enum):
    href: str = None

    def __str__(self) -> str:
        return super().__str__("href", None)


@dataclass
class Hreflang(_Enum):
    hreflang: str = None

    def __str__(self) -> str:
        return super().__str__("hreflang", None)


@dataclass
class Id(_Enum):
    id: str = None

    def __str__(self) -> str:
        return super().__str__("id", None)


@dataclass
class Inert(_Bool):
    inert: bool = False

    def __str__(self) -> str:
        return super().__str__("inert", False)


@dataclass
class InnerHTML:
    innerHTML: list = field(default_factory=list)

    def __str__(self) -> str:
        return " ".join(str(x) for x in self.innerHTML)


@dataclass
class Inputmode(_Enum):
    inputmode: str = None

    def __str__(self) -> str:
        return super().__str__("inputmode", None)


@dataclass
class Is_attr(_Enum):
    is_attr: str = None

    def __str__(self) -> str:
        return super().__str__("is", None)


@dataclass
class Itemid(_Enum):
    itemid: str = None

    def __str__(self) -> str:
        return super().__str__("itemid", None)


@dataclass
class Itemprop(_Enum):
    itemprop: str = None

    def __str__(self) -> str:
        return super().__str__("itemprop", None)


@dataclass
class Itemref(_Enum):
    itemref: str = None

    def __str__(self) -> str:
        return super().__str__("itemref", None)


@dataclass
class Itemscope(_Bool):
    itemscope: bool = False

    def __str__(self) -> str:
        return super().__str__("itemscope", False)


@dataclass
class Itemtype(_Enum):
    itemtype: str = None

    def __str__(self) -> str:
        return super().__str__("itemtype", None)


@dataclass
class Lang(_Enum):
    lang: str = None

    def __str__(self) -> str:
        return super().__str__("lang", None)


@dataclass
class Loop(_Bool):
    loop: bool = False

    def __str__(self) -> str:
        return super().__str__("loop", False)


@dataclass
class Muted(_Bool):
    muted: bool = False

    def __str__(self) -> str:
        return super().__str__("muted", False)


@dataclass
class Name(_Enum):
    name: str = None

    def __str__(self) -> str:
        return super().__str__("name", None)


@dataclass
class Nonce(_Enum):
    nonce: str = None

    def __str__(self) -> str:
        return super().__str__("nonce", None)


@dataclass
class Open(_Bool):
    open: bool = False

    def __str__(self) -> str:
        return super().__str__("open", False)


@dataclass
class Part(_Enum):
    part: str = None

    def __str__(self) -> str:
        return super().__str__("part", None)


@dataclass
class Ping(_Enum):
    ping: str = None

    def __str__(self) -> str:
        return super().__str__("ping", None)


@dataclass
class Popover(_Enum):
    popover: str = None

    def __str__(self) -> str:
        return super().__str__("popover", None)


@dataclass
class Popovertarget(_Enum):
    popovertarget: str = None

    def __str__(self) -> str:
        return super().__str__("popovertarget", None)


@dataclass
class Popovertargetaction(_Enum):
    popovertargetaction: str = None

    def __str__(self) -> str:
        return super().__str__("popovertargetaction", None)


@dataclass
class Preload(_Enum):
    preload: str = None

    def __str__(self) -> str:
        return super().__str__("preload", None)


@dataclass
class Referrerpolicy(_Enum):
    referrerpolicy: str = None

    def __str__(self) -> str:
        return super().__str__("referrerpolicy", None)


@dataclass
class Rel(_Enum):
    rel: str = None

    def __str__(self) -> str:
        return super().__str__("rel", None)


@dataclass
class Role(_Enum):
    role: str = None

    def __str__(self) -> str:
        return super().__str__("role", None)


@dataclass
class Shape(_Enum):
    shape: str = None

    def __str__(self) -> str:
        return super().__str__("shape", None)


@dataclass
class Slot(_Enum):
    slot: str = None

    def __str__(self) -> str:
        return super().__str__("slot", None)


@dataclass
class Span(_Enum):
    span: str = "1"

    def __str__(self) -> str:
        return super().__str__("span", "1")


@dataclass
class Spellcheck(_Enum):
    spellcheck: str = "true"

    def __str__(self) -> str:
        return super().__str__("spellcheck", "true")


@dataclass
class Src(_Enum):
    src: str = None

    def __str__(self) -> str:
        return super().__str__("src", None)


@dataclass
class Style(_Enum):
    style: str = None

    def __str__(self) -> str:
        return super().__str__("style", None)


@dataclass
class Tabindex(_Enum):
    tabindex: str = None

    def __str__(self) -> str:
        return super().__str__("tabindex", None)


@dataclass
class Target(_Enum):
    target: str = None

    def __str__(self) -> str:
        return super().__str__("target", None)


@dataclass
class Title(_Enum):
    title: str = None

    def __str__(self) -> str:
        return super().__str__("title", None)


@dataclass
class Translate(_Enum):
    translate: str = "yes"

    def __str__(self) -> str:
        return super().__str__("translate", "yes")


@dataclass
class Type(_Enum):
    type: str = None

    def __str__(self) -> str:
        return super().__str__("type", None)


@dataclass
class Value(_Enum):
    value: str = None

    def __str__(self) -> str:
        return super().__str__("value", None)


@dataclass
class Virtualkeyboardpolicy(_Enum):
    virtualkeyboardpolicy: str = None

    def __str__(self) -> str:
        return super().__str__("virtualkeyboardpolicy", None)


@dataclass
class Width(_Enum):
    width: str = None

    def __str__(self) -> str:
        return super().__str__("width", None)


@dataclass
class Writingsuggestions(_Enum):
    writingsuggestions: str = "true"

    def __str__(self) -> str:
        return super().__str__("writingsuggestions", "true")
