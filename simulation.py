"""
Probability Simulation Experiments
This program simulates various probability experiments including:
- Coin tosses
- Die rolls
- Card draws
- Compound events
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random


class ProbabilitySimulator:
    def __init__(self):
        """Initialize the probability simulator"""
        self.results = {}
        random.seed()  # Initialize random seed
        np.random.seed()  # Initialize numpy random seed

    def simulate_coin_tosses(self, num_tosses=100):
        """
        Simulate tossing a coin a specified number of times
        
        Args:
            num_tosses (int): Number of coin tosses to simulate
            
        Returns:
            dict: Dictionary with counts of 'heads' and 'tails'
        """
        # Generate random 0s and 1s (0 = tails, 1 = heads)
        tosses = np.random.randint(0, 2, num_tosses)
        
        # Count heads and tails
        heads_count = np.sum(tosses)
        tails_count = num_tosses - heads_count
        
        # Store results
        self.results['coin_tosses'] = {
            'heads': heads_count,
            'tails': tails_count,
            'raw_data': tosses
        }
        
        return self.results['coin_tosses']
    
    def plot_coin_tosses(self):
        """Plot the results of coin toss simulation"""
        if 'coin_tosses' not in self.results:
            print("No coin toss simulation has been run yet.")
            return
        
        results = self.results['coin_tosses']
        
        # Create a bar plot
        labels = ['Heads', 'Tails']
        counts = [results['heads'], results['tails']]
        
        plt.figure(figsize=(8, 6))
        plt.bar(labels, counts, color=['green', 'blue'])
        plt.title(f'Results of {results["heads"] + results["tails"]} Coin Tosses')
        plt.ylabel('Frequency')
        plt.grid(axis='y', alpha=0.3)
        
        # Add count labels on top of bars
        for i, count in enumerate(counts):
            plt.text(i, count + 0.5, str(count), ha='center')
        
        # Calculate and display probability
        total = sum(counts)
        plt.figtext(0.5, 0.01, f'Probability of Heads: {results["heads"]/total:.2f}', 
                   ha='center', fontsize=10)
        
        plt.tight_layout()
        plt.show()
    
    def simulate_die_rolls(self, num_rolls=60):
        """
        Simulate rolling a six-sided die a specified number of times
        
        Args:
            num_rolls (int): Number of die rolls to simulate
            
        Returns:
            dict: Dictionary with counts of each die face
        """
        # Generate random integers between 1 and 6
        rolls = np.random.randint(1, 7, num_rolls)
        
        # Count occurrences of each face
        face_counts = Counter(rolls)
        
        # Ensure all faces are represented in the results
        results = {face: face_counts.get(face, 0) for face in range(1, 7)}
        
        # Store results
        self.results['die_rolls'] = {
            'counts': results,
            'raw_data': rolls
        }
        
        return self.results['die_rolls']
    
    def plot_die_rolls(self):
        """Plot the results of die roll simulation"""
        if 'die_rolls' not in self.results:
            print("No die roll simulation has been run yet.")
            return
        
        results = self.results['die_rolls']['counts']
        
        # Create a bar plot
        faces = list(results.keys())
        counts = list(results.values())
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(faces, counts, color='purple')
        plt.title('Results of Die Rolls')
        plt.xlabel('Die Face')
        plt.ylabel('Frequency')
        plt.xticks(faces)
        plt.grid(axis='y', alpha=0.3)
        
        # Add count labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                   f'{height}', ha='center')
        
        # Calculate and display probabilities
        total = sum(counts)
        expected = total / 6
        plt.figtext(0.5, 0.01, 
                  f'Expected frequency for each face: {expected:.1f}', 
                  ha='center', fontsize=10)
        
        plt.tight_layout()
        plt.show()
    
    def simulate_card_draws(self, num_draws=20):
        """
        Simulate drawing cards from a deck
        
        Args:
            num_draws (int): Number of card draws to simulate
            
        Returns:
            dict: Dictionary with counts of red and black cards
        """
        # Create a deck of cards (1-26 are red, 27-52 are black)
        deck = list(range(1, 53))
        
        # Shuffle the deck
        random.shuffle(deck)
        
        # Draw cards
        draws = deck[:num_draws]
        
        # Count red and black cards
        red_count = sum(1 for card in draws if card <= 26)
        black_count = num_draws - red_count
        
        # Store results
        self.results['card_draws'] = {
            'red': red_count,
            'black': black_count,
            'raw_data': draws
        }
        
        return self.results['card_draws']
    
    def plot_card_draws(self):
        """Plot the results of card draw simulation"""
        if 'card_draws' not in self.results:
            print("No card draw simulation has been run yet.")
            return
        
        results = self.results['card_draws']
        
        # Create a bar plot
        labels = ['Red Cards', 'Black Cards']
        counts = [results['red'], results['black']]
        
        plt.figure(figsize=(8, 6))
        plt.bar(labels, counts, color=['red', 'black'])
        plt.title(f'Results of {results["red"] + results["black"]} Card Draws')
        plt.ylabel('Frequency')
        plt.grid(axis='y', alpha=0.3)
        
        # Add count labels on top of bars
        for i, count in enumerate(counts):
            plt.text(i, count + 0.1, str(count), ha='center', color='white' if i == 1 else 'black')
        
        # Calculate and display probability
        total = sum(counts)
        plt.figtext(0.5, 0.01, f'Probability of Red Card: {results["red"]/total:.2f}', 
                   ha='center', fontsize=10)
        
        plt.tight_layout()
        plt.show()
    
    def simulate_compound_events(self, num_trials=50):
        """
        Simulate flipping two coins a specified number of times
        
        Args:
            num_trials (int): Number of double coin flip trials
            
        Returns:
            dict: Dictionary with counts of different outcomes
        """
        # Initialize counters
        both_heads = 0
        at_least_one_head = 0
        
        # Store raw data
        raw_data = []
        
        # Perform the trials
        for _ in range(num_trials):
            # Flip two coins (0 = tails, 1 = heads)
            flip1 = np.random.randint(0, 2)
            flip2 = np.random.randint(0, 2)
            
            # Store the flips
            raw_data.append((flip1, flip2))
            
            # Check conditions
            if flip1 == 1 and flip2 == 1:
                both_heads += 1
            
            if flip1 == 1 or flip2 == 1:
                at_least_one_head += 1
        
        # Store results
        self.results['compound_events'] = {
            'both_heads': both_heads,
            'at_least_one_head': at_least_one_head,
            'neither_head': num_trials - at_least_one_head,
            'raw_data': raw_data
        }
        
        return self.results['compound_events']
    
    def plot_compound_events(self):
        """Plot the results of compound event simulation"""
        if 'compound_events' not in self.results:
            print("No compound event simulation has been run yet.")
            return
        
        results = self.results['compound_events']
        
        # Create a figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Plot 1: Both Heads vs Not Both Heads
        labels1 = ['Both Heads', 'Not Both Heads']
        counts1 = [results['both_heads'], 
                  (results['at_least_one_head'] - results['both_heads'] + results['neither_head'])]
        
        ax1.bar(labels1, counts1, color=['gold', 'silver'])
        ax1.set_title('Both Heads vs. Not Both Heads')
        ax1.set_ylabel('Frequency')
        ax1.grid(axis='y', alpha=0.3)
        
        # Add count labels
        for i, count in enumerate(counts1):
            ax1.text(i, count + 0.1, str(count), ha='center')
        
        # Plot 2: At Least One Head vs. No Heads
        labels2 = ['At Least One Head', 'No Heads']
        counts2 = [results['at_least_one_head'], results['neither_head']]
        
        ax2.bar(labels2, counts2, color=['gold', 'silver'])
        ax2.set_title('At Least One Head vs. No Heads')
        ax2.set_ylabel('Frequency')
        ax2.grid(axis='y', alpha=0.3)
        
        # Add count labels
        for i, count in enumerate(counts2):
            ax2.text(i, count + 0.1, str(count), ha='center')
        
        # Calculate and display probabilities
        total = sum(counts1)
        fig.text(0.5, 0.01, 
               f'P(Both Heads): {results["both_heads"]/total:.2f} | ' +
               f'P(At Least One Head): {results["at_least_one_head"]/total:.2f}', 
               ha='center', fontsize=10)
        
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.15)
        plt.show()

    def run_all_simulations(self):
        """Run all probability simulations"""
        print("Running coin toss simulation...")
        self.simulate_coin_tosses()
        self.plot_coin_tosses()
        
        print("\nRunning die roll simulation...")
        self.simulate_die_rolls()
        self.plot_die_rolls()
        
        print("\nRunning card draw simulation...")
        self.simulate_card_draws()
        self.plot_card_draws()
        
        print("\nRunning compound event simulation...")
        self.simulate_compound_events()
        self.plot_compound_events()


# Run the simulation if this script is executed directly
if __name__ == "__main__":
    simulator = ProbabilitySimulator()
    simulator.run_all_simulations()