from libpathod import utils
import tutils

def test_parse_size():
    assert utils.parse_size("100") == 100
    assert utils.parse_size("100k") == 100 * 1024
    tutils.raises("invalid size spec",  utils.parse_size, "foo")
    tutils.raises("invalid size spec",  utils.parse_size, "100kk")


def test_parse_anchor_spec():
    assert utils.parse_anchor_spec("foo=200") == ("foo", "200")
    assert utils.parse_anchor_spec("foo") == None


def test_data_path():
    tutils.raises(ValueError, utils.data.path, "nonexistent")