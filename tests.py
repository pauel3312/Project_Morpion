import Morpion


def test_morpion_move():
    game = Morpion.Player()
    game.do_move(3)
    assert game.layout_str == "000001000"
    game.do_move(3)
    assert game.layout_str == "000001000"
    game.do_move(4)
    assert game.layout_str == "000021000"
