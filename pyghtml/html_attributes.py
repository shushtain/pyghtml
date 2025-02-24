"""HTML attributes as classes"""

from dataclasses import dataclass, field


@dataclass
class _Attr:
    """The parent class of all attributes. Don't use in production"""

    def __str__(self, html_name=None, default_value=None, sep=" ") -> str:
        str_out = ""
        for attr_value in self.__dict__.values():

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
class Abbr(_Attr):
    """Specifies an abbreviated version of the content in `<th>`"""

    abbr: str = None

    def __str__(self, html_name="abbr", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Accept(_Attr):
    """Specifies the types of files that the server accepts (only for `type="file"`)"""

    accept: str = None

    def __str__(self, html_name="accept", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class AcceptCharset(_Attr):
    """Specifies the character encodings that are to be used for the form submission"""

    accept_charset: str = None

    def __str__(self, html_name="accept-charset", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Accesskey(_Attr):
    """Specifies a shortcut key to activate/focus an element"""

    accesskey: str = None

    def __str__(self, html_name="accesskey", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Action(_Attr):
    """Specifies where to send the form-data when a form is submitted"""

    action: str = None

    def __str__(self, html_name="action", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Allow(_Attr):
    """Specifies a feature-policy for the `<iframe>`"""

    allow: str = None

    def __str__(self, html_name="allow", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Alt(_Attr):
    """Specifies an alternate text when the original element fails to display"""

    alt: str = None

    def __str__(self, html_name="alt", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Anchor(_Attr):
    """Associates a positioned element with an anchor element"""

    anchor: str = None

    def __str__(self, html_name="anchor", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class AriaAttrs(_Attr):
    """A dictionary of ARIA attributes (for accessibility)"""

    aria_attrs: dict = None

    def __str__(self, html_name="aria-", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class As(_Attr):
    """Specifies the type of content being loaded by the link"""

    as_: str = None

    def __str__(self, html_name="as", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Async(_Attr):
    """Specifies that the script is executed asynchronously (only for external scripts)"""

    async_: bool = False

    def __str__(self, html_name="async", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Attributionsrc(_Attr):
    """Specifies that the Attribution-Reporting-Eligible header should be sent along with the image request"""

    attributionsrc: str = None

    def __str__(self, html_name="attributionsrc", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Autocapitalize(_Attr):
    """Sets whether input is automatically capitalized when entered by user"""

    autocapitalize: str = "none"

    def __str__(self, html_name="autocapitalize", default_value="none", sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Autocomplete(_Attr):
    """Specifies whether the `<form>` or the `<input>` element should have autocomplete enabled"""

    autocomplete: str = None

    def __str__(self, html_name="autocomplete", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Autocorrect(_Attr):
    """Controls whether autocorrection of editable text is enabled for spelling and/or punctuation errors"""

    autocorrect: str = "on"

    def __str__(self, html_name="autocorrect", default_value="on", sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Autofocus(_Attr):
    """Specifies that the element should automatically get focus when the page loads"""

    autofocus: bool = False

    def __str__(self, html_name="autofocus", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Autoplay(_Attr):
    """Specifies that the audio/video will start playing as soon as it is ready"""

    autoplay: bool = False

    def __str__(self, html_name="autoplay", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Blocking(_Attr):
    """Indicates that certain operations should be blocked on the fetching of the script"""

    blocking: str = None

    def __str__(self, html_name="blocking", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Browsingtopics(_Attr):
    """Specifies that the topics for the current user should be sent with the request for the `<iframe>`'s source"""

    browsingtopics: bool = False

    def __str__(self, html_name="browsingtopics", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Capture(_Attr):
    """Specifies that a new file should be captured, and which device should be used to capture that new media of a type defined by the `accept` attribute"""

    capture: str = None

    def __str__(self, html_name="capture", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Charset(_Attr):
    """Specifies the character encoding"""

    charset: str = None

    def __str__(self, html_name="charset", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Checked(_Attr):
    """Specifies that an `<input>` element should be pre-selected when the page loads (for `type="checkbox"` or `type="radio"`)"""

    checked: bool = False

    def __str__(self, html_name="checked", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Cite(_Attr):
    """Specifies a URL which explains the quote/deleted/inserted text"""

    cite: str = None

    def __str__(self, html_name="cite", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Class(_Attr):
    """Specifies one or more class names for an element (refers to a class in a style sheet)"""

    class_: str = None

    def __str__(self, html_name="class", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Cols(_Attr):
    """Specifies the visible width of a text area"""

    cols: str = "20"

    def __str__(self, html_name="cols", default_value="20", sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Colspan(_Attr):
    """Specifies the number of columns a table cell should span"""

    colspan: str = "1"

    def __str__(self, html_name="colspan", default_value="1", sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Command(_Attr):
    """Specifies the action to be performed on an element being controlled by a control `<button>`"""

    command: str = None

    def __str__(self, html_name="command", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Commandfor(_Attr):
    """Makes the `<button>` control the given interactive element"""

    commandfor: str = None

    def __str__(self, html_name="commandfor", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Content(_Attr):
    """Gives the value associated with the `http-equiv` or `name` attribute"""

    content: str = None

    def __str__(self, html_name="content", default_value=None, sep=",") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Contenteditable(_Attr):
    """Specifies whether the content of an element is editable or not"""

    contenteditable: str = None

    def __str__(self, html_name="contenteditable", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Controls(_Attr):
    """Specifies that audio/video controls should be displayed (play/pause button, etc)"""

    controls: bool = False

    def __str__(self, html_name="controls", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Controlslist(_Attr):
    """Specifies which browser-native video controls to hide"""

    controlslist: str = None

    def __str__(self, html_name="controlslist", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Coords(_Attr):
    """Specifies the coordinates of the area"""

    coords: str = None

    def __str__(self, html_name="coords", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Credentialless(_Attr):
    """Makes the content of an `<iframe>` load in a new, ephemeral context"""

    credentialless: bool = False

    def __str__(self, html_name="credentialless", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Crossorigin(_Attr):
    """Specifies how the element handles cross-origin requests"""

    crossorigin: str = None

    def __str__(self, html_name="crossorigin", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Csp(_Attr):
    """Specifies the Content Security Policy that an embedded document must agree to enforce upon itself"""

    csp: str = None

    def __str__(self, html_name="csp", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class CustomAttrs(_Attr):
    """A dictionary of custom attributes"""

    custom_attrs: dict = None

    def __str__(self, html_name="", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Data(_Attr):
    """Specifies the URL of the resource to be used by the object"""

    data: str = None

    def __str__(self, html_name="data", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class DataAttrs(_Attr):
    """Used to store custom data private to the page or application"""

    data_attrs: dict = None

    def __str__(self, html_name="data-", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Datetime(_Attr):
    """Specifies the date and time"""

    datetime: str = None

    def __str__(self, html_name="datetime", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Decoding(_Attr):
    """Indicates the preferred method to decode the image"""

    decoding: str = None

    def __str__(self, html_name="decoding", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Default(_Attr):
    """Specifies that the track is to be enabled if the user's preferences do not indicate that another track would be more appropriate"""

    default: bool = False

    def __str__(self, html_name="default", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Defer(_Attr):
    """Specifies that the script is executed when the page has finished parsing (only for external scripts)"""

    defer: bool = False

    def __str__(self, html_name="defer", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Dir(_Attr):
    """Specifies the text direction for the content in an element"""

    dir: str = None

    def __str__(self, html_name="dir", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Dirname(_Attr):
    """Specifies that the text direction will be submitted"""

    dirname: str = None

    def __str__(self, html_name="dirname", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Disabled(_Attr):
    """Specifies that the specified element/group of elements should be disabled"""

    disabled: bool = False

    def __str__(self, html_name="disabled", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Disablepictureinpicture(_Attr):
    """Disables Picture-in-Picture context menu and automatic switching"""

    disablepictureinpicture: bool = False

    def __str__(
        self, html_name="disablepictureinpicture", default_value=False, sep=" "
    ) -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Disableremoteplayback(_Attr):
    """Disables the capability of remote playback through attached devices"""

    disableremoteplayback: bool = False

    def __str__(
        self, html_name="disableremoteplayback", default_value=False, sep=" "
    ) -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Download(_Attr):
    """Specifies that the target will be downloaded when a user clicks on the hyperlink"""

    download: bool | str = False

    def __str__(self, html_name="download", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Draggable(_Attr):
    """Specifies whether an element is draggable or not"""

    draggable: str = None

    def __str__(self, html_name="draggable", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Elementtiming(_Attr):
    """Indicates that an element is flagged for tracking by PerformanceObserver objects"""

    elementtiming: str = None

    def __str__(self, html_name="elementtiming", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Enctype(_Attr):
    """Specifies how the form-data should be encoded when submitting it to the server (only for `method="post"`)"""

    enctype: str = None

    def __str__(self, html_name="enctype", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Enterkeyhint(_Attr):
    """Specifies the text of the enter-key on a virtual keyboard"""

    enterkeyhint: str = None

    def __str__(self, html_name="enterkeyhint", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class EventAttrs(_Attr):
    """A Python dictionary of event attributes (`onclick`, etc)"""

    event_attrs: dict = None

    def __str__(self, html_name="", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Exportparts(_Attr):
    """Allows to select and style elements existing in nested shadow trees by exporting their `part` names"""

    exportparts: str = None

    def __str__(self, html_name="exportparts", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Fetchpriority(_Attr):
    """Indicates how to fetch a particular image relative to other images"""

    fetchpriority: str = None

    def __str__(self, html_name="fetchpriority", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class For(_Attr):
    """Specifies which form element(s) a label/calculation is bound to"""

    for_: str = None

    def __str__(self, html_name="for", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Form(_Attr):
    """Specifies the name of the form the element belongs to"""

    form: str = None

    def __str__(self, html_name="form", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Formaction(_Attr):
    """Specifies where to send the form-data when a form is submitted (for `type="submit"`)"""

    formaction: str = None

    def __str__(self, html_name="formaction", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Formenctype(_Attr):
    """If the button/input has `type="submit"`, sets the encoding type to use"""

    formenctype: str = None

    def __str__(self, html_name="formenctype", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Formmethod(_Attr):
    """If the button/input has `type="submit"`, sets the submission method to use"""

    formmethod: str = None

    def __str__(self, html_name="formmethod", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Formnovalidate(_Attr):
    """If the button/input has `type="submit"`, specifies that the form is not to be validated when submitted"""

    formnovalidate: bool = False

    def __str__(self, html_name="formnovalidate", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Formtarget(_Attr):
    """If the button/input has `type="submit"`, specifies the browsing context (tab, window, etc) in which to display the response"""

    formtarget: str = None

    def __str__(self, html_name="formtarget", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Headers(_Attr):
    """Specifies one or more headers cells a cell is related to"""

    headers: str = None

    def __str__(self, html_name="headers", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Height(_Attr):
    """Specifies the height of the element"""

    height: str = None

    def __str__(self, html_name="height", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Hidden(_Attr):
    """Prevents rendering of the given element, while keeping child elements, e.g. script elements, active"""

    hidden: bool = False

    def __str__(self, html_name="hidden", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class High(_Attr):
    """Specifies the range that is considered to be a high value"""

    high: str = None

    def __str__(self, html_name="high", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Href(_Attr):
    """Specifies the URL of the page the link goes to"""

    href: str = None

    def __str__(self, html_name="href", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Hreflang(_Attr):
    """Specifies the language of the linked document"""

    hreflang: str = None

    def __str__(self, html_name="hreflang", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class HttpEquiv(_Attr):
    """Provides an HTTP header for the information/value of the content attribute"""

    http_equiv: str = None

    def __str__(self, html_name="http-equiv", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Id(_Attr):
    """Specifies a unique id for an element"""

    id: str = None

    def __str__(self, html_name="id", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Imagesizes(_Attr):
    """`sizes` alternative for `rel="preload" as="image"`"""

    imagesizes: str = None

    def __str__(self, html_name="imagesizes", default_value=None, sep=",") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Imagesrcset(_Attr):
    """`srcset` alternative for `rel="preload" as="image"`"""

    imagesrcset: str = None

    def __str__(self, html_name="imagesrcset", default_value=None, sep=",") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Incremental(_Attr):
    """Whether or not to send repeated search events to allow updating live search results while the user is still editing the value of the field"""

    incremental: bool = False

    def __str__(self, html_name="incremental", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Inert(_Attr):
    """Specifies that the browser should ignore this section"""

    inert: bool = False

    def __str__(self, html_name="inert", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class InnerHTML(_Attr):
    """Contents of a container tag (`<tag>`inner_html`</tag>`)"""

    inner_html: list = field(default_factory=list)

    def __post_init__(self):
        if not isinstance(self.inner_html, list):
            self.inner_html = [self.inner_html]

    def __str__(self, html_name="", default_value=None, sep="") -> str:
        return sep.join(str(x) for x in self.inner_html)

    def __getitem__(self, index):
        try:
            return self.inner_html[index]
        except IndexError as e:
            raise IndexError("Index out of range") from e
        except TypeError as e:
            raise TypeError("Index must be an integer or slice") from e

    def __setitem__(self, index, value):
        try:
            self.inner_html[index] = value
        except IndexError as e:
            raise IndexError("Index out of range") from e
        except TypeError as e:
            raise TypeError("Index must be an integer or slice") from e

    def __delitem__(self, index):
        try:
            del self.inner_html[index]
        except IndexError as e:
            raise IndexError("Index out of range") from e
        except TypeError as e:
            raise TypeError("Index must be an integer or slice") from e


@dataclass
class Inputmode(_Attr):
    """Specifies the mode of a virtual keyboard"""

    inputmode: str = None

    def __str__(self, html_name="inputmode", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Integrity(_Attr):
    """Specifies a Subresource Integrity value that allows browsers to verify what they fetch"""

    integrity: str = None

    def __str__(self, html_name="integrity", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Is(_Attr):
    """Specifies that a standard HTML element should behave like a registered custom built-in element"""

    is_: str = None

    def __str__(self, html_name="is", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Ismap(_Attr):
    """Specifies an image as a server-side image map"""

    ismap: bool = False

    def __str__(self, html_name="ismap", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Itemid(_Attr):
    """The unique, global identifier of an item"""

    itemid: str = None

    def __str__(self, html_name="itemid", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Itemprop(_Attr):
    """Adds properties to an item"""

    itemprop: str = None

    def __str__(self, html_name="itemprop", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Itemref(_Attr):
    """Creates associations for properties that are not descendants of an element with the `itemscope` attribute"""

    itemref: str = None

    def __str__(self, html_name="itemref", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Itemscope(_Attr):
    """Specifies that the HTML contained in a block is about a particular item"""

    itemscope: bool = False

    def __str__(self, html_name="itemscope", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Itemtype(_Attr):
    """Specifies the URL of the vocabulary that will be used to define item properties in the data structure"""

    itemtype: str = None

    def __str__(self, html_name="itemtype", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Kind(_Attr):
    """Specifies the kind of text track"""

    kind: str = "subtitles"

    def __str__(self, html_name="kind", default_value="subtitles", sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Label(_Attr):
    """Specifies the title of the text track"""

    label: str = None

    def __str__(self, html_name="label", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Lang(_Attr):
    """Specifies the language of the element's content"""

    lang: str = None

    def __str__(self, html_name="lang", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class List(_Attr):
    """Refers to a `<datalist>` element that contains pre-defined options for an `<input>` element"""

    list: str = None

    def __str__(self, html_name="list", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Loading(_Attr):
    """Indicates if the element should be loaded lazily (`loading="lazy"`) or loaded immediately (`loading="eager"`)"""

    loading: str = None

    def __str__(self, html_name="loading", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Loop(_Attr):
    """Specifies that the audio/video will start over again, every time it is finished"""

    loop: bool = False

    def __str__(self, html_name="loop", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Low(_Attr):
    """Specifies the range that is considered to be a low value"""

    low: str = None

    def __str__(self, html_name="low", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Max(_Attr):
    """Specifies the maximum value"""

    max: str = None

    def __str__(self, html_name="max", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Maxlength(_Attr):
    """Specifies the maximum number of characters allowed in an element"""

    maxlength: str = None

    def __str__(self, html_name="maxlength", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Media(_Attr):
    """Specifies what media/device the linked document is optimized for"""

    media: str = None

    def __str__(self, html_name="media", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Method(_Attr):
    """Specifies the HTTP method to use when sending form-data"""

    method: str = None

    def __str__(self, html_name="method", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Min(_Attr):
    """Specifies the minimum value"""

    min: str = None

    def __str__(self, html_name="min", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Minlength(_Attr):
    """Specifies the minimum number of characters allowed in an element"""

    minlength: str = None

    def __str__(self, html_name="minlength", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Multiple(_Attr):
    """Specifies that a user can enter more than one value"""

    multiple: bool = False

    def __str__(self, html_name="multiple", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Muted(_Attr):
    """Specifies that the audio output of the video should be muted"""

    muted: bool = False

    def __str__(self, html_name="muted", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Name(_Attr):
    """Specifies the name of the element"""

    name: str = None

    def __str__(self, html_name="name", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Nomodule(_Attr):
    """Indicates whether script execution should be prohibited in browsers that support ES modules"""

    nomodule: bool = False

    def __str__(self, html_name="nomodule", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Nonce(_Attr):
    """Defines a cryptographic nonce"""

    nonce: str = None

    def __str__(self, html_name="nonce", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Novalidate(_Attr):
    """Specifies that the form should not be validated when submitted"""

    novalidate: bool = False

    def __str__(self, html_name="novalidate", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Open(_Attr):
    """Specifies that the details should be visible (open) to the user"""

    open: bool = False

    def __str__(self, html_name="open", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Optimum(_Attr):
    """Specifies what value is the optimal value for the gauge"""

    optimum: str = None

    def __str__(self, html_name="optimum", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Orient(_Attr):
    """Sets the orientation of the range slider"""

    orient: str = None

    def __str__(self, html_name="orient", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Part(_Attr):
    """A space-separated list of the part names (`::part`) of the element"""

    part: str = None

    def __str__(self, html_name="part", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Pattern(_Attr):
    """Specifies a regular expression that an `<input>` element's value is checked against"""

    pattern: str = None

    def __str__(self, html_name="pattern", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Ping(_Attr):
    """A space-separated list of URLs to be notified if a user follows the hyperlink"""

    ping: str = None

    def __str__(self, html_name="ping", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Placeholder(_Attr):
    """Specifies a short hint that describes the expected value of the element"""

    placeholder: str = None

    def __str__(self, html_name="placeholder", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Playsinline(_Attr):
    """Indicates that the video is to be played within the element's playback area"""

    playsinline: bool = False

    def __str__(self, html_name="playsinline", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Popover(_Attr):
    """Specifies a popover element"""

    popover: str = None

    def __str__(self, html_name="popover", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Popovertarget(_Attr):
    """Specifies which popover element is to be invoked"""

    popovertarget: str = None

    def __str__(self, html_name="popovertarget", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Popovertargetaction(_Attr):
    """Specifies what happens to the popover element when the button is clicked"""

    popovertargetaction: str = None

    def __str__(
        self, html_name="popovertargetaction", default_value=None, sep=" "
    ) -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Poster(_Attr):
    """Specifies an image to be shown while the video is downloading, or until the user hits the play button"""

    poster: str = None

    def __str__(self, html_name="poster", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Preload(_Attr):
    """Specifies if and how the author thinks the audio/video should be loaded when the page loads"""

    preload: str = None

    def __str__(self, html_name="preload", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Readonly(_Attr):
    """Specifies that the element is read-only"""

    readonly: bool = False

    def __str__(self, html_name="readonly", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Referrerpolicy(_Attr):
    """Specifies which referrer is sent when fetching the resource"""

    referrerpolicy: str = None

    def __str__(self, html_name="referrerpolicy", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Rel(_Attr):
    """Specifies the relationship between the current document and the linked document"""

    rel: str = None

    def __str__(self, html_name="rel", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Results(_Attr):
    """The maximum number of items that should be displayed in the drop-down list of previous search queries"""

    results: str = None

    def __str__(self, html_name="results", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Required(_Attr):
    """Specifies that the element must be filled out before submitting the form"""

    required: bool = False

    def __str__(self, html_name="required", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Reversed(_Attr):
    """Specifies that the list order should be descending (9,8,7...)"""

    reversed: bool = False

    def __str__(self, html_name="reversed", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Role(_Attr):
    """Defines an explicit role for an element for use by assistive technologies"""

    role: str = None

    def __str__(self, html_name="role", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Rows(_Attr):
    """Specifies the visible number of lines in a text area"""

    rows: str = "2"

    def __str__(self, html_name="rows", default_value="2", sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Rowspan(_Attr):
    """Specifies the number of rows a table cell should span"""

    rowspan: str = "1"

    def __str__(self, html_name="rowspan", default_value="1", sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Sandbox(_Attr):
    """Enables an extra set of restrictions for the content in an `<iframe>`"""

    sandbox: str = None

    def __str__(self, html_name="sandbox", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Scope(_Attr):
    """Specifies whether a header cell is a header for a column, row, or group of columns or rows"""

    scope: str = None

    def __str__(self, html_name="scope", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Selected(_Attr):
    """Specifies that an option should be pre-selected when the page loads"""

    selected: bool = False

    def __str__(self, html_name="selected", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Shadowrootclonable(_Attr):
    """Sets the value of the `clonable` property of a ShadowRoot created using this element"""

    shadowrootclonable: bool = False

    def __str__(
        self, html_name="shadowrootclonable", default_value=False, sep=" "
    ) -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Shadowrootdelegatesfocus(_Attr):
    """Sets the value of the `delegatesFocus` property of a ShadowRoot created using this element"""

    shadowrootdelegatesfocus: bool = False

    def __str__(
        self, html_name="shadowrootdelegatesfocus", default_value=False, sep=" "
    ) -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Shadowrootmode(_Attr):
    """Creates a shadow root for the parent element"""

    shadowrootmode: str = None

    def __str__(self, html_name="shadowrootmode", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Shadowrootserializable(_Attr):
    """Sets the value of the `serializable` property of a ShadowRoot created using this element"""

    shadowrootserializable: bool = False

    def __str__(
        self, html_name="shadowrootserializable", default_value=False, sep=" "
    ) -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Shape(_Attr):
    """Specifies the shape of the area"""

    shape: str = None

    def __str__(self, html_name="shape", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Size(_Attr):
    """Specifies the width, in characters (for `<input>`), or the number of visible options (for `<select>`)"""

    size: str = None

    def __str__(self, html_name="size", default_value=None, sep=",") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Sizes(_Attr):
    """Specifies the size of the linked resource"""

    sizes: str = None

    def __str__(self, html_name="sizes", default_value=None, sep=",") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Slot(_Attr):
    """Assigns a slot in a shadow DOM shadow tree to an element"""

    slot: str = None

    def __str__(self, html_name="slot", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Span(_Attr):
    """Specifies the number of columns to span"""

    span: str = "1"

    def __str__(self, html_name="span", default_value="1", sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Spellcheck(_Attr):
    """Specifies whether the element is to have its spelling and grammar checked or not"""

    spellcheck: str = "true"

    def __str__(self, html_name="spellcheck", default_value="true", sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Src(_Attr):
    """Specifies the URL of the media file"""

    src: str = None

    def __str__(self, html_name="src", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Srcdoc(_Attr):
    """Specifies the HTML content of the page to show in the `<iframe>`"""

    srcdoc: str = None

    def __str__(self, html_name="srcdoc", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Srclang(_Attr):
    """Specifies the language of the track text data (required if `kind="subtitles"`)"""

    srclang: str = None

    def __str__(self, html_name="srclang", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Srcset(_Attr):
    """Specifies the URLs of the images to use in different situations"""

    srcset: str = None

    def __str__(self, html_name="srcset", default_value=None, sep=",") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Start(_Attr):
    """Specifies the start value of an ordered list"""

    start: str = None

    def __str__(self, html_name="start", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Step(_Attr):
    """Specifies the legal number intervals for an input field"""

    step: str = None

    def __str__(self, html_name="step", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Style(_Attr):
    """Specifies an inline CSS style for an element"""

    style: str = None

    def __str__(self, html_name="style", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Tabindex(_Attr):
    """Specifies the tabbing order of an element"""

    tabindex: str = None

    def __str__(self, html_name="tabindex", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Target(_Attr):
    """Specifies the target for where to open the linked document or where to submit the form"""

    target: str = None

    def __str__(self, html_name="target", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Title(_Attr):
    """Specifies extra information about an element"""

    title: str = None

    def __str__(self, html_name="title", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Translate(_Attr):
    """Specifies whether the content of an element should be translated or not"""

    translate: str = "yes"

    def __str__(self, html_name="translate", default_value="yes", sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Type(_Attr):
    """Specifies the type of element"""

    type: str = None

    def __str__(self, html_name="type", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Usemap(_Attr):
    """Specifies an image as a client-side image map"""

    usemap: str = None

    def __str__(self, html_name="usemap", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Value(_Attr):
    """Specifies the value of the element"""

    value: str = None

    def __str__(self, html_name="value", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Virtualkeyboardpolicy(_Attr):
    """Controls the on-screen virtual keyboard behavior on devices where a hardware keyboard may not be available"""

    virtualkeyboardpolicy: str = None

    def __str__(
        self, html_name="virtualkeyboardpolicy", default_value=None, sep=" "
    ) -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Webkitdirectory(_Attr):
    """Indicates that only directories should be available to be selected by the user in the file picker interface"""

    webkitdirectory: bool = False

    def __str__(self, html_name="webkitdirectory", default_value=False, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Width(_Attr):
    """Specifies the width of the element"""

    width: str = None

    def __str__(self, html_name="width", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Wrap(_Attr):
    """Specifies how the text in a text area is to be wrapped when submitted in a form"""

    wrap: str = "soft"

    def __str__(self, html_name="wrap", default_value="soft", sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Writingsuggestions(_Attr):
    """Indicates if browser-provided writing suggestions should be enabled"""

    writingsuggestions: str = "true"

    def __str__(
        self, html_name="writingsuggestions", default_value="true", sep=" "
    ) -> str:
        return super().__str__(html_name, default_value, sep)


@dataclass
class Xmlns(_Attr):
    """Specifies the XML Namespace of the document"""

    xmlns: str = None

    def __str__(self, html_name="xmlns", default_value=None, sep=" ") -> str:
        return super().__str__(html_name, default_value, sep)
