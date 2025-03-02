"""HTML tags as classes"""

from dataclasses import dataclass
from . import attributes as attr


@dataclass
class _Tag(
    attr.Accesskey,
    attr.Anchor,
    attr.AriaAttrs,
    attr.Autocapitalize,
    attr.Autocorrect,
    attr.Autofocus,
    attr.Class,
    attr.Contenteditable,
    attr.CustomAttrs,
    attr.DataAttrs,
    attr.Dir,
    attr.Draggable,
    attr.Enterkeyhint,
    attr.EventAttrs,
    attr.Exportparts,
    attr.Hidden,
    attr.Id,
    attr.Inert,
    attr.Inputmode,
    attr.Is,
    attr.Itemid,
    attr.Itemprop,
    attr.Itemref,
    attr.Itemscope,
    attr.Itemtype,
    attr.Lang,
    attr.Nonce,
    attr.Part,
    attr.Popover,
    attr.Role,
    attr.Slot,
    attr.Spellcheck,
    attr.Style,
    attr.Tabindex,
    attr.Title,
    attr.Translate,
    attr.Virtualkeyboardpolicy,
    attr.Writingsuggestions,
):
    """The highest-level parent class of all other elements that stores global attributes. Returns tag `<None />`. Don't use in production"""

    _tag: str | None = None

    def _attrs_to_str(self):
        """Stringifies attributes"""

        return super().__str__()

    def __str__(self) -> str:

        tag = str(self.__class__._tag)
        attrs = self._attrs_to_str()

        return f"<{tag}{attrs} />"


@dataclass
class _Container(
    _Tag,
    attr.InnerHtml,
):
    """The parent class of all container elements that stores global attributes and an `inner_html` placeholder. Returns tag `<None></None>`. Don't use in production"""

    def __str__(self) -> str:

        tag = str(self.__class__._tag)
        inner_html = attr.InnerHtml.__str__(self)
        attrs = _Tag._attrs_to_str(self)

        return f"<{tag}{attrs}>{inner_html}</{tag}>"


@dataclass
class Doctype:
    """Defines the document type, `<!DOCTYPE html>` (HTML5)"""

    def __str__(self) -> str:
        return "<!DOCTYPE html>"


@dataclass
class CommentHtml(attr.InnerHtml):
    """Defines an HTML comment, `<!-- -->`"""

    def __str__(self, *args, **kwargs) -> str:

        inner_html = attr.InnerHtml.__str__(self)

        return f"<!-- {inner_html} -->"


@dataclass
class A(
    _Container,
    attr.Attributionsrc,
    attr.Download,
    attr.Href,
    attr.Hreflang,
    attr.Ping,
    attr.Referrerpolicy,
    attr.Rel,
    attr.Target,
    attr.Type,
):
    """Defines a hyperlink"""

    _tag = "a"


@dataclass
class Abbr(_Container):
    """Defines an abbreviation or an acronym"""

    _tag = "abbr"


@dataclass
class Address(_Container):
    """Defines contact information for the author/owner of a document"""

    _tag = "address"


@dataclass
class Area(
    _Tag,
    attr.Alt,
    attr.Coords,
    attr.Download,
    attr.Href,
    attr.Ping,
    attr.Referrerpolicy,
    attr.Rel,
    attr.Shape,
    attr.Target,
):
    """Defines an area inside an image map"""

    _tag = "area"


@dataclass
class Article(_Container):
    """Defines an article"""

    _tag = "article"


@dataclass
class Aside(_Container):
    """Defines content aside from the page content"""

    _tag = "aside"


@dataclass
class Audio(
    _Container,
    attr.Autoplay,
    attr.Controls,
    attr.Controlslist,
    attr.Crossorigin,
    attr.Disableremoteplayback,
    attr.Loop,
    attr.Muted,
    attr.Preload,
    attr.Src,
):
    """Defines embedded sound content"""

    _tag = "audio"


@dataclass
class B(_Container):
    """Defines bold text"""

    _tag = "b"


@dataclass
class Base(
    _Tag,
    attr.Href,
    attr.Target,
):
    """Specifies the base URL/target for all relative URLs in a document"""

    _tag = "base"


@dataclass
class Bdi(_Container):
    """Isolates a part of text that might be formatted in a different direction"""

    _tag = "bdi"


@dataclass
class Bdo(_Container):
    """Overrides the current text direction"""

    _tag = "bdo"


@dataclass
class Blockquote(
    _Container,
    attr.Cite,
):
    """Defines a section that is quoted from another source"""

    _tag = "blockquote"


@dataclass
class Body(_Container):
    """Defines the document's body"""

    _tag = "body"


@dataclass
class Br(_Tag):
    """Defines a line break"""

    _tag = "br"


@dataclass
class Button(
    _Container,
    attr.Command,
    attr.Commandfor,
    attr.Disabled,
    attr.Form,
    attr.Formaction,
    attr.Formenctype,
    attr.Formmethod,
    attr.Formnovalidate,
    attr.Formtarget,
    attr.Name,
    attr.Popovertarget,
    attr.Popovertargetaction,
    attr.Type,
    attr.Value,
):
    """Defines a clickable button"""

    _tag = "button"


@dataclass
class Canvas(
    _Container,
    attr.Height,
    attr.Width,
):
    """Used to draw graphics, on the fly, via scripting (usually JavaScript)"""

    _tag = "canvas"


@dataclass
class Caption(_Container):
    """Defines a table caption"""

    _tag = "caption"


@dataclass
class Cite(_Container):
    """Defines the title of a work"""

    _tag = "cite"


@dataclass
class Code(_Container):
    """Defines a piece of computer code"""

    _tag = "code"


@dataclass
class Col(
    _Tag,
    attr.Span,
):
    """Specifies column properties for each column within a <colgroup> element"""

    _tag = "col"


@dataclass
class Colgroup(
    _Container,
    attr.Span,
):
    """Specifies a group of one or more columns in a table for formatting"""

    _tag = "colgroup"


@dataclass
class Data(
    _Container,
    attr.Value,
):
    """Adds a machine-readable translation of a given content"""

    _tag = "data"


@dataclass
class Datalist(_Container):
    """Specifies a list of pre-defined options for input controls"""

    _tag = "datalist"


@dataclass
class Dd(_Container):
    """Defines a description/value of a term in a description list"""

    _tag = "dd"


@dataclass
class Del(
    _Container,
    attr.Cite,
    attr.Datetime,
):
    """Defines text that has been deleted from a document"""

    _tag = "del"


@dataclass
class Details(
    _Container,
    attr.Open,
    attr.Name,
):
    """Defines additional details that the user can view or hide"""

    _tag = "details"


@dataclass
class Dfn(_Container):
    """Specifies a term that is going to be defined within the content"""

    _tag = "dfn"


@dataclass
class Dialog(
    _Container,
    attr.Open,
):
    """Defines a dialog box or window"""

    _tag = "dialog"


@dataclass
class Div(_Container):
    """Defines a section in a document"""

    _tag = "div"


@dataclass
class Dl(_Container):
    """Defines a description list"""

    _tag = "dl"


@dataclass
class Dt(_Container):
    """Defines a term/name in a description list"""

    _tag = "dt"


@dataclass
class Em(_Container):
    """Defines emphasized text"""

    _tag = "em"


@dataclass
class Embed(
    _Tag,
    attr.Height,
    attr.Src,
    attr.Type,
    attr.Width,
):
    """Defines a container for an external application"""

    _tag = "embed"


@dataclass
class Fencedframe(
    _Container,
    attr.Allow,
    attr.Height,
    attr.Width,
):
    """Represents a nested browsing context, embedding another HTML page into the current one"""

    _tag = "fencedframe"


@dataclass
class Fieldset(
    _Container,
    attr.Disabled,
    attr.Form,
    attr.Name,
):
    """Groups related elements in a form"""

    _tag = "fieldset"


@dataclass
class Figcaption(_Container):
    """Defines a caption for a `<figure>` element"""

    _tag = "figcaption"


@dataclass
class Figure(_Container):
    """Specifies self-contained content"""

    _tag = "figure"


@dataclass
class Footer(_Container):
    """Defines a footer for a document or section"""

    _tag = "footer"


@dataclass
class Form(
    _Container,
    attr.AcceptCharset,
    attr.Autocomplete,
    attr.Name,
    attr.Rel,
    attr.Action,
    attr.Enctype,
    attr.Method,
    attr.Novalidate,
    attr.Target,
):
    """Defines an HTML form for user input"""

    _tag = "form"


@dataclass
class H1(_Container):
    """Defines the highest-level HTML heading"""

    _tag = "h1"


@dataclass
class H2(_Container):
    """Defines an HTML heading"""

    _tag = "h2"


@dataclass
class H3(_Container):
    """Defines an HTML heading"""

    _tag = "h3"


@dataclass
class H4(_Container):
    """Defines an HTML heading"""

    _tag = "h4"


@dataclass
class H5(_Container):
    """Defines an HTML heading"""

    _tag = "h5"


@dataclass
class H6(_Container):
    """Defines the lowest-level HTML heading"""

    _tag = "h6"


@dataclass
class Head(_Container):
    """Contains metadata/information for the document"""

    _tag = "head"


@dataclass
class Header(_Container):
    """Defines a header for a document or section"""

    _tag = "header"


@dataclass
class Hgroup(_Container):
    """Defines a header and related content"""

    _tag = "hgroup"


@dataclass
class Hr(_Tag):
    """Defines a thematic change in the content"""

    _tag = "hr"


@dataclass
class Html(
    _Container,
    attr.Xmlns,
):
    """Defines the root of an HTML document"""

    _tag = "html"


@dataclass
class I(_Container):
    """Defines a part of text in an alternate voice or mood"""

    _tag = "i"


@dataclass
class Iframe(
    _Container,
    attr.Allow,
    attr.Browsingtopics,
    attr.Credentialless,
    attr.Csp,
    attr.Height,
    attr.Loading,
    attr.Name,
    attr.Referrerpolicy,
    attr.Sandbox,
    attr.Src,
    attr.Srcdoc,
    attr.Width,
):
    """Defines an inline frame"""

    _tag = "iframe"


@dataclass
class Img(
    _Tag,
    attr.Alt,
    attr.Attributionsrc,
    attr.Crossorigin,
    attr.Decoding,
    attr.Elementtiming,
    attr.Fetchpriority,
    attr.Height,
    attr.Ismap,
    attr.Loading,
    attr.Referrerpolicy,
    attr.Sizes,
    attr.Src,
    attr.Srcset,
    attr.Width,
    attr.Usemap,
):
    """Defines an image"""

    _tag = "img"


@dataclass
class Input(
    _Tag,
    attr.Accept,
    attr.Alt,
    attr.Autocomplete,
    attr.Capture,
    attr.Checked,
    attr.Dirname,
    attr.Disabled,
    attr.Form,
    attr.Formaction,
    attr.Formenctype,
    attr.Formmethod,
    attr.Formnovalidate,
    attr.Formtarget,
    attr.Height,
    attr.Incremental,
    attr.List,
    attr.Max,
    attr.Maxlength,
    attr.Min,
    attr.Minlength,
    attr.Multiple,
    attr.Name,
    attr.Orient,
    attr.Pattern,
    attr.Placeholder,
    attr.Popovertarget,
    attr.Popovertargetaction,
    attr.Readonly,
    attr.Results,
    attr.Required,
    attr.Size,
    attr.Src,
    attr.Step,
    attr.Type,
    attr.Value,
    attr.Webkitdirectory,
    attr.Width,
):
    """Defines an input control"""

    _tag = "input"


@dataclass
class Ins(
    _Container,
    attr.Cite,
    attr.Datetime,
):
    """Defines a text that has been inserted into a document"""

    _tag = "ins"


@dataclass
class Kbd(_Container):
    """Defines keyboard input"""

    _tag = "kbd"


@dataclass
class Label(
    _Container,
    attr.For,
):
    """Defines a label for an `<input>` element"""

    _tag = "label"


@dataclass
class Legend(_Container):
    """Defines a caption for a `<fieldset>` element"""

    _tag = "legend"


@dataclass
class Li(
    _Container,
    attr.Value,
):
    """Defines a list item"""

    _tag = "li"


@dataclass
class Link(
    _Tag,
    attr.As,
    attr.Blocking,
    attr.Crossorigin,
    attr.Disabled,
    attr.Fetchpriority,
    attr.Href,
    attr.Hreflang,
    attr.Imagesizes,
    attr.Imagesrcset,
    attr.Integrity,
    attr.Media,
    attr.Referrerpolicy,
    attr.Rel,
    attr.Sizes,
    attr.Type,
):
    """Defines the relationship between a document and an external resource"""

    _tag = "link"


@dataclass
class Main(_Container):
    """Specifies the main content of a document"""

    _tag = "main"


@dataclass
class Map(
    _Container,
    attr.Name,
):
    """Defines an image map"""

    _tag = "map"


@dataclass
class Mark(_Container):
    """Defines marked/highlighted text"""

    _tag = "mark"


@dataclass
class Menu(_Container):
    """Defines an unordered list"""

    _tag = "menu"


@dataclass
class Meta(
    _Tag,
    attr.Charset,
    attr.Content,
    attr.HttpEquiv,
    attr.Media,
    attr.Name,
):
    """Defines metadata about an HTML document"""

    _tag = "meta"


@dataclass
class Meter(
    _Container,
    attr.Value,
    attr.Min,
    attr.Max,
    attr.Low,
    attr.High,
    attr.Optimum,
    attr.Form,
):
    """Defines a scalar measurement within a known range (a gauge)"""

    _tag = "meter"


@dataclass
class Nav(_Container):
    """Defines navigation links"""

    _tag = "nav"


@dataclass
class Noscript(_Container):
    """Defines an alternate content for users that do not support client-side scripts"""

    _tag = "noscript"


@dataclass
class Object(
    _Container,
    attr.Data,
    attr.Form,
    attr.Height,
    attr.Name,
    attr.Type,
    attr.Width,
):
    """Defines a container for an external application"""

    _tag = "object"


@dataclass
class Ol(
    _Container,
    attr.Reversed,
    attr.Start,
    attr.Type,
):
    """Defines an ordered list"""

    _tag = "ol"


@dataclass
class Optgroup(
    _Container,
    attr.Disabled,
    attr.Label,
):
    """Defines a group of related options in a dropdown"""

    _tag = "optgroup"


@dataclass
class Option(
    _Container,
    attr.Disabled,
    attr.Label,
    attr.Selected,
    attr.Value,
):
    """Defines an option in a dropdown"""

    _tag = "option"


@dataclass
class Output(
    _Container,
    attr.For,
    attr.Form,
    attr.Name,
):
    """Defines the result of a calculation"""

    _tag = "output"


@dataclass
class P(_Container):
    """Defines a paragraph"""

    _tag = "p"


@dataclass
class Param(
    _Tag,
    attr.Name,
    attr.Value,
):
    """Defines a parameter for an object"""

    _tag = "param"


@dataclass
class Picture(_Container):
    """Defines a container for multiple image resources"""

    _tag = "picture"


@dataclass
class Pre(_Container):
    """Defines pre-formatted text"""

    _tag = "pre"


@dataclass
class Progress(
    _Container,
    attr.Max,
    attr.Value,
):
    """Represents the progress of a task"""

    _tag = "progress"


@dataclass
class Q(
    _Container,
    attr.Cite,
):
    """Defines a short quotation"""

    _tag = "q"


@dataclass
class Rp(_Container):
    """Defines what to show in browsers that do not support ruby annotations"""

    _tag = "rp"


@dataclass
class Rt(_Container):
    """Defines an explanation/pronunciation of characters"""

    _tag = "rt"


@dataclass
class Ruby(_Container):
    """Defines a ruby annotation"""

    _tag = "ruby"


@dataclass
class S(_Container):
    """Defines text that is no longer correct"""

    _tag = "s"


@dataclass
class Samp(_Container):
    """Defines sample output from a computer program"""

    _tag = "samp"


@dataclass
class Script(
    _Container,
    attr.Async,
    attr.Attributionsrc,
    attr.Blocking,
    attr.Crossorigin,
    attr.Defer,
    attr.Fetchpriority,
    attr.Integrity,
    attr.Nomodule,
    attr.Referrerpolicy,
    attr.Src,
    attr.Type,
):
    """Defines a client-side script"""

    _tag = "script"


@dataclass
class Search(_Container):
    """Defines a search section"""

    _tag = "search"


@dataclass
class Section(_Container):
    """Defines a section in a document"""

    _tag = "section"


@dataclass
class Select(
    _Container,
    attr.Autocomplete,
    attr.Disabled,
    attr.Form,
    attr.Multiple,
    attr.Name,
    attr.Required,
    attr.Size,
):
    """Defines a dropdown"""

    _tag = "select"


@dataclass
class Slot(
    _Container,
    attr.Name,
):
    """Defines a placeholder inside a web component with a separate markup"""

    _tag = "slot"


@dataclass
class Small(_Container):
    """Defines smaller text"""

    _tag = "small"


@dataclass
class Source(
    _Tag,
    attr.Type,
    attr.Src,
    attr.Srcset,
    attr.Sizes,
    attr.Media,
    attr.Height,
    attr.Width,
):
    """Defines multiple resources for media elements"""

    _tag = "source"


@dataclass
class Span(_Container):
    """Defines an inline section"""

    _tag = "span"


@dataclass
class Strong(_Container):
    """Defines important text"""

    _tag = "strong"


@dataclass
class Style(
    _Container,
    attr.Blocking,
    attr.Media,
):
    """Defines style information for a document"""

    _tag = "style"


@dataclass
class Sub(_Container):
    """Defines subscripted text"""

    _tag = "sub"


@dataclass
class Summary(_Container):
    """Defines a visible heading for a `<details>` element"""

    _tag = "summary"


@dataclass
class Sup(_Container):
    """Defines superscripted text"""

    _tag = "sup"


@dataclass
class Table(_Container):
    """Defines a table"""

    _tag = "table"


@dataclass
class Tbody(_Container):
    """Groups the body content in a table"""

    _tag = "tbody"


@dataclass
class Td(
    _Container,
    attr.Colspan,
    attr.Headers,
    attr.Rowspan,
):
    """Defines a cell in a table"""

    _tag = "td"


@dataclass
class Template(
    _Container,
    attr.Shadowrootclonable,
    attr.Shadowrootdelegatesfocus,
    attr.Shadowrootmode,
    attr.Shadowrootserializable,
):
    """Defines a container for content that should be hidden when the page loads"""

    _tag = "template"


@dataclass
class Textarea(
    _Container,
    attr.Autocomplete,
    attr.Cols,
    attr.Dirname,
    attr.Disabled,
    attr.Form,
    attr.Maxlength,
    attr.Minlength,
    attr.Name,
    attr.Placeholder,
    attr.Readonly,
    attr.Required,
    attr.Rows,
    attr.Wrap,
):
    """Defines a multiline text input area"""

    _tag = "textarea"


@dataclass
class Tfoot(_Container):
    """Groups the footer content in a table"""

    _tag = "tfoot"


@dataclass
class Th(
    _Container,
    attr.Abbr,
    attr.Colspan,
    attr.Headers,
    attr.Rowspan,
    attr.Scope,
):
    """Defines a header cell in a table"""

    _tag = "th"


@dataclass
class Thead(_Container):
    """Groups the header content in a table"""

    _tag = "thead"


@dataclass
class Time(
    _Container,
    attr.Datetime,
):
    """Defines a specific time (or datetime)"""

    _tag = "time"


@dataclass
class Title(_Container):
    """Defines a title for the document"""

    _tag = "title"


@dataclass
class Tr(_Container):
    """Defines a row in a table"""

    _tag = "tr"


@dataclass
class Track(
    _Tag,
    attr.Default,
    attr.Kind,
    attr.Label,
    attr.Src,
    attr.Srclang,
):
    """Defines text tracks for media elements"""

    _tag = "track"


@dataclass
class U(_Container):
    """Defines some text that is unarticulated and styled differently from normal text"""

    _tag = "u"


@dataclass
class Ul(_Container):
    """Defines an unordered list"""

    _tag = "ul"


@dataclass
class Var(_Container):
    """Defines a variable"""

    _tag = "var"


@dataclass
class Video(
    _Container,
    attr.Autoplay,
    attr.Controls,
    attr.Controlslist,
    attr.Crossorigin,
    attr.Disablepictureinpicture,
    attr.Disableremoteplayback,
    attr.Height,
    attr.Loop,
    attr.Muted,
    attr.Playsinline,
    attr.Poster,
    attr.Preload,
    attr.Src,
    attr.Width,
):
    """Defines embedded video content"""

    _tag = "video"


@dataclass
class Wbr(_Tag):
    """Defines a possible line-break"""

    _tag = "wbr"
