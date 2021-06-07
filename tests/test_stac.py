from stactools.gap.stac import create_item


class TestStac:
    def test_create_item(self):
        path = "where/is/the/file"
        item = create_item(path)
        item.validate()
