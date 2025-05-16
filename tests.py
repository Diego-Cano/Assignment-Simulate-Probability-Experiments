"""
Tests for the Probability Simulator
Includes unit tests for normal use and edge cases.
"""

import unittest
import numpy as np
from simulation import ProbabilitySimulator

class TestProbabilitySimulator(unittest.TestCase):
    
    def setUp(self):
        self.simulator = ProbabilitySimulator()
        np.random.seed(42)  # Set seed for reproducibility

    # Normal cases

    def test_coin_tosses_normal(self):
        result = self.simulator.simulate_coin_tosses(100)
        self.assertEqual(result['heads'] + result['tails'], 100)
        self.assertTrue(0 <= result['heads'] <= 100)
        self.assertTrue(0 <= result['tails'] <= 100)

    def test_die_rolls_normal(self):
        result = self.simulator.simulate_die_rolls(60)
        counts = result['counts']
        self.assertEqual(sum(counts.values()), 60)
        self.assertTrue(all(face in counts for face in range(1, 7)))
        self.assertTrue(all(0 <= count <= 60 for count in counts.values()))

    def test_card_draws_normal(self):
        result = self.simulator.simulate_card_draws(20)
        self.assertEqual(result['red'] + result['black'], 20)
        self.assertTrue(0 <= result['red'] <= 20)
        self.assertTrue(0 <= result['black'] <= 20)

    # Edge cases

    def test_coin_tosses_zero(self):
        result = self.simulator.simulate_coin_tosses(0)
        self.assertEqual(result['heads'], 0)
        self.assertEqual(result['tails'], 0)
        self.assertEqual(len(result['raw_data']), 0)

    def test_die_rolls_large_number(self):
        result = self.simulator.simulate_die_rolls(10000)
        expected = 10000 / 6
        for count in result['counts'].values():
            self.assertTrue(0.8 * expected <= count <= 1.2 * expected)

    def test_compound_events_consistency(self):
        result = self.simulator.simulate_compound_events(100)
        self.assertTrue(result['both_heads'] <= result['at_least_one_head'])
        self.assertEqual(result['at_least_one_head'] + result['neither_head'], 100)

if __name__ == '__main__':
    unittest.main()
