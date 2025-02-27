"""HTML attributes as classes"""

from dataclasses import dataclass, field


@dataclass
class _Attr:
    """The parent class of all attributes. Don't use in production"""

    def __str__(self) -> str:
        attrs = self.__dict__
        attrs_str = ""
        for key, value in attrs.items():

            key_pure = key[:-1] if key[-1] == "_" else key

            # skip "service" arguments
            if key[0] == "_":
                continue

            # skip inner_html as a quasi-attribute
            if key == "inner_html":
                continue

            # skip default values
            default_value = self.__dataclass_fields__[key].default
            if value == default_value:
                continue
            # including `1` as `"1"`, but not booleans
            if type(default_value) is int and value == str(default_value):
                continue

            html_name = key_pure.replace("_", "-")

            if isinstance(value, bool):
                attrs_str += f" {html_name}" if value else ""
                continue

            if isinstance(value, (str, int, float)):
                attrs_str += f' {html_name}="{str(value)}"'
                continue

            if isinstance(value, dict):
                for k, v in value.items():
                    if isinstance(v, bool):
                        attrs_str += f" {k}" if v else ""
                    elif isinstance(v, (str, int, float)):
                        attrs_str += f' {k}="{str(v)}"'
                continue

            types = str(self.__dataclass_fields__[key].type).split(" | ")
            if types[0] == "list":
                sep = ", "
            else:
                sep = " "

            if isinstance(value, list):
                temp = sep.join(str(x) for x in value)
                attrs_str += f' {html_name}="{temp}"'
                continue

        return attrs_str


@dataclass
class Abbr(_Attr):
    """Specifies an abbreviated version of the content in `<th>`"""

    abbr: str | None = None


@dataclass
class Accept(_Attr):
    """Specifies the types of files that the server accepts (only for `type="file"`)"""

    accept: str | None = None


@dataclass
class AcceptCharset(_Attr):
    """Specifies the character encodings that are to be used for the form submission"""

    accept_charset: str | None = None


@dataclass
class Accesskey(_Attr):
    """Specifies a shortcut key to activate/focus an element"""

    accesskey: str | None = None


@dataclass
class Action(_Attr):
    """Specifies where to send the form-data when a form is submitted"""

    action: str | None = None


@dataclass
class Allow(_Attr):
    """Specifies a feature-policy for the `<iframe>`"""

    allow: str | None = None


@dataclass
class Alt(_Attr):
    """Specifies an alternate text when the original element fails to display"""

    alt: str | None = None


@dataclass
class Anchor(_Attr):
    """Associates a positioned element with an anchor element"""

    anchor: str | None = None


@dataclass
class AriaAttrs(_Attr):
    """A dictionary of ARIA attributes (for accessibility)"""

    aria_attrs: dict | None = None


@dataclass
class As(_Attr):
    """Specifies the type of content being loaded by the link"""

    as_: str | None = None


@dataclass
class Async(_Attr):
    """Specifies that the script is executed asynchronously (only for external scripts)"""

    async_: bool = False


@dataclass
class Attributionsrc(_Attr):
    """Specifies that the Attribution-Reporting-Eligible header should be sent along with the image request"""

    attributionsrc: str | None = None


@dataclass
class Autocapitalize(_Attr):
    """Sets whether input is automatically capitalized when entered by user"""

    autocapitalize: str = "none"


@dataclass
class Autocomplete(_Attr):
    """Specifies whether the `<form>` or the `<input>` element should have autocomplete enabled"""

    autocomplete: str | None = None


@dataclass
class Autocorrect(_Attr):
    """Controls whether autocorrection of editable text is enabled for spelling and/or punctuation errors"""

    autocorrect: str = "on"


@dataclass
class Autofocus(_Attr):
    """Specifies that the element should automatically get focus when the page loads"""

    autofocus: bool = False


@dataclass
class Autoplay(_Attr):
    """Specifies that the audio/video will start playing as soon as it is ready"""

    autoplay: bool = False


@dataclass
class Blocking(_Attr):
    """Indicates that certain operations should be blocked on the fetching of the script"""

    blocking: str | None = None


@dataclass
class Browsingtopics(_Attr):
    """Specifies that the topics for the current user should be sent with the request for the `<iframe>`'s source"""

    browsingtopics: bool = False


@dataclass
class Capture(_Attr):
    """Specifies that a new file should be captured, and which device should be used to capture that new media of a type defined by the `accept` attribute"""

    capture: str | None = None


@dataclass
class Charset(_Attr):
    """Specifies the character encoding"""

    charset: str | None = None


@dataclass
class Checked(_Attr):
    """Specifies that an `<input>` element should be pre-selected when the page loads (for `type="checkbox"` or `type="radio"`)"""

    checked: bool = False


@dataclass
class Cite(_Attr):
    """Specifies a URL which explains the quote/deleted/inserted text"""

    cite: str | None = None


@dataclass
class Class(_Attr):
    """Specifies one or more class names for an element (refers to a class in a style sheet)"""

    class_: str | list | None = None


@dataclass
class Cols(_Attr):
    """Specifies the visible width of a text area"""

    cols: str | int = 20


@dataclass
class Colspan(_Attr):
    """Specifies the number of columns a table cell should span"""

    colspan: str | int = 1


@dataclass
class Command(_Attr):
    """Specifies the action to be performed on an element being controlled by a control `<button>`"""

    command: str | None = None


@dataclass
class Commandfor(_Attr):
    """Makes the `<button>` control the given interactive element"""

    commandfor: str | None = None


@dataclass
class Content(_Attr):
    """Gives the value associated with the `http-equiv` or `name` attribute"""

    content: list | str | None = None


@dataclass
class Contenteditable(_Attr):
    """Specifies whether the content of an element is editable or not"""

    contenteditable: str | None = None


@dataclass
class Controls(_Attr):
    """Specifies that audio/video controls should be displayed (play/pause button, etc)"""

    controls: bool = False


@dataclass
class Controlslist(_Attr):
    """Specifies which browser-native video controls to hide"""

    controlslist: str | None = None


@dataclass
class Coords(_Attr):
    """Specifies the coordinates of the area"""

    coords: str | None = None


@dataclass
class Credentialless(_Attr):
    """Makes the content of an `<iframe>` load in a new, ephemeral context"""

    credentialless: bool = False


@dataclass
class Crossorigin(_Attr):
    """Specifies how the element handles cross-origin requests"""

    crossorigin: bool | str = False


@dataclass
class Csp(_Attr):
    """Specifies the Content Security Policy that an embedded document must agree to enforce upon itself"""

    csp: str | None = None


@dataclass
class CustomAttrs(_Attr):
    """A dictionary of custom attributes"""

    custom_attrs: dict | None = None


@dataclass
class Data(_Attr):
    """Specifies the URL of the resource to be used by the object"""

    data: str | None = None


@dataclass
class DataAttrs(_Attr):
    """Used to store custom data private to the page or application"""

    data_attrs: dict | None = None


@dataclass
class Datetime(_Attr):
    """Specifies the date and time"""

    datetime: str | None = None


@dataclass
class Decoding(_Attr):
    """Indicates the preferred method to decode the image"""

    decoding: str | None = None


@dataclass
class Default(_Attr):
    """Specifies that the track is to be enabled if the user's preferences do not indicate that another track would be more appropriate"""

    default: bool = False


@dataclass
class Defer(_Attr):
    """Specifies that the script is executed when the page has finished parsing (only for external scripts)"""

    defer: bool = False


@dataclass
class Dir(_Attr):
    """Specifies the text direction for the content in an element"""

    dir: str | None = None


@dataclass
class Dirname(_Attr):
    """Specifies that the text direction will be submitted"""

    dirname: str | None = None


@dataclass
class Disabled(_Attr):
    """Specifies that the specified element/group of elements should be disabled"""

    disabled: bool = False


@dataclass
class Disablepictureinpicture(_Attr):
    """Disables Picture-in-Picture context menu and automatic switching"""

    disablepictureinpicture: bool = False


@dataclass
class Disableremoteplayback(_Attr):
    """Disables the capability of remote playback through attached devices"""

    disableremoteplayback: bool = False


@dataclass
class Download(_Attr):
    """Specifies that the target will be downloaded when a user clicks on the hyperlink"""

    download: bool | str = False


@dataclass
class Draggable(_Attr):
    """Specifies whether an element is draggable or not"""

    draggable: str | None = None


@dataclass
class Elementtiming(_Attr):
    """Indicates that an element is flagged for tracking by PerformanceObserver objects"""

    elementtiming: str | None = None


@dataclass
class Enctype(_Attr):
    """Specifies how the form-data should be encoded when submitting it to the server (only for `method="post"`)"""

    enctype: str | None = None


@dataclass
class Enterkeyhint(_Attr):
    """Specifies the text of the enter-key on a virtual keyboard"""

    enterkeyhint: str | None = None


@dataclass
class EventAttrs(_Attr):
    """A Python dictionary of event attributes (`onclick`, etc)"""

    event_attrs: dict | None = None


@dataclass
class Exportparts(_Attr):
    """Allows to select and style elements existing in nested shadow trees by exporting their `part` names"""

    exportparts: str | None = None


@dataclass
class Fetchpriority(_Attr):
    """Indicates how to fetch a particular image relative to other images"""

    fetchpriority: str | None = None


@dataclass
class For(_Attr):
    """Specifies which form element(s) a label/calculation is bound to"""

    for_: str | None = None


@dataclass
class Form(_Attr):
    """Specifies the name of the form the element belongs to"""

    form: str | None = None


@dataclass
class Formaction(_Attr):
    """Specifies where to send the form-data when a form is submitted (for `type="submit"`)"""

    formaction: str | None = None


@dataclass
class Formenctype(_Attr):
    """If the button/input has `type="submit"`, sets the encoding type to use"""

    formenctype: str | None = None


@dataclass
class Formmethod(_Attr):
    """If the button/input has `type="submit"`, sets the submission method to use"""

    formmethod: str | None = None


@dataclass
class Formnovalidate(_Attr):
    """If the button/input has `type="submit"`, specifies that the form is not to be validated when submitted"""

    formnovalidate: bool = False


@dataclass
class Formtarget(_Attr):
    """If the button/input has `type="submit"`, specifies the browsing context (tab, window, etc) in which to display the response"""

    formtarget: str | None = None


@dataclass
class Headers(_Attr):
    """Specifies one or more headers cells a cell is related to"""

    headers: str | None = None


@dataclass
class Height(_Attr):
    """Specifies the height of the element"""

    height: str | None = None


@dataclass
class Hidden(_Attr):
    """Prevents rendering of the given element, while keeping child elements, e.g. script elements, active"""

    hidden: bool = False


@dataclass
class High(_Attr):
    """Specifies the range that is considered to be a high value"""

    high: str | None = None


@dataclass
class Href(_Attr):
    """Specifies the URL of the page the link goes to"""

    href: str | None = None


@dataclass
class Hreflang(_Attr):
    """Specifies the language of the linked document"""

    hreflang: str | None = None


@dataclass
class HttpEquiv(_Attr):
    """Provides an HTTP header for the information/value of the content attribute"""

    http_equiv: str | None = None


@dataclass
class Id(_Attr):
    """Specifies a unique id for an element"""

    id: str | None = None


@dataclass
class Imagesizes(_Attr):
    """`sizes` alternative for `rel="preload" as="image"`"""

    imagesizes: list | str | None = None


@dataclass
class Imagesrcset(_Attr):
    """`srcset` alternative for `rel="preload" as="image"`"""

    imagesrcset: list | str | None = None


@dataclass
class Incremental(_Attr):
    """Whether or not to send repeated search events to allow updating live search results while the user is still editing the value of the field"""

    incremental: bool = False


@dataclass
class Inert(_Attr):
    """Specifies that the browser should ignore this section"""

    inert: bool = False


@dataclass
class InnerHtml:
    """Contents of a container tag (`<tag>`inner_html`</tag>`)"""

    inner_html: list = field(default_factory=list)

    def __post_init__(self):
        if not isinstance(self.inner_html, list):
            self.inner_html = [self.inner_html]

    def __str__(self):
        return "".join(str(x) for x in self.inner_html)

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

    inputmode: str | None = None


@dataclass
class Integrity(_Attr):
    """Specifies a Subresource Integrity value that allows browsers to verify what they fetch"""

    integrity: str | None = None


@dataclass
class Is(_Attr):
    """Specifies that a standard HTML element should behave like a registered custom built-in element"""

    is_: str | None = None


@dataclass
class Ismap(_Attr):
    """Specifies an image as a server-side image map"""

    ismap: bool = False


@dataclass
class Itemid(_Attr):
    """The unique, global identifier of an item"""

    itemid: str | None = None


@dataclass
class Itemprop(_Attr):
    """Adds properties to an item"""

    itemprop: str | None = None


@dataclass
class Itemref(_Attr):
    """Creates associations for properties that are not descendants of an element with the `itemscope` attribute"""

    itemref: str | None = None


@dataclass
class Itemscope(_Attr):
    """Specifies that the HTML contained in a block is about a particular item"""

    itemscope: bool = False


@dataclass
class Itemtype(_Attr):
    """Specifies the URL of the vocabulary that will be used to define item properties in the data structure"""

    itemtype: str | None = None


@dataclass
class Kind(_Attr):
    """Specifies the kind of text track"""

    kind: str = "subtitles"


@dataclass
class Label(_Attr):
    """Specifies the title of the text track"""

    label: str | None = None


@dataclass
class Lang(_Attr):
    """Specifies the language of the element's content"""

    lang: str | None = None


@dataclass
class List(_Attr):
    """Refers to a `<datalist>` element that contains pre-defined options for an `<input>` element"""

    list: str | None = None


@dataclass
class Loading(_Attr):
    """Indicates if the element should be loaded lazily (`loading="lazy"`) or loaded immediately (`loading="eager"`)"""

    loading: str | None = None


@dataclass
class Loop(_Attr):
    """Specifies that the audio/video will start over again, every time it is finished"""

    loop: bool = False


@dataclass
class Low(_Attr):
    """Specifies the range that is considered to be a low value"""

    low: str | None = None


@dataclass
class Max(_Attr):
    """Specifies the maximum value"""

    max: str | None = None


@dataclass
class Maxlength(_Attr):
    """Specifies the maximum number of characters allowed in an element"""

    maxlength: str | None = None


@dataclass
class Media(_Attr):
    """Specifies what media/device the linked document is optimized for"""

    media: str | None = None


@dataclass
class Method(_Attr):
    """Specifies the HTTP method to use when sending form-data"""

    method: str | None = None


@dataclass
class Min(_Attr):
    """Specifies the minimum value"""

    min: str | None = None


@dataclass
class Minlength(_Attr):
    """Specifies the minimum number of characters allowed in an element"""

    minlength: str | None = None


@dataclass
class Multiple(_Attr):
    """Specifies that a user can enter more than one value"""

    multiple: bool = False


@dataclass
class Muted(_Attr):
    """Specifies that the audio output of the video should be muted"""

    muted: bool = False


@dataclass
class Name(_Attr):
    """Specifies the name of the element"""

    name: str | None = None


@dataclass
class Nomodule(_Attr):
    """Indicates whether script execution should be prohibited in browsers that support ES modules"""

    nomodule: bool = False


@dataclass
class Nonce(_Attr):
    """Defines a cryptographic nonce"""

    nonce: str | None = None


@dataclass
class Novalidate(_Attr):
    """Specifies that the form should not be validated when submitted"""

    novalidate: bool = False


@dataclass
class Open(_Attr):
    """Specifies that the details should be visible (open) to the user"""

    open: bool = False


@dataclass
class Optimum(_Attr):
    """Specifies what value is the optimal value for the gauge"""

    optimum: str | None = None


@dataclass
class Orient(_Attr):
    """Sets the orientation of the range slider"""

    orient: str | None = None


@dataclass
class Part(_Attr):
    """A space-separated list of the part names (`::part`) of the element"""

    part: str | None = None


@dataclass
class Pattern(_Attr):
    """Specifies a regular expression that an `<input>` element's value is checked against"""

    pattern: str | None = None


@dataclass
class Ping(_Attr):
    """A space-separated list of URLs to be notified if a user follows the hyperlink"""

    ping: str | None = None


@dataclass
class Placeholder(_Attr):
    """Specifies a short hint that describes the expected value of the element"""

    placeholder: str | None = None


@dataclass
class Playsinline(_Attr):
    """Indicates that the video is to be played within the element's playback area"""

    playsinline: bool = False


@dataclass
class Popover(_Attr):
    """Specifies a popover element"""

    popover: str | None = None


@dataclass
class Popovertarget(_Attr):
    """Specifies which popover element is to be invoked"""

    popovertarget: str | None = None


@dataclass
class Popovertargetaction(_Attr):
    """Specifies what happens to the popover element when the button is clicked"""

    popovertargetaction: str | None = None


@dataclass
class Poster(_Attr):
    """Specifies an image to be shown while the video is downloading, or until the user hits the play button"""

    poster: str | None = None


@dataclass
class Preload(_Attr):
    """Specifies if and how the author thinks the audio/video should be loaded when the page loads"""

    preload: str | None = None


@dataclass
class Readonly(_Attr):
    """Specifies that the element is read-only"""

    readonly: bool = False


@dataclass
class Referrerpolicy(_Attr):
    """Specifies which referrer is sent when fetching the resource"""

    referrerpolicy: str | None = None


@dataclass
class Rel(_Attr):
    """Specifies the relationship between the current document and the linked document"""

    rel: str | None = None


@dataclass
class Results(_Attr):
    """The maximum number of items that should be displayed in the drop-down list of previous search queries"""

    results: str | None = None


@dataclass
class Required(_Attr):
    """Specifies that the element must be filled out before submitting the form"""

    required: bool = False


@dataclass
class Reversed(_Attr):
    """Specifies that the list order should be descending (9,8,7...)"""

    reversed: bool = False


@dataclass
class Role(_Attr):
    """Defines an explicit role for an element for use by assistive technologies"""

    role: str | None = None


@dataclass
class Rows(_Attr):
    """Specifies the visible number of lines in a text area"""

    rows: str | int = 2


@dataclass
class Rowspan(_Attr):
    """Specifies the number of rows a table cell should span"""

    rowspan: str | int = 1


@dataclass
class Sandbox(_Attr):
    """Enables an extra set of restrictions for the content in an `<iframe>`"""

    sandbox: str | None = None

    "sandbox"


@dataclass
class Scope(_Attr):
    """Specifies whether a header cell is a header for a column, row, or group of columns or rows"""

    scope: str | None = None


@dataclass
class Selected(_Attr):
    """Specifies that an option should be pre-selected when the page loads"""

    selected: bool = False


@dataclass
class Shadowrootclonable(_Attr):
    """Sets the value of the `clonable` property of a ShadowRoot created using this element"""

    shadowrootclonable: bool = False


@dataclass
class Shadowrootdelegatesfocus(_Attr):
    """Sets the value of the `delegatesFocus` property of a ShadowRoot created using this element"""

    shadowrootdelegatesfocus: bool = False


@dataclass
class Shadowrootmode(_Attr):
    """Creates a shadow root for the parent element"""

    shadowrootmode: str | None = None


@dataclass
class Shadowrootserializable(_Attr):
    """Sets the value of the `serializable` property of a ShadowRoot created using this element"""

    shadowrootserializable: bool = False


@dataclass
class Shape(_Attr):
    """Specifies the shape of the area"""

    shape: str | None = None


@dataclass
class Size(_Attr):
    """Specifies the width, in characters (for `<input>`), or the number of visible options (for `<select>`)"""

    size: list | str | None = None


@dataclass
class Sizes(_Attr):
    """Specifies the size of the linked resource"""

    sizes: list | str | None = None


@dataclass
class Slot(_Attr):
    """Assigns a slot in a shadow DOM shadow tree to an element"""

    slot: str | None = None


@dataclass
class Span(_Attr):
    """Specifies the number of columns to span"""

    span: str | int = 1


@dataclass
class Spellcheck(_Attr):
    """Specifies whether the element is to have its spelling and grammar checked or not"""

    spellcheck: str = "true"


@dataclass
class Src(_Attr):
    """Specifies the URL of the media file"""

    src: str | None = None


@dataclass
class Srcdoc(_Attr):
    """Specifies the HTML content of the page to show in the `<iframe>`"""

    srcdoc: str | None = None


@dataclass
class Srclang(_Attr):
    """Specifies the language of the track text data (required if `kind="subtitles"`)"""

    srclang: str | None = None


@dataclass
class Srcset(_Attr):
    """Specifies the URLs of the images to use in different situations"""

    srcset: list | str | None = None


@dataclass
class Start(_Attr):
    """Specifies the start value of an ordered list"""

    start: str | None = None


@dataclass
class Step(_Attr):
    """Specifies the legal number intervals for an input field"""

    step: str | None = None


@dataclass
class Style(_Attr):
    """Specifies an inline CSS style for an element"""

    style: str | None = None


@dataclass
class Tabindex(_Attr):
    """Specifies the tabbing order of an element"""

    tabindex: str | None = None


@dataclass
class Target(_Attr):
    """Specifies the target for where to open the linked document or where to submit the form"""

    target: str | None = None


@dataclass
class Title(_Attr):
    """Specifies extra information about an element"""

    title: str | None = None


@dataclass
class Translate(_Attr):
    """Specifies whether the content of an element should be translated or not"""

    translate: str = "yes"


@dataclass
class Type(_Attr):
    """Specifies the type of element"""

    type: str | None = None


@dataclass
class Usemap(_Attr):
    """Specifies an image as a client-side image map"""

    usemap: str | None = None


@dataclass
class Value(_Attr):
    """Specifies the value of the element"""

    value: str | None = None


@dataclass
class Virtualkeyboardpolicy(_Attr):
    """Controls the on-screen virtual keyboard behavior on devices where a hardware keyboard may not be available"""

    virtualkeyboardpolicy: str | None = None


@dataclass
class Webkitdirectory(_Attr):
    """Indicates that only directories should be available to be selected by the user in the file picker interface"""

    webkitdirectory: bool = False


@dataclass
class Width(_Attr):
    """Specifies the width of the element"""

    width: str | None = None


@dataclass
class Wrap(_Attr):
    """Specifies how the text in a text area is to be wrapped when submitted in a form"""

    wrap: str = "soft"


@dataclass
class Writingsuggestions(_Attr):
    """Indicates if browser-provided writing suggestions should be enabled"""

    writingsuggestions: str = "true"


@dataclass
class Xmlns(_Attr):
    """Specifies the XML Namespace of the document"""

    xmlns: str | None = None
