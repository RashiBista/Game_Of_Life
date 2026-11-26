
import pytest

from game.engine.simulation import life_step, count_neighbors


def test_isolated_cell_dies():
    live = {(5, 5)}

    assert life_step(live) == set()


def test_block_remains_stable():
    block = {
        (5, 5), (5, 6),
        (6, 5), (6, 6),
    }

    assert life_step(block) == block


def test_blinker_oscillates():
    horizontal = {
        (5, 4), (5, 5), (5, 6),
    }

    vertical = {
        (4, 5), (5, 5), (6, 5),
    }

    assert life_step(horizontal) == vertical
    assert life_step(vertical) == horizontal


def test_cell_with_three_neighbours_is_born():
    live = {
        (4, 5),
        (5, 4),
        (5, 6),
    }

    assert (5, 5) in life_step(live)


def test_cell_with_two_neighbours_survives():
    live = {
        (5, 4),
        (5, 5),
        (5, 6),
    }

    next_generation = life_step(live)

    assert (5, 5) in next_generation


def test_cell_with_four_neighbours_dies():
    live = {
        (5, 5),
        (4, 5),
        (6, 5),
        (5, 4),
        (5, 6),
    }

    assert (5, 5) not in life_step(live)


def test_walls_cannot_contain_live_cells():
    live = {(5, 5)}
    walls = {(5, 5)}

    with pytest.raises(ValueError):
        life_step(live, walls)


def test_cells_cannot_be_born_inside_walls():
    live = {
        (4, 5),
        (5, 4),
        (5, 6),
    }
    walls = {(5, 5)}

    assert (5, 5) not in life_step(live, walls)


def test_cell_adjacent_to_wall_can_survive():
    live = {
        (1, 0),
        (1, 1),
        (1, 2),
    }
    walls = {(0, 0)}

    next_generation = life_step(live, walls)

    assert (1, 1) in next_generation


def test_cells_do_not_wrap_around_board_edges():
    live = {
        (0, 0),
        (0, 1),
        (1, 0),
    }

    next_generation = life_step(live, rows=5, cols=5)

    assert (4, 4) not in next_generation


def test_count_neighbors():
    live = {
        (4, 4),
        (4, 5),
        (5, 4),
    }

    assert count_neighbors((5, 5), live) == 3


def test_out_of_bounds_cells_are_rejected():
    with pytest.raises(ValueError):
        life_step({(24, 40)})
