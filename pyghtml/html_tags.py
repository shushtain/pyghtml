"""HTML tags as classes"""

from dataclasses import dataclass, replace
from . import html_attributes as attr


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

    _tag = None

    def __str__(self, *args, **kwargs) -> str:

        tag = str(self.__class__._tag)

        attrs = ""

        for cls in self.__class__.mro():
            for key, value in self.__dict__.items():
                if key in cls.__dict__:
                    temp = f"{str(cls(value))}"
                    if temp != "":
                        attrs += f" {temp}"

        return f"<{tag}{attrs} />"


@dataclass
class _Container(
    _Tag,
    attr.InnerHTML,
):
    """The parent class of all container elements that stores global attributes and an `inner_html` placeholder. Returns tag `<None></None>`. Don't use in production"""

    def __str__(self) -> str:

        tag = str(self.__class__._tag)

        inner_html = attr.InnerHTML.__str__(self)

        attrs = ""

        for cls in self.__class__.mro():
            for key, value in self.__dict__.items():
                if key == "inner_html":
                    continue
                if key in cls.__dict__:
                    temp = f"{str(cls(value))}"
                    if temp != "":
                        attrs += f" {temp}"

        return f"<{tag}{attrs}>{inner_html}</{tag}>"

    def __add__(self, other):
        temp = self.inner_html[:]
        temp.append(other)
        return replace(self, inner_html=temp)

    def __iadd__(self, other):
        self.inner_html.append(other)
        return self


@dataclass
class Doctype:
    def __str__(self) -> str:
        return "<!DOCTYPE html>"


@dataclass
class CommentHTML(attr.InnerHTML):

    def __str__(self, *args, **kwargs) -> str:

        inner_html = attr.InnerHTML.__str__(self)

        return f"<!-- {inner_html} -->"

    def __add__(self, other):
        temp = self.inner_html[:]
        temp.append(other)
        return replace(self, inner_html=temp)

    def __iadd__(self, other):
        self.inner_html.append(other)
        return self


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
    _tag = "a"


@dataclass
class Abbr(_Container):
    _tag = "abbr"


@dataclass
class Address(_Container):
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
    _tag = "area"


@dataclass
class Article(_Container):
    _tag = "article"


@dataclass
class Aside(_Container):
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
    _tag = "audio"


@dataclass
class B(_Container):
    _tag = "b"


@dataclass
class Base(
    _Tag,
    attr.Href,
    attr.Target,
):
    _tag = "base"


@dataclass
class Bdi(_Container):
    _tag = "bdi"


@dataclass
class Bdo(_Container):
    _tag = "bdo"


@dataclass
class Blockquote(
    _Container,
    attr.Cite,
):
    _tag = "blockquote"


@dataclass
class Body(_Container):
    _tag = "body"


@dataclass
class Br(_Tag):
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
    _tag = "button"


@dataclass
class Canvas(
    _Container,
    attr.Height,
    attr.Width,
):
    _tag = "canvas"


@dataclass
class Caption(_Container):
    _tag = "caption"


@dataclass
class Cite(_Container):
    _tag = "cite"


@dataclass
class Code(_Container):
    _tag = "code"


@dataclass
class Col(
    _Tag,
    attr.Span,
):
    _tag = "col"


@dataclass
class Colgroup(
    _Container,
    attr.Span,
):
    _tag = "colgroup"


@dataclass
class Data(
    _Container,
    attr.Value,
):
    _tag = "data"


@dataclass
class Datalist(_Container):
    _tag = "datalist"


@dataclass
class Dd(_Container):
    _tag = "dd"


@dataclass
class Del(
    _Container,
    attr.Cite,
    attr.Datetime,
):
    _tag = "del"


@dataclass
class Details(
    _Container,
    attr.Open,
    attr.Name,
):
    _tag = "details"


@dataclass
class Dfn(_Container):
    _tag = "dfn"


@dataclass
class Dialog(
    _Container,
    attr.Open,
):
    _tag = "dialog"


@dataclass
class Div(_Container):
    _tag = "div"


@dataclass
class Dl(_Container):
    _tag = "dl"


@dataclass
class Dt(_Container):
    _tag = "dt"


@dataclass
class Em(_Container):
    _tag = "em"


@dataclass
class Embed(
    _Tag,
    attr.Height,
    attr.Src,
    attr.Type,
    attr.Width,
):
    _tag = "embed"


@dataclass
class Fencedframe(
    _Container,
    attr.Allow,
    attr.Height,
    attr.Width,
):
    _tag = "fencedframe"


@dataclass
class Fieldset(
    _Container,
    attr.Disabled,
    attr.Form,
    attr.Name,
):
    _tag = "fieldset"


@dataclass
class Figcaption(_Container):
    _tag = "figcaption"


@dataclass
class Figure(_Container):
    _tag = "figure"


@dataclass
class Footer(_Container):
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
    _tag = "form"


@dataclass
class H1(_Container):
    _tag = "h1"


@dataclass
class H2(_Container):
    _tag = "h2"


@dataclass
class H3(_Container):
    _tag = "h3"


@dataclass
class H4(_Container):
    _tag = "h4"


@dataclass
class H5(_Container):
    _tag = "h5"


@dataclass
class H6(_Container):
    _tag = "h6"


@dataclass
class Head(_Container):
    _tag = "head"


@dataclass
class Header(_Container):
    _tag = "header"


@dataclass
class Hgroup(_Container):
    _tag = "hgroup"


@dataclass
class Hr(_Tag):
    _tag = "hr"


@dataclass
class Html(
    _Container,
    attr.Xmlns,
):
    _tag = "html"


@dataclass
class I(_Container):
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
    _tag = "input"


@dataclass
class Ins(
    _Container,
    attr.Cite,
    attr.Datetime,
):
    _tag = "ins"


@dataclass
class Kbd(_Container):
    _tag = "kbd"


@dataclass
class Label(
    _Container,
    attr.For,
):
    _tag = "label"


@dataclass
class Legend(_Container):
    _tag = "legend"


@dataclass
class Li(
    _Container,
    attr.Value,
):
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
    _tag = "link"


@dataclass
class Main(_Container):
    _tag = "main"


@dataclass
class Map(
    _Container,
    attr.Name,
):
    _tag = "map"


@dataclass
class Mark(_Container):
    _tag = "mark"


@dataclass
class Menu(_Container):
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
    _tag = "meter"


@dataclass
class Nav(_Container):
    _tag = "nav"


@dataclass
class Noscript(_Container):
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
    _tag = "object"


@dataclass
class Ol(
    _Container,
    attr.Reversed,
    attr.Start,
    attr.Type,
):
    _tag = "ol"


@dataclass
class Optgroup(
    _Container,
    attr.Disabled,
    attr.Label,
):
    _tag = "optgroup"


@dataclass
class Option(
    _Container,
    attr.Disabled,
    attr.Label,
    attr.Selected,
    attr.Value,
):
    _tag = "option"


@dataclass
class Output(
    _Container,
    attr.For,
    attr.Form,
    attr.Name,
):
    _tag = "output"


@dataclass
class P(_Container):
    _tag = "p"


@dataclass
class Param(
    _Tag,
    attr.Name,
    attr.Value,
):
    _tag = "param"


@dataclass
class Picture(_Container):
    _tag = "picture"


@dataclass
class Pre(_Container):
    _tag = "pre"


@dataclass
class Progress(
    _Container,
    attr.Max,
    attr.Value,
):
    _tag = "progress"


@dataclass
class Q(
    _Container,
    attr.Cite,
):
    _tag = "q"


@dataclass
class Rp(_Container):
    _tag = "rp"


@dataclass
class Rt(_Container):
    _tag = "rt"


@dataclass
class Ruby(_Container):
    _tag = "ruby"


@dataclass
class S(_Container):
    _tag = "s"


@dataclass
class Samp(_Container):
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
    _tag = "script"


@dataclass
class Search(_Container):
    _tag = "search"


@dataclass
class Section(_Container):
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
    _tag = "select"


@dataclass
class Slot(
    _Container,
    attr.Name,
):
    _tag = "slot"


@dataclass
class Small(_Container):
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
    _tag = "source"


@dataclass
class Span(_Container):
    _tag = "span"


@dataclass
class Strong(_Container):
    _tag = "strong"


@dataclass
class Style(
    _Container,
    attr.Blocking,
    attr.Media,
):
    _tag = "style"


@dataclass
class Sub(_Container):
    _tag = "sub"


@dataclass
class Summary(_Container):
    _tag = "summary"


@dataclass
class Sup(_Container):
    _tag = "sup"


@dataclass
class Table(_Container):
    _tag = "table"


@dataclass
class Tbody(_Container):
    _tag = "tbody"


@dataclass
class Td(
    _Container,
    attr.Colspan,
    attr.Headers,
    attr.Rowspan,
):
    _tag = "td"


@dataclass
class Template(
    _Container,
    attr.Shadowrootclonable,
    attr.Shadowrootdelegatesfocus,
    attr.Shadowrootmode,
    attr.Shadowrootserializable,
):
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
    _tag = "textarea"


@dataclass
class Tfoot(_Container):
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
    _tag = "th"


@dataclass
class Thead(_Container):
    _tag = "thead"


@dataclass
class Time(
    _Container,
    attr.Datetime,
):
    _tag = "time"


@dataclass
class Title(_Container):
    _tag = "title"


@dataclass
class Tr(_Container):
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
    _tag = "track"


@dataclass
class U(_Container):
    _tag = "u"


@dataclass
class Ul(_Container):
    _tag = "ul"


@dataclass
class Var(_Container):
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
    _tag = "video"


@dataclass
class Wbr(_Tag):
    _tag = "wbr"
