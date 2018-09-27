# Zhengchao Ni, 73173892

import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        self.assertEqual(string_to_location('A1'),(0,0))
        self.assertEqual(string_to_location('B2'),(1,1))
        self.assertEqual(string_to_location('C3'),(2,2))
        self.assertEqual(string_to_location('D4'),(3,3))
        self.assertEqual(string_to_location('E5'),(4,4))

    def test_location_to_string(self):
        self.assertEqual(location_to_string((0,0)),'A1')
        self.assertEqual(location_to_string((1,1)),'B2')
        self.assertEqual(location_to_string((2,2)),'C3')
        self.assertEqual(location_to_string((3,3)),'D4')
        self.assertEqual(location_to_string((4,4)),'E5')

    def test_at(self):
        self.assertEqual(at((0,2)),'-')
        self.assertEqual(at((0,3)),'M')
        self.assertEqual(at((3,4)),'-')
        self.assertEqual(at((3,1)),'R')
        
    def test_all_locations(self):
        self.assertEqual(all_locations(),[(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),\
                                         (2,0),(2,1),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),(3,3),(3,4),\
                                         (4,0),(4,1),(4,2),(4,3),(4,4)])

    def test_adjacent_location(self):
        self.assertEqual(adjacent_location((0,2), 'down'),(1,2))
        self.assertEqual(adjacent_location((1,3), 'right'),(1,4))
        self.assertEqual(adjacent_location((4,3), 'up'),(3,3))
        self.assertEqual(adjacent_location((2,4), 'left'),(2,3))
        
    def test_is_legal_move_by_musketeer(self):
        self.assertTrue(is_legal_move_by_musketeer((2,2), 'right'))
        self.assertFalse(is_legal_move_by_musketeer((0,3), 'down'))
        self.assertTrue(is_legal_move_by_musketeer((1,3), 'left'))
        self.assertTrue(is_legal_move_by_musketeer((2,2), 'up'))
        
    def test_is_legal_move_by_enemy(self):
        self.assertFalse(is_legal_move_by_enemy((3,1), 'up'))
        self.assertTrue(is_legal_move_by_enemy((1,2), 'left'))
        self.assertTrue(is_legal_move_by_enemy((2,3), 'right'))
        self.assertFalse(is_legal_move_by_enemy((2,1), 'down'))

    def test_is_legal_move(self):
        self.assertFalse(is_legal_move((0,3), 'right'))
        self.assertTrue(is_legal_move((1,3), 'left'))
        self.assertTrue(is_legal_move((2,1), 'up'))
        self.assertFalse(is_legal_move((2,2), 'down'))
        
    def test_has_some_legal_move_somewhere(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))
        set_board([ [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, M, M],
                    [_, _, _, M, R] ])
        self.assertFalse(has_some_legal_move_somewhere('R'))
        self.assertTrue(has_some_legal_move_somewhere('M'))

    def test_possible_moves_from(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])
        self.assertEqual(possible_moves_from((0,3)),[])
        self.assertEqual(possible_moves_from((1,2)),['left', 'up'])
        self.assertEqual(possible_moves_from((1,3)),['left', 'down'])
        self.assertEqual(possible_moves_from((2,1)),['left', 'up'])
        self.assertEqual(possible_moves_from((2,2)),['left', 'right', 'up'])
        self.assertEqual(possible_moves_from((2,3)),['right', 'down'])
        self.assertEqual(possible_moves_from((3,1)),['left', 'right', 'down'])
        self.assertEqual(possible_moves_from((4,3)),['left', 'right', 'up'])

    def test_can_move_piece_at(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(can_move_piece_at((0,3)))
        self.assertFalse(can_move_piece_at((0,4)))
        self.assertFalse(can_move_piece_at((1,3)))
        self.assertTrue(can_move_piece_at((1,4)))
        self.assertTrue(can_move_piece_at((2,2)))

    def test_is_legal_location(self):
        create_board()
        self.assertTrue(is_legal_location((2,4)))
        self.assertFalse(is_legal_location((-2,4)))
        self.assertFalse(is_legal_location((2,-4)))
        self.assertFalse(is_legal_location((-2,-4)))

    def test_is_within_board(self):
        set_board([ [_, _, _, _, M],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(is_within_board((0,4),'right'))
        self.assertFalse(is_within_board((4,0),'left'))
        self.assertFalse(is_within_board((0,2),'up'))
        self.assertFalse(is_within_board((4,3),'down'))
        self.assertTrue(is_within_board((0,4),'down'))
        self.assertTrue(is_within_board((4,0),'up'))
        self.assertTrue(is_within_board((0,2),'left'))
        self.assertTrue(is_within_board((4,3),'right'))
        

    def test_all_possible_moves_for(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertEqual(all_possible_moves_for('M'),[((0,3),'left'),((0,3),'right'),((1,4),'up')])
        self.assertEqual(all_possible_moves_for('R'),[((0,2),'left'),((0,2),'down')])
        
    def test_make_move(self):
        # every time I test, I should reset the board
        # otherwise, the board of the nearest test continues.
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])
        self.assertEqual(make_move((1,2),'left'),[
                [_, _, _, M, _],
                [_, R, _, M, _],
                [_, R, M, R, _],
                [_, R, _, _, _],
                [_, _, _, R, _] ])
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])
        self.assertEqual(make_move((3,1),'right'),[
                [_, _, _, M, _],
                [_, _, R, M, _],
                [_, R, M, R, _],
                [_, _, R, _, _],
                [_, _, _, R, _] ])
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])
        self.assertEqual(make_move((2,2),'up'),[
                [_, _, _, M, _],
                [_, _, M, M, _],
                [_, R, _, R, _],
                [_, R, _, _, _],
                [_, _, _, R, _] ])
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])
        self.assertEqual(make_move((1,3),'down'),[
                [_, _, _, M, _],
                [_, _, R, _, _],
                [_, R, M, M, _],
                [_, R, _, _, _],
                [_, _, _, R, _] ])
        
    def test_choose_computer_move(self):
        self.assertEqual(choose_computer_move('R'),((3,1), 'left'))
        self.assertEqual(choose_computer_move('M'),((2,2), 'right'))
        

    def test_is_enemy_win(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, _, M, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertTrue(is_enemy_win())
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(is_enemy_win())
unittest.main()
