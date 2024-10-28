from dataclasses import dataclass
from typing import List, Dict
import random

@dataclass
class MutationParameters:
    """Parameters that can be mutated"""
    learning_rate: float
    response_length: int
    creativity_factor: float
    context_weight: float

class MutationEngine:
    """Handles system mutations and evolution"""
    
    def __init__(self):
        self.current_parameters = MutationParameters(
            learning_rate=0.01,
            response_length=1000,
            creativity_factor=0.7,
            context_weight=0.5
        )

    def mutate(self, harmony_score: float) -> MutationParameters:
        """Apply mutations based on harmony evaluation"""
        if harmony_score < 0.5:
            # Stronger mutations when harmony is low
            mutation_strength = 0.2
        else:
            mutation_strength = 0.1

        new_params = MutationParameters(
            learning_rate=self._mutate_value(
                self.current_parameters.learning_rate, 
                mutation_strength,
                min_val=0.001,
                max_val=0.1
            ),
            response_length=int(self._mutate_value(
                self.current_parameters.response_length,
                mutation_strength,
                min_val=100,
                max_val=5000
            )),
            creativity_factor=self._mutate_value(
                self.current_parameters.creativity_factor,
                mutation_strength,
                min_val=0.1,
                max_val=1.0
            ),
            context_weight=self._mutate_value(
                self.current_parameters.context_weight,
                mutation_strength,
                min_val=0.1,
                max_val=1.0
            )
        )
        
        return new_params

    def _mutate_value(self, value: float, strength: float, min_val: float, max_val: float) -> float:
        """Helper method to mutate a single value within bounds"""
        mutation = random.uniform(-strength, strength)
        new_value = value + (value * mutation)
        return max(min_val, min(max_val, new_value))