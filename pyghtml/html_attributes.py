from dataclasses import dataclass, field


@dataclass
class _Attr:
    def __str__(self, html_name, default_value, sep=" ") -> str:
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
                temp = sep.join(str(x) for x in attr_value)
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
class Abbr(_Enum):
    abbr: str = None

    def __str__(self) -> str:
        return super().__str__("abbr", None)


@dataclass
class Accept(_Enum):
    accept: str = None

    def __str__(self) -> str:
        return super().__str__("accept", None, ",")


@dataclass
class Accept_charset(_Enum):
    accept_charset: str = None

    def __str__(self) -> str:
        return super().__str__("accept-charset", None)


@dataclass
class Accesskey(_Enum):
    accesskey: str = None

    def __str__(self) -> str:
        return super().__str__("accesskey", None)


@dataclass
class Action(_Enum):
    action: str = None

    def __str__(self) -> str:
        return super().__str__("action", None)


@dataclass
class Allow(_Enum):
    allow: str = None

    def __str__(self) -> str:
        return super().__str__("allow", None)


@dataclass
class Allowfullscreen(_Bool):
    allowfullscreen: bool = False

    def __str__(self) -> str:
        return super().__str__("allowfullscreen", False)


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
class As_attr(_Enum):
    as_attr: str = None

    def __str__(self) -> str:
        return super().__str__("as", None)


@dataclass
class Async_attr(_Bool):
    async_attr: bool = False

    def __str__(self) -> str:
        return super().__str__("async", False)


@dataclass
class Attributionsrc(_Enum):
    attributionsrc: bool | str = False

    def __str__(self) -> str:
        return super().__str__("attributionsrc", False)


@dataclass
class Autocapitalize(_Enum):
    autocapitalize: str = "none"

    def __str__(self) -> str:
        return super().__str__("autocapitalize", "none")


@dataclass
class Autocomplete(_Enum):
    autocomplete: str = None

    def __str__(self) -> str:
        return super().__str__("autocomplete", None)


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
class Blocking(_Enum):
    blocking: str = None

    def __str__(self) -> str:
        return super().__str__("blocking", None)


@dataclass
class Browsingtopics(_Bool):
    browsingtopics: bool = False

    def __str__(self) -> str:
        return super().__str__("browsingtopics", False)


@dataclass
class Capture(_Enum):
    capture: str = None

    def __str__(self) -> str:
        return super().__str__("capture", None)


@dataclass
class Charset(_Enum):
    charset: str = None

    def __str__(self) -> str:
        return super().__str__("charset", None)


@dataclass
class Checked(_Bool):
    checked: bool = False

    def __str__(self) -> str:
        return super().__str__("checked", False)


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
class Cols(_Enum):
    cols: str = "20"

    def __str__(self) -> str:
        return super().__str__("cols", "20")


@dataclass
class Colspan(_Enum):
    colspan: str = "1"

    def __str__(self) -> str:
        return super().__str__("colspan", "1")


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
class Content(_Enum):
    content: str = None

    def __str__(self) -> str:
        return super().__str__("content", None)


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
class Credentialless(_Bool):
    credentialless: bool = False

    def __str__(self) -> str:
        return super().__str__("credentialless", False)


@dataclass
class Crossorigin(_Enum):
    crossorigin: str = None

    def __str__(self) -> str:
        return super().__str__("crossorigin", None)


@dataclass
class Csp(_Enum):
    csp: str = None

    def __str__(self) -> str:
        return super().__str__("csp", None)


@dataclass
class Custom_attrs(_Dict):
    custom_attrs: dict = None

    def __str__(self) -> str:
        return super().__str__("", None)


@dataclass
class Data(_Enum):
    data: str = None

    def __str__(self) -> str:
        return super().__str__("data", None)


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
class Decoding(_Enum):
    decoding: str = None

    def __str__(self) -> str:
        return super().__str__("decoding", None)


@dataclass
class Default(_Bool):
    default: bool = False

    def __str__(self) -> str:
        return super().__str__("default", False)


@dataclass
class Defer(_Bool):
    defer: bool = False

    def __str__(self) -> str:
        return super().__str__("defer", False)


@dataclass
class Dir(_Enum):
    dir: str = None

    def __str__(self) -> str:
        return super().__str__("dir", None)


@dataclass
class Dirname(_Enum):
    dirname: str = None

    def __str__(self) -> str:
        return super().__str__("dirname", None)


@dataclass
class Disabled(_Bool):
    disabled: bool = False

    def __str__(self) -> str:
        return super().__str__("disabled", False)


@dataclass
class Disablepictureinpicture(_Bool):
    disablepictureinpicture: bool = False

    def __str__(self) -> str:
        return super().__str__("disablepictureinpicture", False)


@dataclass
class Disableremoteplayback(_Bool):
    disableremoteplayback: bool = False

    def __str__(self) -> str:
        return super().__str__("disableremoteplayback", False)


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
class Elementtiming(_Enum):
    elementtiming: str = None

    def __str__(self) -> str:
        return super().__str__("elementtiming", None)


@dataclass
class Enctype(_Enum):
    enctype: str = None

    def __str__(self) -> str:
        return super().__str__("enctype", None)


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
class Fetchpriority(_Enum):
    fetchpriority: str = None

    def __str__(self) -> str:
        return super().__str__("fetchpriority", None)


@dataclass
class For_attr(_Enum):
    for_attr: str = None

    def __str__(self) -> str:
        return super().__str__("for", None)


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
class Headers(_Enum):
    headers: str = None

    def __str__(self) -> str:
        return super().__str__("headers", None)


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
class High(_Enum):
    high: str = None

    def __str__(self) -> str:
        return super().__str__("high", None)


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
class Http_equiv(_Enum):
    http_equiv: str = None

    def __str__(self) -> str:
        return super().__str__("http-equiv", None)


@dataclass
class Id(_Enum):
    id: str = None

    def __str__(self) -> str:
        return super().__str__("id", None)


@dataclass
class Imagesizes(_Enum):
    imagesizes: str = None

    def __str__(self) -> str:
        return super().__str__("imagesizes", None, ",")


@dataclass
class Imagesrcset(_Enum):
    imagesrcset: str = None

    def __str__(self) -> str:
        return super().__str__("imagesrcset", None, ",")


@dataclass
class Incremental(_Bool):
    incremental: bool = False

    def __str__(self) -> str:
        return super().__str__("incremental", False)


@dataclass
class Inert(_Bool):
    inert: bool = False

    def __str__(self) -> str:
        return super().__str__("inert", False)


@dataclass
class InnerHTML:
    innerHTML: list = field(default_factory=list)

    def __str__(self, sep="") -> str:
        return sep.join(str(x) for x in self.innerHTML)


@dataclass
class Inputmode(_Enum):
    inputmode: str = None

    def __str__(self) -> str:
        return super().__str__("inputmode", None)


@dataclass
class Integrity(_Enum):
    integrity: str = None

    def __str__(self) -> str:
        return super().__str__("integrity", None)


@dataclass
class Is_attr(_Enum):
    is_attr: str = None

    def __str__(self) -> str:
        return super().__str__("is", None)


@dataclass
class Ismap(_Bool):
    ismap: bool = False

    def __str__(self) -> str:
        return super().__str__("ismap", False)


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
class Kind(_Enum):
    kind: str = "subtitles"

    def __str__(self) -> str:
        return super().__str__("kind", "subtitles")


@dataclass
class Label(_Enum):
    label: str = None

    def __str__(self) -> str:
        return super().__str__("label", None)


@dataclass
class Lang(_Enum):
    lang: str = None

    def __str__(self) -> str:
        return super().__str__("lang", None)


@dataclass
class List(_Enum):
    list: str = None

    def __str__(self) -> str:
        return super().__str__("list", None)


@dataclass
class Loading(_Enum):
    loading: str = None

    def __str__(self) -> str:
        return super().__str__("loading", None)


@dataclass
class Loop(_Bool):
    loop: bool = False

    def __str__(self) -> str:
        return super().__str__("loop", False)


@dataclass
class Low(_Enum):
    low: str = None

    def __str__(self) -> str:
        return super().__str__("low", None)


@dataclass
class Max(_Enum):
    max: str = None

    def __str__(self) -> str:
        return super().__str__("max", None)


@dataclass
class Maxlength(_Enum):
    maxlength: str = None

    def __str__(self) -> str:
        return super().__str__("maxlength", None)


@dataclass
class Media(_Enum):
    media: str = None

    def __str__(self) -> str:
        return super().__str__("media", None)


@dataclass
class Method(_Enum):
    method: str = None

    def __str__(self) -> str:
        return super().__str__("method", None)


@dataclass
class Min(_Enum):
    min: str = None

    def __str__(self) -> str:
        return super().__str__("min", None)


@dataclass
class Minlength(_Enum):
    minlength: str = None

    def __str__(self) -> str:
        return super().__str__("minlength", None)


@dataclass
class Multiple(_Bool):
    multiple: bool = False

    def __str__(self) -> str:
        return super().__str__("multiple", False)


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
class Nomodule(_Bool):
    nomodule: bool = False

    def __str__(self) -> str:
        return super().__str__("nomodule", False)


@dataclass
class Nonce(_Enum):
    nonce: str = None

    def __str__(self) -> str:
        return super().__str__("nonce", None)


@dataclass
class Novalidate(_Bool):
    novalidate: bool = False

    def __str__(self) -> str:
        return super().__str__("novalidate", False)


@dataclass
class Open(_Bool):
    open: bool = False

    def __str__(self) -> str:
        return super().__str__("open", False)


@dataclass
class Optimum(_Enum):
    optimum: str = None

    def __str__(self) -> str:
        return super().__str__("optimum", None)


@dataclass
class Orient(_Enum):
    orient: str = None

    def __str__(self) -> str:
        return super().__str__("orient", None)


@dataclass
class Part(_Enum):
    part: str = None

    def __str__(self) -> str:
        return super().__str__("part", None)


@dataclass
class Pattern(_Enum):
    pattern: str = None

    def __str__(self) -> str:
        return super().__str__("pattern", None)


@dataclass
class Ping(_Enum):
    ping: str = None

    def __str__(self) -> str:
        return super().__str__("ping", None)


@dataclass
class Placeholder(_Enum):
    placeholder: str = None

    def __str__(self) -> str:
        return super().__str__("placeholder", None)


@dataclass
class Playsinline(_Bool):
    playsinline: bool = False

    def __str__(self) -> str:
        return super().__str__("playsinline", False)


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
class Poster(_Enum):
    poster: str = None

    def __str__(self) -> str:
        return super().__str__("poster", None)


@dataclass
class Preload(_Enum):
    preload: str = None

    def __str__(self) -> str:
        return super().__str__("preload", None)


@dataclass
class Readonly(_Bool):
    readonly: bool = False

    def __str__(self) -> str:
        return super().__str__("readonly", False)


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
class Results(_Enum):
    results: str = None

    def __str__(self) -> str:
        return super().__str__("results", None)


@dataclass
class Required(_Bool):
    required: bool = False

    def __str__(self) -> str:
        return super().__str__("required", False)


@dataclass
class Reversed(_Bool):
    reversed: bool = False

    def __str__(self) -> str:
        return super().__str__("reversed", False)


@dataclass
class Role(_Enum):
    role: str = None

    def __str__(self) -> str:
        return super().__str__("role", None)


@dataclass
class Rows(_Enum):
    rows: str = "2"

    def __str__(self) -> str:
        return super().__str__("rows", "2")


@dataclass
class Rowspan(_Enum):
    rowspan: str = "1"

    def __str__(self) -> str:
        return super().__str__("rowspan", "1")


@dataclass
class Sandbox(_Enum):
    sandbox: str = None

    def __str__(self) -> str:
        return super().__str__("sandbox", None)


@dataclass
class Scope(_Enum):
    scope: str = None

    def __str__(self) -> str:
        return super().__str__("scope", None)


@dataclass
class Selected(_Bool):
    selected: bool = False

    def __str__(self) -> str:
        return super().__str__("selected", False)


@dataclass
class Shadowrootclonable(_Bool):
    shadowrootclonable: bool = False

    def __str__(self) -> str:
        return super().__str__("shadowrootclonable", False)


@dataclass
class Shadowrootdelegatesfocus(_Bool):
    shadowrootdelegatesfocus: bool = False

    def __str__(self) -> str:
        return super().__str__("shadowrootdelegatesfocus", False)


@dataclass
class Shadowrootmode(_Enum):
    shadowrootmode: str = None

    def __str__(self) -> str:
        return super().__str__("shadowrootmode", None)


@dataclass
class Shadowrootserializable(_Bool):
    shadowrootserializable: bool = False

    def __str__(self) -> str:
        return super().__str__("shadowrootserializable", False)


@dataclass
class Shape(_Enum):
    shape: str = None

    def __str__(self) -> str:
        return super().__str__("shape", None)


@dataclass
class Size(_Enum):
    size: str = None

    def __str__(self) -> str:
        return super().__str__("size", None, ",")


@dataclass
class Sizes(_Enum):
    sizes: str = None

    def __str__(self) -> str:
        return super().__str__("sizes", None, ",")


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
class Srcdoc(_Enum):
    srcdoc: str = None

    def __str__(self) -> str:
        return super().__str__("srcdoc", None)


@dataclass
class Srclang(_Enum):
    srclang: str = None

    def __str__(self) -> str:
        return super().__str__("srclang", None)


@dataclass
class Srcset(_Enum):
    srcset: str = None

    def __str__(self) -> str:
        return super().__str__("srcset", None, ",")


@dataclass
class Start(_Enum):
    start: str = None

    def __str__(self) -> str:
        return super().__str__("start", None)


@dataclass
class Step(_Enum):
    step: str = None

    def __str__(self) -> str:
        return super().__str__("step", None)


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
class Usemap(_Enum):
    usemap: str = None

    def __str__(self) -> str:
        return super().__str__("usemap", None)


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
class Webkitdirectory(_Bool):
    webkitdirectory: bool = False

    def __str__(self) -> str:
        return super().__str__("webkitdirectory", False)


@dataclass
class Width(_Enum):
    width: str = None

    def __str__(self) -> str:
        return super().__str__("width", None)


@dataclass
class Wrap(_Enum):
    wrap: str = "soft"

    def __str__(self) -> str:
        return super().__str__("wrap", "soft")


@dataclass
class Writingsuggestions(_Enum):
    writingsuggestions: str = "true"

    def __str__(self) -> str:
        return super().__str__("writingsuggestions", "true")


@dataclass
class Xmlns(_Enum):
    xmlns: str = None

    def __str__(self) -> str:
        return super().__str__("xmlns", None)
