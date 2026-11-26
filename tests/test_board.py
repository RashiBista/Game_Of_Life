
from game.interface.board import pixel_to_cell


def test_pixel_to_cell():
    assert pixel_to_cell((45, 65)) == (3, 2)


def test_top_left_corner():
    assert pixel_to_cell((0, 0)) == (0, 0)


def test_last_cell():
    assert pixel_to_cell((799, 479)) == (23, 39)


def test_outside_right_boundary():
    assert pixel_to_cell((800, 100)) is None


def test_outside_bottom_boundary():
    assert pixel_to_cell((100, 480)) is None


def test_negative_coordinates():
    assert pixel_to_cell((-1, 20)) is None
