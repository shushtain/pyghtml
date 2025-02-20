# pyghtml

Python-Generated HTML

> ⚠️ **The library is in active development**: Not all tags are added yet.  
> 💩 I'm not a skilled programmer. Any help or critique is encouraged.

## Idea

This library was born when I needed to convert hundreds of English lesson plans from JSON to a static website. I didn't want to learn how to set up a server just to compile some pages. And I don't know PHP, even if I wanted to use it. So this library consists of HTML tags as Python classes, with attributes as class properties. This way you can create "cleaner" templates.

> ☝️ It's pie-tea-em-el, actually.

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

Both `__add__` and `__iadd__` append the element on the right to the `innerHTML` property of the element on the left. So you can use `+` or `+=` to put something inside a "tag".

```python
html = pyghtml.Html()
html += pyghtml.Body(innerHTML=["Hello!"])
print(html)
```

produces:

```html
<html>
  <body>
    Hello!
  </body>
</html>
```

## Additional notes

- HTML attributes that match Python reserved words are suffixed with `_attr` (`class` is `class_attr`).
- Future or present HTML tags that match Python reserved words are suffixed with `_tag`.
- Self-closing tags are self-closing (`<br />`).
- `data-*` attributes should be given as `data_attributes = {"data-custom-name": "custom value"}`.
- Event attributes (`onclick`, `onfocus`, etc) should be given similarly, through `event_attributes`. This was done to shorten the code.
- The same logic applies to `aria-*` attributes. Although their variety is finite, their behavior is connected to the global attribute `role` in ways I refuse to understand.
- There is an option to add custom enumerate and boolean attributes through `custom_attributes = {"custom1": "value", "custom2": True}`.
- If the attribute's default value is `None`, that usually means there is no clear default value for it in the HTML specification (like the values controlled by the client-side agents when omitted).

## Sources

- [HTML Spec][def2]
- [MDN Web Docs][def]

## What could be improved

- [ ] Finish all tags
- [ ] Add specs for all tags
- [ ] Add specs for all attributes
- [ ] Add validation to each property
- [ ] Pack it for pip

[def]: https://developer.mozilla.org/en-US/docs/Web/HTML
[def2]: https://html.spec.whatwg.org/
