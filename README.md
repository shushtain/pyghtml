# pyghtml

Python-generatable HTML

> ⚠️ **Active Development**  
> 💩 I'm not a skilled programmer. Any help or critique is encouraged.

## Idea

This library was born when I needed to convert hundreds of English lesson plans from JSON to a static website. I didn't want to learn how to set up a server just to compile some pages. And I don't know PHP, even if I wanted to use it. So this library consists of HTML tags as Python classes, with attributes as class properties. This allows for "cleaner" templates.

> 💅 It's pie-tea-em-el, actually.

## Core functionality

### Attribute types and defaults

Boolean Python values behave according to the logic of boolean HTML attributes. `autofocus` is turned off by default, so `autofocus=False` doesn't lead to redundancies.

```python
a = pyghtml.A(href="1.jpg", disabled=True, autofocus=False)
print(a)
```

produces:

```html
<a href="1.jpg" disabled />
```

### Simple container logic

Both `__add__` and `__iadd__` append the element on the right to the `innerHTML` property of the element on the left (`__add__` returns a new instance). So you can use `+` or `+=` to put something inside a "tag".

```python
html = pyghtml.Html()
html2 = html + pyghtml.A(href="1.jpg", innerHTML=["Link"])
html += pyghtml.Body(innerHTML=["Hello!"])
print(html)
print(html2)
```

produces:

```html
<html><body>Hello!</body></html>
<html><body><a href="1.jpg">Link</a></body></html>
```

## Additional notes

- HTML attributes that match Python reserved words are suffixed with `_attr` (`class` is `class_attr`).
- Self-closing tags are self-closing (`<br />`).
- `data-*`, `aria-*`, event (`onclick`, etc), and custom/missing attributes should be given as dictionaries through `data_attrs`, `aria_attrs`, `event_attrs`, `custom_attrs`. For example: `data_attrs = {"data-custom-name": "custom value"}`.
- If the attribute's default value is `None`, that usually means there is no clear default value for it in the HTML specification (like the values controlled by the client-side agents when omitted). Attributes like `alt` also default to `None` because their validation is not the same for an omitted attributed and `""`.

## Sources

- [HTML Spec][def2]
- [MDN Web Docs][def]

## What could be improved

- [x] Finish all tags
- [ ] Add attribute docstrings
- [ ] Add tag docstrings
- [ ] Add attribute validation
- [ ] Add tag validation
- [ ] Add custom tag classes (`Link_stylesheet` with pre-set `rel`, etc)
- [ ] Pack it for pip

[def]: https://developer.mozilla.org/en-US/docs/Web/HTML
[def2]: https://html.spec.whatwg.org/
