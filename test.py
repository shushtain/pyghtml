import unittest
import pyghtml as html


class TestPyGHtml(unittest.TestCase):
    def test_boolean_attributes(self):
        """Test boolean attributes behavior"""
        button = html.Button(
            title="Home", disabled=True, autofocus=False, autocorrect="on"
        )
        result = str(button)
        self.assertIn('title="Home"', result)
        self.assertIn("disabled", result)
        self.assertNotIn("autofocus", result)
        self.assertNotIn("autocorrect", result)  # default value should be omitted
        self.assertIn("<button", result)
        self.assertIn("></button>", result)

    def test_container_operations(self):
        """Test container operations like +, +=, and list operations"""
        # Test + operator returns new instance
        list1 = html.Ul() + html.Li(inner_html="I'm Sawcon")
        list2 = html.Ul() + (list1[0] + ", too!")

        # Test += operator modifies in place
        list1 += html.Li() + ["Sawcon", " ", "Deeznuts"]

        # Test list1 structure
        result1 = str(list1)
        self.assertIn("<ul", result1)
        self.assertIn("</ul>", result1)
        self.assertIn("<li>I'm Sawcon</li>", result1)
        self.assertIn("<li>Sawcon Deeznuts</li>", result1)

        # Test list2 structure
        result2 = str(list2)
        self.assertIn("<ul", result2)
        self.assertIn("</ul>", result2)
        self.assertIn("<li>I'm Sawcon, too!</li>", result2)

    def test_with_statement(self):
        """Test context manager ('with' statement) functionality"""
        with html.Div(class_="outer") as outer:
            with html.Div(class_="inner"):
                html.P(inner_html="Inner text")
            html.P(inner_html="Outer text")

        result = str(outer)
        self.assertIn('<div class="outer"', result)
        self.assertIn('<div class="inner"', result)
        self.assertIn("<p>Inner text</p>", result)
        self.assertIn("<p>Outer text</p>", result)
        self.assertIn("</div>", result)  # Just check for closing tags existence

    def test_self_closing_tags(self):
        """Test self-closing tags behavior"""
        br = html.Br()
        self.assertEqual(str(br), "<br />")

        # Should raise TypeError when used with 'with'
        with self.assertRaises(TypeError):
            with html.Br():
                pass

    def test_special_tags(self):
        """Test special tags like DOCTYPE and comments"""
        doctype = html.Doctype()
        comment = html.CommentHtml(inner_html="Test comment")

        self.assertEqual(str(doctype), "<!DOCTYPE html>")
        self.assertEqual(str(comment), "<!-- Test comment -->")

    def test_tag_method(self):
        """Test tag() method"""
        tag1 = html.Div().tag()
        tag2 = html.Br().tag()

        self.assertEqual(str(tag1), "div")
        self.assertEqual(str(tag2), "br")

    def test_attribute_handling(self):
        """Test various attribute handling cases"""
        # Test class_ for Python reserved word
        div = html.Div(class_="test-class")
        result_div = str(div)
        self.assertIn('class="test-class"', result_div)
        self.assertIn("<div", result_div)
        self.assertIn("</div>", result_div)

        # Test None attributes are omitted
        img = html.Img(alt=None, src="test.jpg")
        result_img = str(img)
        self.assertIn('src="test.jpg"', result_img)
        self.assertNotIn("alt", result_img)
        self.assertIn("<img", result_img)
        self.assertIn("/>", result_img)

        # Test custom attributes
        custom = html.Div(
            data_attrs={"data-test": "value"},
            aria_attrs={"aria-label": "test"},
            event_attrs={"onclick": "alert()"},
            custom_attrs={"custom-attr": "value"},
        )

        result = str(custom)
        self.assertIn('data-test="value"', result)
        self.assertIn('aria-label="test"', result)
        self.assertIn('onclick="alert()"', result)
        self.assertIn('custom-attr="value"', result)
        self.assertIn("<div", result)
        self.assertIn("</div>", result)

    def test_find_by_attr(self):
        """Test finding elements by attribute"""
        # Create a container div first
        container = html.Div(id="container")

        # Then add elements to it
        with container:
            html.P(id="p1")
            with html.Div():
                html.P(id="p2")
                html.Span(id="p3")
                html.P(id=None)  # Element with None id

        # Test finding all elements with 'id' attribute (excluding container)
        results = html.find_by_attr(container, "id", deep=True)
        self.assertEqual(
            len(results), 5
        )  # Should find all elements that have the 'id' attribute
        ids = [getattr(r, "id") for r in results]
        self.assertIn("p1", ids)
        self.assertIn("p2", ids)
        self.assertIn("p3", ids)
        self.assertEqual(ids.count(None), 2)  # Two elements with id=None

        # Test non-recursive search
        results = html.find_by_attr(container, "id")
        self.assertEqual(
            len(results), 2
        )  # Should find both P and Div immediate children
        ids = [getattr(r, "id") for r in results]
        self.assertIn("p1", ids)
        self.assertIn(None, ids)  # The immediate Div has id=None

        # Test search with specific value
        results = html.find_by_attr(container, "id", "p2", deep=True)
        self.assertEqual(len(results), 1)
        self.assertEqual(getattr(results[0], "id"), "p2")

        # Test search with None value
        results = html.find_by_attr(container, "id", None, deep=True)
        self.assertEqual(len(results), 2)  # Should find both elements with id=None
        self.assertTrue(all(getattr(r, "id") is None for r in results))

    def test_contains(self):
        """Test contains() function behavior"""
        # Create a nested structure
        container = html.Div()
        with container:
            p1 = html.P(inner_html="First")
            with html.Div() as inner:
                p2 = html.P(inner_html="Second")

        # Test non-recursive search
        self.assertTrue(html.contains(p1, container))
        self.assertFalse(html.contains(p2, container))

        # Test recursive search
        self.assertTrue(html.contains(p2, container, deep=True))

        # Test with non-element content
        container += ["text", 123]
        self.assertTrue(html.contains("text", container))
        self.assertTrue(html.contains(123, container))

        # Test with non-existing item
        self.assertFalse(html.contains("nonexistent", container, deep=True))

    def test_find_by_tag(self):
        """Test find_by_tag() function behavior"""
        # Create a nested structure
        container = html.Div()
        with container:
            html.P(inner_html="First")
            with html.Div():
                html.P(inner_html="Second")
                html.Span(inner_html="Third")

        # Test non-recursive search
        results = html.find_by_tag(container, "p")
        self.assertEqual(len(results), 1)
        self.assertEqual(
            results[0].inner_html, ["First"]
        )  # Fixed: inner_html is a list

        # Test recursive search
        results = html.find_by_tag(container, "p", deep=True)
        self.assertEqual(len(results), 2)
        self.assertTrue(
            any(p.inner_html == ["First"] for p in results)
        )  # Fixed: compare with list
        self.assertTrue(
            any(p.inner_html == ["Second"] for p in results)
        )  # Fixed: compare with list

        # Test with non-existing tag
        results = html.find_by_tag(container, "nonexistent", deep=True)
        self.assertEqual(len(results), 0)

    def test_sub(self):
        """Test sub() function behavior"""
        # Create a nested structure
        container = html.Div()
        with container:
            p1 = html.P(inner_html="Replace me")
            with html.Div():
                html.P(inner_html="Replace me")
                html.P(inner_html="Keep me")

        # Test non-recursive substitution
        result = html.sub(container, p1, html.P(inner_html="Replaced"))
        self.assertEqual(result, container)  # Should return same container
        self.assertEqual(
            len([p for p in container if isinstance(p, html.P)]), 1
        )  # Should replace only first level

        # Test recursive substitution
        container = html.Div()  # Fresh container
        with container:
            html.P(inner_html="Replace me")
            with html.Div():
                html.P(inner_html="Replace me")
                html.P(inner_html="Keep me")

        result = html.sub(
            container,
            html.P(inner_html="Replace me"),
            html.P(inner_html="Replaced"),
            deep=True,
        )
        replaced = html.find_by_tag(result, "p", deep=True)
        self.assertEqual(
            len([p for p in replaced if p.inner_html == ["Replaced"]]),
            2,  # Fixed: compare with list
        )

        # Test count parameter
        container = html.Div()
        with container:
            html.P(inner_html="Replace me")
            html.P(inner_html="Replace me")
            html.P(inner_html="Replace me")

        result = html.sub(
            container,
            html.P(inner_html="Replace me"),
            html.P(inner_html="Replaced"),
            count=2,
        )
        replaced = html.find_by_tag(result, "p")
        self.assertEqual(
            len([p for p in replaced if p.inner_html == ["Replaced"]]),
            2,  # Fixed: compare with list
        )
        self.assertEqual(
            len([p for p in replaced if p.inner_html == ["Replace me"]]), 1
        )

        # Test invalid count
        with self.assertRaises(ValueError):
            html.sub(
                container,
                html.P(inner_html="Replace me"),
                html.P(inner_html="Replaced"),
                count=-2,
            )


if __name__ == "__main__":
    unittest.main()

    # with html.Div() as div:
    #     html.Img(src="image.jpg")
    #     p = html.P(inner_html="Hello")

    # p.class_ = "greeting"
    # p += " World!"

    # print(div)
    # print(html.attr._context)

    # b = html.Button(title="Home", disabled=True, autofocus=False, autocorrect="on")
    # print(b)
