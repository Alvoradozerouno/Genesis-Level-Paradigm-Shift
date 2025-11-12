"""
Adaptive Self-Reflection - Continuous learning and improvement
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import logging


class AdaptiveSelfReflection:
    """
    Implements adaptive self-reflection for continuous learning and improvement.
    
    Monitors performance, analyzes behavior, and adapts strategies.
    """
    
    def __init__(self):
        """Initialize Adaptive Self-Reflection."""
        self.logger = logging.getLogger(__name__)
        self.performance_metrics = []
        self.behavior_logs = []
        self.adaptations = []
        self.knowledge_base = {}
        
    def monitor_performance(
        self,
        operation: str,
        metrics: Dict[str, float],
        success: bool
    ) -> Dict[str, Any]:
        """
        Monitor and record performance of an operation.
        
        Args:
            operation: The operation performed
            metrics: Performance metrics (e.g., accuracy, speed)
            success: Whether operation succeeded
            
        Returns:
            Performance analysis
        """
        record = {
            'operation': operation,
            'metrics': metrics,
            'success': success,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        self.performance_metrics.append(record)
        
        # Analyze if adaptation is needed
        analysis = self._analyze_performance_trend(operation)
        
        return {
            'record': record,
            'trend_analysis': analysis,
            'recommendation': self._generate_recommendation(analysis)
        }
    
    def log_behavior(
        self,
        behavior_type: str,
        description: str,
        context: Dict[str, Any]
    ) -> None:
        """
        Log a specific behavior for later analysis.
        
        Args:
            behavior_type: Type of behavior observed
            description: Description of the behavior
            context: Contextual information
        """
        self.behavior_logs.append({
            'type': behavior_type,
            'description': description,
            'context': context,
            'timestamp': datetime.utcnow().isoformat()
        })
    
    def adapt_strategy(
        self,
        current_strategy: str,
        performance_data: Dict[str, Any],
        constraints: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Adapt strategy based on performance data.
        
        Args:
            current_strategy: Current approach being used
            performance_data: Recent performance information
            constraints: Constraints to consider in adaptation
            
        Returns:
            New strategy recommendation
        """
        adaptation = {
            'current_strategy': current_strategy,
            'performance_data': performance_data,
            'new_strategy': None,
            'confidence': 0.0,
            'reasoning': '',
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Simple adaptive logic
        if performance_data.get('success_rate', 1.0) < 0.7:
            adaptation['new_strategy'] = f"{current_strategy}_optimized"
            adaptation['confidence'] = 0.75
            adaptation['reasoning'] = "Low success rate detected, optimizing strategy"
        elif performance_data.get('success_rate', 1.0) > 0.95:
            adaptation['new_strategy'] = current_strategy
            adaptation['confidence'] = 0.9
            adaptation['reasoning'] = "Strategy performing well, no change needed"
        else:
            adaptation['new_strategy'] = current_strategy
            adaptation['confidence'] = 0.8
            adaptation['reasoning'] = "Strategy performing adequately"
        
        self.adaptations.append(adaptation)
        
        return adaptation
    
    def consolidate_knowledge(
        self,
        experience: str,
        learning: str,
        category: str
    ) -> None:
        """
        Consolidate learned knowledge into knowledge base.
        
        Args:
            experience: The experience that led to learning
            learning: What was learned
            category: Category of knowledge
        """
        if category not in self.knowledge_base:
            self.knowledge_base[category] = []
        
        self.knowledge_base[category].append({
            'experience': experience,
            'learning': learning,
            'timestamp': datetime.utcnow().isoformat()
        })
    
    def retrieve_knowledge(self, category: str) -> List[Dict[str, Any]]:
        """Retrieve knowledge from a specific category."""
        return self.knowledge_base.get(category, [])
    
    def get_reflection_summary(self) -> Dict[str, Any]:
        """Generate summary of self-reflection activities."""
        total_operations = len(self.performance_metrics)
        
        if total_operations == 0:
            return {
                'total_operations': 0,
                'success_rate': 0.0,
                'adaptations_made': 0,
                'knowledge_categories': 0
            }
        
        successful = sum(
            1 for m in self.performance_metrics if m['success']
        )
        
        return {
            'total_operations': total_operations,
            'success_rate': successful / total_operations,
            'adaptations_made': len(self.adaptations),
            'knowledge_categories': len(self.knowledge_base),
            'behavior_logs': len(self.behavior_logs)
        }
    
    def _analyze_performance_trend(self, operation: str) -> Dict[str, Any]:
        """Analyze performance trend for a specific operation."""
        relevant_metrics = [
            m for m in self.performance_metrics
            if m['operation'] == operation
        ]
        
        if len(relevant_metrics) < 2:
            return {'trend': 'insufficient_data', 'direction': 'unknown'}
        
        recent = relevant_metrics[-5:]
        success_rate = sum(1 for m in recent if m['success']) / len(recent)
        
        if success_rate > 0.8:
            trend = 'positive'
        elif success_rate < 0.5:
            trend = 'negative'
        else:
            trend = 'stable'
        
        return {
            'trend': trend,
            'success_rate': success_rate,
            'sample_size': len(recent)
        }
    
    def _generate_recommendation(self, analysis: Dict[str, Any]) -> str:
        """Generate recommendation based on trend analysis."""
        trend = analysis.get('trend', 'unknown')
        
        recommendations = {
            'positive': 'Continue current approach, monitor for consistency',
            'negative': 'Consider strategy adaptation or intervention',
            'stable': 'Performance is adequate, minor optimizations may help',
            'insufficient_data': 'Collect more data before making changes',
            'unknown': 'Insufficient information for recommendation'
        }
        
        return recommendations.get(trend, recommendations['unknown'])
