class _Global:
    """The highest-order parent class of all other elements that stores global attributes. Returns tag None. Don't use in production."""

    _tag = None

    def __init__(
        self,
        *,
        accesskey: str = None,
        anchor: str = None,
        aria_attributes: dict = None,
        autocapitalize: str = "none",
        autocorrect: str = "on",
        autofocus: bool = False,
        class_attr: str = None,
        contenteditable: str = None,
        custom_attributes: dict = None,
        data_attributes: dict = None,
        dir: str = None,
        draggable: str = None,
        enterkeyhint: str = None,
        event_attributes: dict = None,
        exportparts: str = None,
        hidden: bool = False,
        id: str = None,
        inert: bool = False,
        inputmode: str = None,
        is_attr: str = None,
        itemid: str = None,
        itemprop: str = None,
        itemref: str = None,
        itemscope: bool = False,
        itemtype: str = None,
        lang: str = None,
        nonce: str = None,
        part: str = None,
        popover: str = None,
        role: str = None,
        slot: str = None,
        spellcheck: str = "true",
        style: str = None,
        tabindex: str = None,
        title: str = None,
        translate: str = "yes",
        virtualkeyboardpolicy: str = None,
        writingsuggestions: str = "true",
    ):
        self.accesskey = accesskey
        self.anchor = anchor
        self.aria_attributes = aria_attributes
        self.autocapitalize = autocapitalize
        self.autocorrect = autocorrect
        self.autofocus = autofocus
        self.class_attr = class_attr
        self.contenteditable = contenteditable
        self.custom_attributes = custom_attributes
        self.data_attributes = data_attributes
        self.dir = dir
        self.draggable = draggable
        self.enterkeyhint = enterkeyhint
        self.event_attributes = event_attributes
        self.exportparts = exportparts
        self.hidden = hidden
        self.id = id
        self.inert = inert
        self.inputmode = inputmode
        self.is_attr = is_attr
        self.itemid = itemid
        self.itemprop = itemprop
        self.itemref = itemref
        self.itemscope = itemscope
        self.itemtype = itemtype
        self.lang = lang
        self.nonce = nonce
        self.part = part
        self.popover = popover
        self.role = role
        self.slot = slot
        self.spellcheck = spellcheck
        self.style = style
        self.tabindex = tabindex
        self.title = title
        self.translate = translate
        self.virtualkeyboardpolicy = virtualkeyboardpolicy
        self.writingsuggestions = writingsuggestions

    @property
    def accesskey(self):
        return self._accesskey[1]

    @accesskey.setter
    def accesskey(self, accesskey):
        self._accesskey = [None, accesskey, "accesskey"]

    @property
    def anchor(self):
        return self._anchor[1]

    @anchor.setter
    def anchor(self, anchor):
        self._anchor = [None, anchor, "anchor"]

    @property
    def aria_attributes(self):
        return self._aria_attributes[1]

    @aria_attributes.setter
    def aria_attributes(self, aria_attributes):
        self._aria_attributes = [None, aria_attributes, ""]

    @property
    def autocapitalize(self):
        return self._autocapitalize[1]

    @autocapitalize.setter
    def autocapitalize(self, autocapitalize):
        self._autocapitalize = ["none", autocapitalize, "autocapitalize"]

    @property
    def autocorrect(self):
        return self._autocorrect[1]

    @autocorrect.setter
    def autocorrect(self, autocorrect):
        self._autocorrect = ["on", autocorrect, "autocorrect"]

    @property
    def autofocus(self):
        return self._autofocus[1]

    @autofocus.setter
    def autofocus(self, autofocus):
        self._autofocus = [False, autofocus, "autofocus"]

    @property
    def class_attr(self):
        return self._class_attr[1]

    @class_attr.setter
    def class_attr(self, class_attr):
        self._class_attr = [None, class_attr, "class"]

    @property
    def contenteditable(self):
        return self._contenteditable[1]

    @contenteditable.setter
    def contenteditable(self, contenteditable):
        self._contenteditable = [None, contenteditable, "contenteditable"]

    @property
    def custom_attributes(self):
        return self._custom_attributes[1]

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        self._custom_attributes = [None, custom_attributes, ""]

    @property
    def data_attributes(self):
        return self._data_attributes[1]

    @data_attributes.setter
    def data_attributes(self, data_attributes):
        self._data_attributes = [None, data_attributes, ""]

    @property
    def dir(self):
        return self._dir[1]

    @dir.setter
    def dir(self, dir):
        self._dir = [None, dir, "dir"]

    @property
    def draggable(self):
        return self._draggable[1]

    @draggable.setter
    def draggable(self, draggable):
        self._draggable = [None, draggable, "draggable"]

    @property
    def enterkeyhint(self):
        return self._enterkeyhint[1]

    @enterkeyhint.setter
    def enterkeyhint(self, enterkeyhint):
        self._enterkeyhint = [None, enterkeyhint, "enterkeyhint"]

    @property
    def event_attributes(self):
        return self._event_attributes[1]

    @event_attributes.setter
    def event_attributes(self, event_attributes):
        self._event_attributes = [None, event_attributes, "event_attributes"]

    @property
    def exportparts(self):
        return self._exportparts[1]

    @exportparts.setter
    def exportparts(self, exportparts):
        self._exportparts = [None, exportparts, "exportparts"]

    @property
    def hidden(self):
        return self._hidden[1]

    @hidden.setter
    def hidden(self, hidden):
        self._hidden = [False, hidden, "hidden"]

    @property
    def id(self):
        return self._id[1]

    @id.setter
    def id(self, id):
        self._id = [None, id, "id"]

    @property
    def inert(self):
        return self._inert[1]

    @inert.setter
    def inert(self, inert):
        self._inert = [False, inert, "inert"]

    @property
    def inputmode(self):
        return self._inputmode[1]

    @inputmode.setter
    def inputmode(self, inputmode):
        self._inputmode = [None, inputmode, "inputmode"]

    @property
    def is_attr(self):
        return self._is_attr[1]

    @is_attr.setter
    def is_attr(self, is_attr):
        self._is_attr = [None, is_attr, "is"]

    @property
    def itemid(self):
        return self._itemid[1]

    @itemid.setter
    def itemid(self, itemid):
        self._itemid = [None, itemid, "itemid"]

    @property
    def itemprop(self):
        return self._itemprop[1]

    @itemprop.setter
    def itemprop(self, itemprop):
        self._itemprop = [None, itemprop, "itemprop"]

    @property
    def itemref(self):
        return self._itemref[1]

    @itemref.setter
    def itemref(self, itemref):
        self._itemref = [None, itemref, "itemref"]

    @property
    def itemscope(self):
        return self._itemscope[1]

    @itemscope.setter
    def itemscope(self, itemscope):
        self._itemscope = [False, itemscope, "itemscope"]

    @property
    def itemtype(self):
        return self._itemtype[1]

    @itemtype.setter
    def itemtype(self, itemtype):
        self._itemtype = [None, itemtype, "itemtype"]

    @property
    def lang(self):
        return self._lang[1]

    @lang.setter
    def lang(self, lang):
        self._lang = [None, lang, "lang"]

    @property
    def nonce(self):
        return self._nonce[1]

    @nonce.setter
    def nonce(self, nonce):
        self._nonce = [None, nonce, "nonce"]

    @property
    def part(self):
        return self._part[1]

    @part.setter
    def part(self, part):
        self._part = [None, part, "part"]

    @property
    def popover(self):
        return self._popover[1]

    @popover.setter
    def popover(self, popover):
        self._popover = [None, popover, "popover"]

    @property
    def role(self):
        return self._role[1]

    @role.setter
    def role(self, role):
        self._role = [None, role, "role"]

    @property
    def slot(self):
        return self._slot[1]

    @slot.setter
    def slot(self, slot):
        self._slot = [None, slot, "slot"]

    @property
    def spellcheck(self):
        return self._spellcheck[1]

    @spellcheck.setter
    def spellcheck(self, spellcheck):
        self._spellcheck = ["true", spellcheck, "spellcheck"]

    @property
    def style(self):
        return self._style[1]

    @style.setter
    def style(self, style):
        self._style = [None, style, "style"]

    @property
    def tabindex(self):
        return self._tabindex[1]

    @tabindex.setter
    def tabindex(self, tabindex):
        self._tabindex = [None, tabindex, "tabindex"]

    @property
    def title(self):
        return self._title[1]

    @title.setter
    def title(self, title):
        self._title = [None, title, "title"]

    @property
    def translate(self):
        return self._translate[1]

    @translate.setter
    def translate(self, translate):
        self._translate = ["yes", translate, "translate"]

    @property
    def virtualkeyboardpolicy(self):
        return self._virtualkeyboardpolicy[1]

    @virtualkeyboardpolicy.setter
    def virtualkeyboardpolicy(self, virtualkeyboardpolicy):
        self._virtualkeyboardpolicy = [
            None,
            virtualkeyboardpolicy,
            "virtualkeyboardpolicy",
        ]

    @property
    def writingsuggestions(self):
        return self._writingsuggestions[1]

    @writingsuggestions.setter
    def writingsuggestions(self, writingsuggestions):
        self._writingsuggestions = ["true", writingsuggestions, "writingsuggestions"]

    @staticmethod
    def _attr_to_string(key, value):

        if value[1] == value[0]:
            return ""

        if isinstance(value[1], str):
            return f' {str(value[2])}="{str(value[1])}"'
        elif isinstance(value[1], dict):
            temp = ""
            for k, v in value[1].items():
                if isinstance(v, str):
                    temp += f' {str(k)}="{str(v)}"'
                elif isinstance(v, bool) and v:
                    temp += f" {str(k)}"
            return temp
        elif isinstance(value[1], bool) and value[1]:
            return f" {str(value[2])}"

        return ""

    def __str__(self):

        tag = str(self.__class__._tag)

        attrs = ""
        for key, value in self.__dict__.items():
            attrs += _Global._attr_to_string(key, value)

        return f"<{tag}{attrs} />"


class _Container(_Global):
    """The parent class of all container elements. Returns tag None. Don't use in production."""

    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        innerHTML: list = [],
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
        )
        self.innerHTML = innerHTML

    @property
    def innerHTML(self):
        return self._innerHTML

    @innerHTML.setter
    def innerHTML(self, innerHTML):
        self._innerHTML = innerHTML

    def __str__(self):

        tag = str(self.__class__._tag)

        innerHTML = ""
        for elem in self.innerHTML:
            innerHTML += str(elem)

        attrs = ""
        for key, value in self.__dict__.items():

            if key == "_innerHTML":
                continue

            attrs += self._attr_to_string(key, value)

        return f"<{tag}{attrs}>{innerHTML}</{tag}>"

    def __add__(self, other):
        self.innerHTML.append(other)

    def __iadd__(self, other):
        self.innerHTML.append(other)


class Doctype:
    """Returns HTML5 variant."""

    def __str__(self):
        return f"<!DOCTYPE html>"


class A(_Container):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        innerHTML=[],
        attributionsrc: bool | str = None,
        download: bool | str = False,
        href: str = None,
        hreflang: str = None,
        ping: str = None,
        referrerpolicy: str = None,
        rel: str = None,
        target: str = None,
        type: str = None,
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
            innerHTML=innerHTML,
        )
        self.attributionsrc = attributionsrc
        self.download = download
        self.href = href
        self.hreflang = hreflang
        self.ping = ping
        self.referrerpolicy = referrerpolicy
        self.rel = rel
        self.target = target
        self.type = type

    @property
    def attributionsrc(self):
        return self._attributionsrc[1]

    @attributionsrc.setter
    def attributionsrc(self, attributionsrc):
        self._attributionsrc = [None, attributionsrc, "attributionsrc"]

    @property
    def download(self):
        return self._download[1]

    @download.setter
    def download(self, download):
        self._download = [False, download, "download"]

    @property
    def href(self):
        return self._href[1]

    @href.setter
    def href(self, href):
        self._href = [None, href, "href"]

    @property
    def hreflang(self):
        return self._hreflang[1]

    @hreflang.setter
    def hreflang(self, hreflang):
        self._hreflang = [None, hreflang, "hreflang"]

    @property
    def ping(self):
        return self._ping[1]

    @ping.setter
    def ping(self, ping):
        self._ping = [None, ping, "ping"]

    @property
    def referrerpolicy(self):
        return self._referrerpolicy[1]

    @referrerpolicy.setter
    def referrerpolicy(self, referrerpolicy):
        self._referrerpolicy = [None, referrerpolicy, "referrerpolicy"]

    @property
    def rel(self):
        return self._rel[1]

    @rel.setter
    def rel(self, rel):
        self._rel = [None, rel, "rel"]

    @property
    def target(self):
        return self._target[1]

    @target.setter
    def target(self, target):
        self._target = [None, target, "target"]

    @property
    def type(self):
        return self._type[1]

    @type.setter
    def type(self, type):
        self._type = [None, type, "type"]


class Attr(_Container): ...


class Address(_Container): ...


class Area(_Global):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        alt: str = None,
        coords: str = None,
        download: bool | str = False,
        href: str = None,
        ping: str = None,
        referrerpolicy: str = None,
        rel: str = None,
        shape: str = None,
        target: str = None,
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
        )
        self.alt = alt
        self.coords = coords
        self.download = download
        self.href = href
        self.ping = ping
        self.referrerpolicy = referrerpolicy
        self.rel = rel
        self.shape = shape
        self.target = target

    @property
    def alt(self):
        return self._alt[1]

    @alt.setter
    def alt(self, alt):
        self._alt = [None, alt, "alt"]

    @property
    def coords(self):
        return self._coords[1]

    @coords.setter
    def coords(self, coords):
        self._coords = [None, coords, "coords"]

    @property
    def download(self):
        return self._download[1]

    @download.setter
    def download(self, download):
        self._download = [False, download, "download"]

    @property
    def href(self):
        return self._href[1]

    @href.setter
    def href(self, href):
        self._href = [None, href, "href"]

    @property
    def ping(self):
        return self._ping[1]

    @ping.setter
    def ping(self, ping):
        self._ping = [None, ping, "ping"]

    @property
    def referrerpolicy(self):
        return self._referrerpolicy[1]

    @referrerpolicy.setter
    def referrerpolicy(self, referrerpolicy):
        self._referrerpolicy = [None, referrerpolicy, "referrerpolicy"]

    @property
    def rel(self):
        return self._rel[1]

    @rel.setter
    def rel(self, rel):
        self._rel = [None, rel, "rel"]

    @property
    def shape(self):
        return self._shape[1]

    @shape.setter
    def shape(self, shape):
        self._shape = [None, shape, "shape"]

    @property
    def target(self):
        return self._target[1]

    @target.setter
    def target(self, target):
        self._target = [None, target, "target"]


class Article(_Container): ...


class Aside(_Container): ...


class Audio(_Container):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        innerHTML=[],
        autoplay: bool = False,
        controls: bool = False,
        controlslist: str = None,
        crossorigin: str = None,
        disableremoteplayback: bool = False,
        loop: bool = False,
        muted: bool = False,
        preload: str = None,
        src: str = None,
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
            innerHTML=innerHTML,
        )
        self.autoplay = autoplay
        self.controls = controls
        self.controlslist = controlslist
        self.crossorigin = crossorigin
        self.disableremoteplayback = disableremoteplayback
        self.loop = loop
        self.muted = muted
        self.preload = preload
        self.src = src

    @property
    def autoplay(self):
        return self._autoplay[1]

    @autoplay.setter
    def autoplay(self, autoplay):
        self._autoplay = [False, autoplay, "autoplay"]

    @property
    def controls(self):
        return self._controls[1]

    @controls.setter
    def controls(self, controls):
        self._controls = [False, controls, "controls"]

    @property
    def controlslist(self):
        return self._controlslist[1]

    @controlslist.setter
    def controlslist(self, controlslist):
        self._controlslist = [None, controlslist, "controlslist"]

    @property
    def crossorigin(self):
        return self._crossorigin[1]

    @crossorigin.setter
    def crossorigin(self, crossorigin):
        self._crossorigin = [None, crossorigin, "crossorigin"]

    @property
    def disableremoteplayback(self):
        return self._disableremoteplayback[1]

    @disableremoteplayback.setter
    def disableremoteplayback(self, disableremoteplayback):
        self._disableremoteplayback = [
            False,
            disableremoteplayback,
            "disableremoteplayback",
        ]

    @property
    def loop(self):
        return self._loop[1]

    @loop.setter
    def loop(self, loop):
        self._loop = [False, loop, "loop"]

    @property
    def muted(self):
        return self._muted[1]

    @muted.setter
    def muted(self, muted):
        self._muted = [False, muted, "muted"]

    @property
    def preload(self):
        return self._preload[1]

    @preload.setter
    def preload(self, preload):
        self._preload = [None, preload, "preload"]

    @property
    def src(self):
        return self._src[1]

    @src.setter
    def src(self, src):
        self._src = [None, src, "src"]


class B(_Container): ...


class Base(_Global):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        href: str = None,
        target: str = None,
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
        )
        self.href = href
        self.target = target

    @property
    def href(self):
        return self._href[1]

    @href.setter
    def href(self, href):
        self._href = [None, href, "href"]

    @property
    def target(self):
        return self._target[1]

    @target.setter
    def target(self, target):
        self._target = [None, target, "target"]


class Bdi(_Container): ...


class Bdo(_Container): ...


class Blockquote(_Container):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        innerHTML=[],
        cite: str = None,
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
            innerHTML=innerHTML,
        )
        self.cite = cite

    @property
    def cite(self):
        return self._cite[1]

    @cite.setter
    def cite(self, cite):
        self._cite = [None, cite, "cite"]


class Body(_Container): ...


class Br(_Global): ...


class Button(_Container):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        innerHTML=[],
        command: str = None,
        commandfor: str = None,
        disabled: bool = False,
        form: str = None,
        formaction: str = None,
        formenctype: str = None,
        formmethod: str = None,
        formnovalidate: bool = False,
        formtarget: str = None,
        name: str = None,
        popovertarget: str = None,
        popovertargetaction: str = None,
        type: str = None,
        value: str = None,
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
            innerHTML=innerHTML,
        )
        self.command = command
        self.commandfor = commandfor
        self.disabled = disabled
        self.form = form
        self.formaction = formaction
        self.formenctype = formenctype
        self.formmethod = formmethod
        self.formnovalidate = formnovalidate
        self.formtarget = formtarget
        self.name = name
        self.popovertarget = popovertarget
        self.popovertargetaction = popovertargetaction
        self.type = type
        self.value = value

    @property
    def command(self):
        return self._command[1]

    @command.setter
    def command(self, command):
        self._command = [None, command, "command"]

    @property
    def commandfor(self):
        return self._commandfor[1]

    @commandfor.setter
    def commandfor(self, commandfor):
        self._commandfor = [None, commandfor, "commandfor"]

    @property
    def disabled(self):
        return self._disabled[1]

    @disabled.setter
    def disabled(self, disabled):
        self._disabled = [False, disabled, "disabled"]

    @property
    def form(self):
        return self._form[1]

    @form.setter
    def form(self, form):
        self._form = [None, form, "form"]

    @property
    def formaction(self):
        return self._formaction[1]

    @formaction.setter
    def formaction(self, formaction):
        self._formaction = [None, formaction, "formaction"]

    @property
    def formenctype(self):
        return self._formenctype[1]

    @formenctype.setter
    def formenctype(self, formenctype):
        self._formenctype = [None, formenctype, "formenctype"]

    @property
    def formmethod(self):
        return self._formmethod[1]

    @formmethod.setter
    def formmethod(self, formmethod):
        self._formmethod = [None, formmethod, "formmethod"]

    @property
    def formnovalidate(self):
        return self._formnovalidate[1]

    @formnovalidate.setter
    def formnovalidate(self, formnovalidate):
        self._formnovalidate = [False, formnovalidate, "formnovalidate"]

    @property
    def formtarget(self):
        return self._formtarget[1]

    @formtarget.setter
    def formtarget(self, formtarget):
        self._formtarget = [None, formtarget, "formtarget"]

    @property
    def name(self):
        return self._name[1]

    @name.setter
    def name(self, name):
        self._name = [None, name, "name"]

    @property
    def popovertarget(self):
        return self._popovertarget[1]

    @popovertarget.setter
    def popovertarget(self, popovertarget):
        self._popovertarget = [None, popovertarget, "popovertarget"]

    @property
    def popovertargetaction(self):
        return self._popovertargetaction[1]

    @popovertargetaction.setter
    def popovertargetaction(self, popovertargetaction):
        self._popovertargetaction = [None, popovertargetaction, "popovertargetaction"]

    @property
    def type(self):
        return self._type[1]

    @type.setter
    def type(self, type):
        self._type = [None, type, "type"]

    @property
    def value(self):
        return self._value[1]

    @value.setter
    def value(self, value):
        self._value = [None, value, "value"]


class Canvas(_Container):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        innerHTML=[],
        height: str = None,
        width: str = None,
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
            innerHTML=innerHTML,
        )
        self.height = height
        self.width = width

    @property
    def height(self):
        return self._height[1]

    @height.setter
    def height(self, height):
        self._height = [None, height, "height"]

    @property
    def width(self):
        return self._width[1]

    @width.setter
    def width(self, width):
        self._width = [None, width, "width"]


class Caption(_Container): ...


class Cite(_Container): ...


class Code(_Container): ...


class Col(_Global):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        span: str = "1",
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
        )
        self.span = span

    @property
    def span(self):
        return self._span[1]

    @span.setter
    def span(self, span):
        self._span = ["1", span, "span"]


class Colgroup(_Container):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        innerHTML=[],
        span: str = "1",
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
            innerHTML=innerHTML,
        )
        self.span = span

    @property
    def span(self):
        return self._span[1]

    @span.setter
    def span(self, span):
        self._span = ["1", span, "span"]


class Data(_Container):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        innerHTML=[],
        value: str = None,
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
            innerHTML=innerHTML,
        )
        self.value = value

    @property
    def value(self):
        return self._value[1]

    @value.setter
    def value(self, value):
        self._value = [None, value, "value"]


class Datalist(_Container): ...


class Dd(_Container): ...


class Del(_Container):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        innerHTML=[],
        cite: str = None,
        datetime: str = None,
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
            innerHTML=innerHTML,
        )
        self.cite = cite
        self.datetime = datetime

    @property
    def cite(self):
        return self._cite[1]

    @cite.setter
    def cite(self, cite):
        self._cite = [None, cite, "cite"]

    @property
    def datetime(self):
        return self._datetime[1]

    @datetime.setter
    def datetime(self, datetime):
        self._datetime = [None, datetime, "datetime"]


class Details(_Container):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        innerHTML=[],
        open: bool = False,
        name: str = None,
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
            innerHTML=innerHTML,
        )
        self.open = open
        self.name = name

    @property
    def open(self):
        return self._open[1]

    @open.setter
    def open(self, open):
        self._open = [False, open, "open"]

    @property
    def name(self):
        return self._name[1]

    @name.setter
    def name(self, name):
        self._name = [None, name, "name"]


class Dfn(_Container): ...


class Dialog(_Container):
    def __init__(
        self,
        *,
        accesskey=None,
        anchor=None,
        aria_attributes=None,
        autocapitalize="none",
        autocorrect="on",
        autofocus=False,
        class_attr=None,
        contenteditable=None,
        custom_attributes=None,
        data_attributes=None,
        dir=None,
        draggable=None,
        enterkeyhint=None,
        event_attributes=None,
        exportparts=None,
        hidden=False,
        id=None,
        inert=False,
        inputmode=None,
        is_attr=None,
        itemid=None,
        itemprop=None,
        itemref=None,
        itemscope=False,
        itemtype=None,
        lang=None,
        nonce=None,
        part=None,
        popover=None,
        role=None,
        slot=None,
        spellcheck="true",
        style=None,
        tabindex=None,
        title=None,
        translate="yes",
        virtualkeyboardpolicy=None,
        writingsuggestions="true",
        innerHTML=[],
        open: bool = False,
    ):
        super().__init__(
            accesskey=accesskey,
            anchor=anchor,
            aria_attributes=aria_attributes,
            autocapitalize=autocapitalize,
            autocorrect=autocorrect,
            autofocus=autofocus,
            class_attr=class_attr,
            contenteditable=contenteditable,
            custom_attributes=custom_attributes,
            data_attributes=data_attributes,
            dir=dir,
            draggable=draggable,
            enterkeyhint=enterkeyhint,
            event_attributes=event_attributes,
            exportparts=exportparts,
            hidden=hidden,
            id=id,
            inert=inert,
            inputmode=inputmode,
            is_attr=is_attr,
            itemid=itemid,
            itemprop=itemprop,
            itemref=itemref,
            itemscope=itemscope,
            itemtype=itemtype,
            lang=lang,
            nonce=nonce,
            part=part,
            popover=popover,
            role=role,
            slot=slot,
            spellcheck=spellcheck,
            style=style,
            tabindex=tabindex,
            title=title,
            translate=translate,
            virtualkeyboardpolicy=virtualkeyboardpolicy,
            writingsuggestions=writingsuggestions,
            innerHTML=innerHTML,
        )
        self.open = open

    @property
    def open(self):
        return self._open[1]

    @open.setter
    def open(self, open):
        self._open = [False, open, "open"]


class Div(_Container): ...


class Dl(_Container): ...


class Dt(_Container): ...
