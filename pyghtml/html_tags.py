from dataclasses import dataclass, replace
import html_attributes as a


@dataclass
class _Tag(
    a.Accesskey,
    a.Anchor,
    a.Aria_attrs,
    a.Autocapitalize,
    a.Autocorrect,
    a.Autofocus,
    a.Class_attr,
    a.Contenteditable,
    a.Custom_attrs,
    a.Data_attrs,
    a.Dir,
    a.Draggable,
    a.Enterkeyhint,
    a.Event_attrs,
    a.Exportparts,
    a.Hidden,
    a.Id,
    a.Inert,
    a.Inputmode,
    a.Is_attr,
    a.Itemid,
    a.Itemprop,
    a.Itemref,
    a.Itemscope,
    a.Itemtype,
    a.Lang,
    a.Nonce,
    a.Part,
    a.Popover,
    a.Role,
    a.Slot,
    a.Spellcheck,
    a.Style,
    a.Tabindex,
    a.Title,
    a.Translate,
    a.Virtualkeyboardpolicy,
    a.Writingsuggestions,
):
    _tag = None

    def __str__(self):

        tag = str(self.__class__._tag)

        attrs = ""
        for key, value in self.__dict__.items():
            attrs += f" {str(value)}"

        return f"<{tag}{attrs} />"


@dataclass
class _Container(_Tag, a.InnerHTML):

    def __str__(self):

        tag = str(self.__class__._tag)

        inner_html = a.InnerHTML.__str__(self)

        attrs = ""

        for cls in self.__class__.mro():
            for key, value in self.__dict__.items():
                if key == "innerHTML":
                    continue
                if key in cls.__dict__:
                    attrs += f" {str(cls(value))}"

        return f"<{tag}{attrs}>{inner_html}</{tag}>"

    def __add__(self, other):
        temp = self.innerHTML[:]
        temp.append(other)
        return replace(self, innerHTML=temp)

    def __iadd__(self, other):
        self.innerHTML.append(other)
        return self


@dataclass
class Doctype:
    def __str__(self):
        return f"<!DOCTYPE html>"


@dataclass
class A(
    _Container,
    a.Attributionsrc,
    a.Download,
    a.Href,
    a.Hreflang,
    a.Ping,
    a.Referrerpolicy,
    a.Rel,
    a.Target,
    a.Type,
):
    _tag = "a"


@dataclass
class Attr(_Container):
    _tag = "attr"


@dataclass
class Address(_Container):
    _tag = "address"


@dataclass
class Area(
    _Tag,
    a.Alt,
    a.Coords,
    a.Download,
    a.Href,
    a.Ping,
    a.Referrerpolicy,
    a.Rel,
    a.Shape,
    a.Target,
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
    a.Autoplay,
    a.Controls,
    a.Controlslist,
    a.Crossorigin,
    a.Disableremoteplayback,
    a.Loop,
    a.Muted,
    a.Preload,
    a.Src,
):
    _tag = "audio"


@dataclass
class B(_Container):
    _tag = "b"


@dataclass
class Base(_Tag, a.Href, a.Target):
    _tag = "base"


@dataclass
class bdi(_Container):
    _tag = "bdi"


@dataclass
class bdo(_Container):
    _tag = "bdo"


@dataclass
class blockquote(_Container, a.Cite):
    _tag = "blockquote"


@dataclass
class body(_Container):
    _tag = "body"


@dataclass
class br(_Tag):
    _tag = "br"


@dataclass
class button(
    _Container,
    a.Command,
    a.Commandfor,
    a.Disabled,
    a.Form,
    a.Formaction,
    a.Formenctype,
    a.Formmethod,
    a.Formnovalidate,
    a.Formtarget,
    a.Name,
    a.Popovertarget,
    a.Popovertargetaction,
    a.Type,
    a.Value,
):
    _tag = "button"


@dataclass
class canvas(_Container, a.Height, a.Width):
    _tag = "canvas"


@dataclass
class caption(_Container):
    _tag = "caption"


@dataclass
class cite(_Container):
    _tag = "cite"


@dataclass
class code(_Container):
    _tag = "code"


@dataclass
class col(_Tag, a.Span):
    _tag = "col"


@dataclass
class colgroup(_Container, a.Span):
    _tag = "colgroup"


@dataclass
class data(_Container, a.Value):
    _tag = "data"


@dataclass
class datalist(_Container):
    _tag = "datalist"


@dataclass
class dd(_Container):
    _tag = "dd"


@dataclass
class Del(_Container, a.Cite, a.Datetime):
    _tag = "del"


@dataclass
class details(_Container, a.Open, a.Name):
    _tag = "details"


@dataclass
class dfn(_Container):
    _tag = "dfn"


@dataclass
class dialog(_Container, a.Open):
    _tag = "dialog"


@dataclass
class div(_Container):
    _tag = "div"


@dataclass
class dl(_Container):
    _tag = "dl"


@dataclass
class dt(_Container):
    _tag = "dt"
