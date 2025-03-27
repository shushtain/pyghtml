# pyghtml

Python-Generatable HTML

> ⚠️ **In per-issue development**  
> 🦐 Any help or critique is encouraged.

## Idea

This library was born when I needed to convert English lesson plans from JSON to a static website. I didn't want to learn how to set up a server just to compile some pages. And I don't know PHP. So this library consists of HTML tags as Python classes, with attributes as class properties.

> 💅 It's pie-tea-em-el, actually.

## Features

### Attribute types and defaults

Boolean Python values behave according to the logic of boolean HTML attributes. `autofocus` is turned off by default, so `autofocus=False` doesn't lead to redundancies. The same goes for `autocorrect="on"`, which is the default value.

```python
import pyghtml as html

b = html.Button() + "Pyghtml"

b.title = "Home"
b.disabled = True
b.autofocus = False   # default
b.autocorrect = "on"  # default

print(b)
```

produces:

```html
<button title="Home" disabled>Pyghtml</button>
```

### Simple container logic

- Each container tag is a `MutableSequence` storing children in the `inner_html`
- `.append()` is the same as `+= item`; `.extend()` is the same as `+= [items]`
- You can use `with` to automatically append elements, so you don't forget

```python
import pyghtml as html

with html.Div() as div:
    html.Img(src="image.jpg")
    p = html.P(inner_html="Hello")

p.class_ = "greeting"
p += " World!"

print(div)
```

produces:

```html
<div>
    <img src="image.jpg" />
    <p class="greeting">Hello World!</p>
</div>
```

> `with` is safe to use while multi-threading html generation.  
> The contexts are stored in `threading.local()`.

### Utilities

#### Class methods

- `Div().copy()` returns a shallow copy of the element
- `Div().tag()` returns `div`
- `Div(id="main", hidden=True).attrs_to_str()` returns `id="main" hidden`

#### Functions

- `contains()` checks if an item/element is in a container
  - `deep=False` is equivalent to `item in container`
  - `deep=True` checks recursively
  
- `find_by_tag()` returns a list of children with the specified tag
  - `deep=True` searches recursively

- `find_by_attr()` returns a list of children that support the attribute
  - optional `value` also matches the attribute's value
  - `deep=True` searches recursively

- `sub()` substitutes children within a container
  - `count` limits the number of replacements
  - `deep=True` replaces recursively

## Installation

Run:

```bash
pip install pyghtml
```

Import:

```python
import pyghtml as html
```

## Additional notes

- Self-closing tags are self-closing (`<br />`).

- `<!DOCTYPE html>` is `Doctype()` and `<!-- -->` is `CommentHtml()`.

- HTML attributes that match Python reserved words are suffixed with `_` (`class` is `class_`).

- If the attribute's default value is `None`, that usually means there is no clear default value for it in the HTML spec (like the values controlled by the client-side agents when omitted). Attributes like `alt` default to `None` because an omitted `alt` is not the same as `alt=""` from the accessibility standpoint.

- `data-*`, `aria-*`, event (`onclick`, etc), and custom/missing attributes should be given as dictionaries through `data_attrs`, `aria_attrs`, `event_attrs`, `custom_attrs`. For example: `data_attrs = {"data-custom-name": "custom value"}`.

- Abbreviations are broken: `Html()`, `Wbr()`. This may be debatable, but I thought that classes like `HttpEquiv()` and `AriaAttrs()` reflect `http-equiv` and `aria-*` much more clearly than `HTTPEquiv()` and `ARIAAttrs()`. Also, it's hard to keep in mind whether `bdi`, `bdo`, `src`, `ul`, `li`, `dt`, `dfn` count as abbreviations.

- There are class names like `I()` for `<i></i>`, so please use a font that differentiates between `Il1`. I use JetBrains Mono.

## Future improvements

- [x] Add attribute docstrings
- [x] Add tag docstrings
- [ ] Add attribute validation
- [ ] Add tag validation

## Sources

- [HTML Spec](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [MDN Web Docs](https://html.spec.whatwg.org/)
- [W3Schools](https://www.w3schools.com/tags/default.asp)
