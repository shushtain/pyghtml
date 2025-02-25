""" This is an edge-case scenario where the page itself isn't complex but tedious to code manually. Surely we seldomly build layouts based on golden ratios, but hopefully it conveys how not only text may vary from page to page, but the layout itself (based on the number of sections in your JSON, etc)."""

import pyghtml as html


# *** The input data is the Fibonacci sequence.
# Could be a JSON file converted into a dict, etc.


def fib_seq(length: int = 10) -> list:
    """Generates a Fibonacci sequence of `length`"""
    array: list = [1, 1]

    def fib(array, length):
        if len(array) < length:
            array.append(array[-2] + array[-1])
            fib(array, length)

    fib(array, length)
    return array


blocks = fib_seq(10)


# *** Bulding parts of the page

# *-- body

body = html.Body()
body += html.H1() + "Fibonacci numbers"
body += html.Div(class_="container horz")


def pack(elem, array):
    """Turns data blocks into HTML elements"""
    if len(array) > 0:
        elem[-1] += html.Div() + html.P(inner_html=array[-1])
        elem[-1] += html.Div(class_=("vert" if len(array) % 2 == 0 else "horz"))
        pack(elem[-1], array[:-1])
    return elem


pack(body, blocks)

# *-- head
# Inline css is good for providing a single-file example.

style = html.Style()

style += "* {box-sizing: border-box;margin: 0;padding: 0;} body {width: 90vw;height: 80vh;font-family: sans-serif;background-color: #0d0d0d;color: #f2f2f2;padding: 2rem;} h1 {margin-bottom: 2rem;} .container {width: 100%;aspect-ratio: 1.618;max-width: 125vh;} div {display: flex;flex-flow: row nowrap;} .vert {flex-flow: column nowrap;} .vert>div {width: 100%;height: 38.2%;aspect-ratio: 1;} .vert>div:has(>p) {justify-content: center;align-items: center;height: 61.8%;} .horz>div {width: 38.2%;height: 100%;} .horz>div:has(>p) {justify-content: center; align-items: center; width: 61.8%;} div:has(>p) {border: 1px solid #999999;}"

head = html.Head() + style


# *** Assembling and printing
# The output should be identical to a minimized version of example.html
# Just didn't want to create unsolicited files on your side.


page = html.Html(lang="en") + head + body
print(str(html.Doctype()) + str(page))
