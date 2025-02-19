class _Global:
    """The highest-order parent class of all other elements that stores global attributes. Returns tag None. Don't use in production."""

    __tag = None

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
    # must be a dict {"data-custom-name": "value"}
    # converted into data-custom-name="value"
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

        tag = str(self.__class__.__tag)

        attrs = ""
        for key, value in self.__dict__.items():
            attrs += _Global._attr_to_string(key, value)

        return f"<{tag}{attrs} />"


class __Container_tags(_Global):
    """The parent class of all container elements. Returns tag None. Don't use in production."""

    __tag = None

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

        tag = str(self.__class__.__tag)

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
