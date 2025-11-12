"""
Conscious Design Protocol - Self-aware AI design patterns
"""

from typing import Dict, Any, List, Optional
import logging
from datetime import datetime


class ConsciousDesignProtocol:
    """
    Implements conscious design patterns for self-aware AI systems.
    
    Enables reflective reasoning, intent recognition, and context awareness.
    """
    
    def __init__(self):
        """Initialize the Conscious Design Protocol."""
        self.logger = logging.getLogger(__name__)
        self.reasoning_history = []
        self.intent_recognitions = []
        self.context_stack = []
        
    def reflective_reasoning(
        self,
        decision: str,
        rationale: str,
        alternatives: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Apply reflective reasoning to a decision.
        
        Args:
            decision: The decision being made
            rationale: Why this decision was chosen
            alternatives: Alternative decisions considered
            
        Returns:
            Reflection analysis with confidence and considerations
        """
        reflection = {
            'decision': decision,
            'rationale': rationale,
            'alternatives': alternatives or [],
            'timestamp': datetime.utcnow().isoformat(),
            'confidence': self._calculate_confidence(decision, rationale, alternatives),
            'considerations': self._identify_considerations(decision, rationale)
        }
        
        self.reasoning_history.append(reflection)
        
        return reflection
    
    def recognize_intent(
        self,
        operation: str,
        context: Dict[str, Any],
        user_input: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Recognize and validate intent behind an operation.
        
        Args:
            operation: The operation being performed
            context: Contextual information
            user_input: Optional user input to analyze
            
        Returns:
            Intent analysis with alignment score
        """
        intent = {
            'operation': operation,
            'stated_purpose': context.get('purpose', 'unknown'),
            'inferred_goals': self._infer_goals(operation, context),
            'alignment_score': 0.0,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Calculate alignment between stated and inferred intent
        intent['alignment_score'] = self._calculate_alignment(
            intent['stated_purpose'],
            intent['inferred_goals']
        )
        
        self.intent_recognitions.append(intent)
        
        return intent
    
    def push_context(self, context: Dict[str, Any]) -> None:
        """Add context to the awareness stack."""
        self.context_stack.append({
            'context': context,
            'timestamp': datetime.utcnow().isoformat()
        })
    
    def pop_context(self) -> Optional[Dict[str, Any]]:
        """Remove and return most recent context."""
        if self.context_stack:
            return self.context_stack.pop()
        return None
    
    def get_current_context(self) -> Optional[Dict[str, Any]]:
        """Get current context without removing it."""
        if self.context_stack:
            return self.context_stack[-1]['context']
        return None
    
    def validate_goal_alignment(
        self,
        operation: str,
        intended_goal: str,
        actual_outcome: Any
    ) -> Dict[str, Any]:
        """
        Validate that operation outcome aligns with intended goal.
        
        Args:
            operation: The operation performed
            intended_goal: What was supposed to be achieved
            actual_outcome: What was actually achieved
            
        Returns:
            Alignment validation result
        """
        # Simple heuristic validation
        outcome_str = str(actual_outcome)
        goal_alignment = intended_goal.lower() in outcome_str.lower()
        
        return {
            'operation': operation,
            'intended_goal': intended_goal,
            'goal_achieved': goal_alignment,
            'confidence': 0.8 if goal_alignment else 0.3,
            'timestamp': datetime.utcnow().isoformat()
        }
    
    def _calculate_confidence(
        self,
        decision: str,
        rationale: str,
        alternatives: Optional[List[Dict[str, Any]]]
    ) -> float:
        """Calculate confidence score for a decision."""
        base_confidence = 0.5
        
        # Increase confidence if rationale is detailed
        if len(rationale) > 50:
            base_confidence += 0.2
        
        # Increase confidence if alternatives were considered
        if alternatives and len(alternatives) > 0:
            base_confidence += 0.2
        
        # Decrease confidence if no clear rationale
        if len(rationale) < 20:
            base_confidence -= 0.2
        
        return min(max(base_confidence, 0.0), 1.0)
    
    def _identify_considerations(
        self,
        decision: str,
        rationale: str
    ) -> List[str]:
        """Identify key considerations in a decision."""
        considerations = []
        
        # Look for key consideration indicators
        indicators = {
            'ethical': ['ethical', 'moral', 'right', 'wrong'],
            'practical': ['efficient', 'effective', 'practical', 'feasible'],
            'risk': ['risk', 'danger', 'harm', 'safe'],
            'impact': ['impact', 'effect', 'consequence', 'result']
        }
        
        rationale_lower = rationale.lower()
        
        for category, keywords in indicators.items():
            if any(keyword in rationale_lower for keyword in keywords):
                considerations.append(category)
        
        return considerations
    
    def _infer_goals(self, operation: str, context: Dict[str, Any]) -> List[str]:
        """Infer likely goals from operation and context."""
        goals = []
        
        # Common operation patterns
        if 'process' in operation.lower():
            goals.append('data_transformation')
        if 'analyze' in operation.lower() or 'analysis' in operation.lower():
            goals.append('insight_generation')
        if 'predict' in operation.lower():
            goals.append('future_estimation')
        if 'classify' in operation.lower():
            goals.append('categorization')
        
        # Context-based inference
        if context.get('purpose'):
            goals.append(f"achieve_{context['purpose']}")
        
        return goals if goals else ['general_operation']
    
    def _calculate_alignment(self, stated: str, inferred: List[str]) -> float:
        """Calculate alignment score between stated and inferred intent."""
        if stated == 'unknown':
            return 0.5
        
        stated_lower = stated.lower()
        
        # Check if stated purpose aligns with any inferred goal
        for goal in inferred:
            if goal.lower() in stated_lower or stated_lower in goal.lower():
                return 0.9
        
        return 0.6  # Moderate alignment if no clear match
    
    def get_reasoning_summary(self) -> Dict[str, Any]:
        """Get summary of reasoning history."""
        if not self.reasoning_history:
            return {'total_decisions': 0}
        
        avg_confidence = sum(
            r['confidence'] for r in self.reasoning_history
        ) / len(self.reasoning_history)
        
        return {
            'total_decisions': len(self.reasoning_history),
            'average_confidence': avg_confidence,
            'recent_decisions': self.reasoning_history[-5:]
        }
