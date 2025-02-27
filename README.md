# pyghtml

Python-Generatable HTML

> ⚠️ **Active Development**  
> 🦐 Any help or critique is encouraged.

## Idea

This library was born when I needed to convert English lesson plans from JSON to a static website. I didn't want to learn how to set up a server just to compile some pages. And I don't know PHP. So this library consists of HTML tags as Python classes, with attributes as class properties.

> 💅 It's pie-tea-em-el, actually.

## Core functionality

### Attribute types and defaults

Boolean Python values behave according to the logic of boolean HTML attributes. `autofocus` is turned off by default, so `autofocus=False` doesn't lead to redundancies. The same goes for `autocorrect="on"`, which is the default value.

```python
b = pyghtml.Button(title="Home", disabled=True, autofocus=False, autocorrect="on")
print(b)
```

produces:

```html
<button title="Home" disabled></button>
```

### Simple container logic

Both `__add__` and `__iadd__` append the element on the right to the `inner_html` property of the element on the left (`__add__` returns a new instance). So you can use `+` or `+=` to put something inside a "tag".

Containers are also subscriptable.

```python
list1 = pyghtml.Ul() + pyghtml.Li(inner_html="I'm Sawcon")
list2 = pyghtml.Ul() + (list1[0] + ", too!")
list1 += pyghtml.Li() + "Sawcon Deeznuts"
print(list1)
print(list2)
```

produces:

```html
<ul>
    <li>I'm Sawcon</li>
    <li>Sawcon Deeznuts</li>
</ul>
<ul>
    <li>I'm Sawcon, too!</li>
</ul>
```

## Additional notes

- Self-closing tags are self-closing (`<br />`).
- `<!DOCTYPE html>` is `Doctype()` and `<!-- -->` is `CommentHtml()`.
- HTML attributes that match Python reserved words are suffixed with `_` (`class` is `class_`).
- If the attribute's default value is `None`, that usually means there is no clear default value for it in the HTML spec (like the values controlled by the client-side agents when omitted). Attributes like `alt` default to `None` because an omitted `alt` is not the same as `alt=""` from the accessibility standpoint.
- `data-*`, `aria-*`, event (`onclick`, etc), and custom/missing attributes should be given as dictionaries through `data_attrs`, `aria_attrs`, `event_attrs`, `custom_attrs`. For example: `data_attrs = {"data-custom-name": "custom value"}`.
- Abbreviations are broken: `Html()`, `Wbr()`. This may be debatable, but I thought that classes like `HttpEquiv()` and `AriaAttrs()` reflect `http-equiv` and `aria-*` much more clearly than `HTTPEquiv()` and `ARIAAttrs()` would do. Also, it's hard to keep in mind whether `bdi`, `bdo`, `src`, `ul`, `li`, `dt`, `dfn` count as abbreviations.
- There are class names like `I()` for `<i></i>`, so please use a font that differentiates between `Il1`. JetBrains Mono, for instance.

## Future improvements

- [x] Add attribute docstrings
- [x] Add tag docstrings
- [ ] Add attribute validation
- [ ] Add tag validation
- [ ] Add recipes (`LinkStylesheet` with pre-set `rel`, etc)
- [x] Package for pip

## Sources

- [HTML Spec](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [MDN Web Docs](https://html.spec.whatwg.org/)
- [W3Schools](https://www.w3schools.com/tags/default.asp)
