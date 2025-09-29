# Problem Statement
# Given a list of n people, assign each person a different person to give a gift to, such that:

# No one is assigned to themselves
# Each person is assigned exactly one person to give a gift to
# Each person receives a gift from exactly one person
# The assignment forms one or more cycles (typically we want one complete cycle)

import random

class SecretSanta:
    
    def assign_secret_santa(self, people):
        """
        Assigns each person a different person to give a gift to.
        Uses Fisher-Yates shuffle with validation.
        
        Args:
            people: List of names (strings)
            
        Returns:
            Dictionary mapping giver -> receiver
        """
        if len(people) < 2:
            raise ValueError("Need at least 2 people for Secret Santa")
        
        n = len(people)
        receivers = people.copy()
        
        # Keep shuffling until we get a valid derangement
        # (no one is assigned to themselves)
        while True:
            random.shuffle(receivers)
            
            # Check if anyone got themselves
            valid = True
            for i in range(n):
                if people[i] == receivers[i]:
                    valid = False
                    break
            
            if valid:
                break
        
        # Create the assignment dictionary
        assignments = {}
        for i in range(n):
            assignments[people[i]] = receivers[i]
        
        return assignments
    
    def assign_optimized(self, people):
        """
        Optimized approach: Create a single cycle derangement
        This guarantees a valid assignment in O(n) time
        
        Args:
            people: List of names (strings)
            
        Returns:
            Dictionary mapping giver -> receiver
        """
        if len(people) < 2:
            raise ValueError("Need at least 2 people for Secret Santa")
        
        n = len(people)
        shuffled = people.copy()
        random.shuffle(shuffled)
        
        # Create a cycle: each person gives to the next person
        # The last person gives to the first
        assignments = {}
        for i in range(n):
            assignments[shuffled[i]] = shuffled[(i + 1) % n]
        
        return assignments
    
    def verify_assignment(self, assignments):
        """
        Verifies the Secret Santa assignment is valid
        
        Args:
            assignments: Dictionary of giver -> receiver
            
        Returns:
            Tuple (is_valid, error_message)
        """
        givers = set(assignments.keys())
        receivers = set(assignments.values())
        
        # Check 1: Same people in both sets
        if givers != receivers:
            return False, "Givers and receivers don't match"
        
        # Check 2: No one assigned to themselves
        for giver, receiver in assignments.items():
            if giver == receiver:
                return False, f"{giver} is assigned to themselves"
        
        # Check 3: Each person gives to exactly one person
        if len(assignments) != len(set(assignments.values())):
            return False, "Someone receives from multiple people"
        
        return True, "Valid assignment"

