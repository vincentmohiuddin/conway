import numpy as np

from backend.automaton import Automaton
from backend.cell import Cell


def get_horizontal_blinker() -> set[Cell]:
    return {Cell(0, 1), Cell(1, 1), Cell(2, 1)}


def get_vertical_blinker() -> set[Cell]:
    return {Cell(1, 0), Cell(1, 1), Cell(1, 2)}


def get_block() -> set[Cell]:
    return {Cell(0, 0), Cell(1, 0), Cell(0, 1), Cell(1, 1)}


def test_empty_grid_stays_empty():
    assert Automaton.get_next_alive_cells(set()) == set()


def test_get_next_alive_cells_underpopulation():
    assert Automaton.get_next_alive_cells({Cell(0, 0)}) == set()


def test_get_next_alive_cells_overpopulation():
    result = Automaton.get_next_alive_cells(
        {Cell(1, 1), Cell(0, 0), Cell(2, 0), Cell(0, 2), Cell(2, 2)}
    )
    assert Cell(1, 1) not in result


def test_still_life_block():
    assert Automaton.get_next_alive_cells(get_block()) == get_block()


def test_blinker_period_2():
    assert (
        Automaton.get_next_alive_cells(get_horizontal_blinker())
        == get_vertical_blinker()
    )
    assert (
        Automaton.get_next_alive_cells(get_vertical_blinker())
        == get_horizontal_blinker()
    )


def test_run_stops_at_fixed_point():
    frames = list(Automaton(rows=5, cols=5).run(get_block()))
    assert len(frames) == 1
    assert frames[0][0, 0] == 1


def test_run_stops_at_extinction():
    frames = list(Automaton(rows=5, cols=5).run({Cell(0, 0)}))
    assert frames[0][0, 0] == 1
    assert np.all(frames[-1] == 0)


def test_run_clips_out_of_bounds():
    frames = list(Automaton(rows=3, cols=3).run({Cell(2, 2)}))
    assert frames[0][2, 2] == 1
    assert frames[1][2, 2] == 0
