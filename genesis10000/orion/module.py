"""
OR1ON - Operational Resilience & Intelligent Optimization Network

Advanced operational intelligence for adaptive, resilient AI systems.
"""

from typing import Dict, Any, List, Optional, Callable
import logging
from datetime import datetime, timedelta
from collections import deque


class OR1ONModule:
    """
    OR1ON (Operational Resilience & Intelligent Optimization Network)
    
    Provides self-monitoring, performance optimization, failure recovery,
    and proactive learning capabilities.
    """
    
    def __init__(self, self_reflection=None):
        """
        Initialize OR1ON module.
        
        Args:
            self_reflection: AdaptiveSelfReflection instance for learning
        """
        self.logger = logging.getLogger(__name__)
        self.self_reflection = self_reflection
        self.health_status = 'healthy'
        self.health_checks = deque(maxlen=100)
        self.performance_history = deque(maxlen=1000)
        self.recovery_strategies = {}
        self.optimizations = []
        
        self.logger.info("OR1ON module initialized")
    
    def monitor_health(
        self,
        component: str,
        metrics: Dict[str, float]
    ) -> Dict[str, Any]:
        """
        Monitor health of a system component.
        
        Args:
            component: Name of component to monitor
            metrics: Health metrics (e.g., response_time, error_rate)
            
        Returns:
            Health assessment
        """
        # Analyze metrics
        health_score = self._calculate_health_score(metrics)
        
        status = 'healthy'
        if health_score < 0.5:
            status = 'critical'
        elif health_score < 0.7:
            status = 'degraded'
        elif health_score < 0.9:
            status = 'warning'
        
        check = {
            'component': component,
            'metrics': metrics,
            'health_score': health_score,
            'status': status,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        self.health_checks.append(check)
        
        # Update overall health status
        self._update_overall_health()
        
        # Trigger recovery if needed
        if status in ['critical', 'degraded']:
            recovery = self.recover_from_failure(component, check)
            check['recovery_initiated'] = recovery
        
        return check
    
    def optimize_performance(
        self,
        operation: str,
        current_metrics: Dict[str, float],
        target_metrics: Optional[Dict[str, float]] = None
    ) -> Dict[str, Any]:
        """
        Optimize performance of an operation.
        
        Args:
            operation: Operation to optimize
            current_metrics: Current performance metrics
            target_metrics: Optional target metrics to achieve
            
        Returns:
            Optimization recommendations
        """
        optimization = {
            'operation': operation,
            'current_metrics': current_metrics,
            'target_metrics': target_metrics or {},
            'recommendations': [],
            'estimated_improvement': 0.0,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Analyze performance bottlenecks
        bottlenecks = self._identify_bottlenecks(current_metrics, target_metrics)
        
        # Generate optimization recommendations
        for bottleneck in bottlenecks:
            recommendation = self._generate_optimization(bottleneck, current_metrics)
            optimization['recommendations'].append(recommendation)
        
        # Estimate potential improvement
        if optimization['recommendations']:
            optimization['estimated_improvement'] = self._estimate_improvement(
                optimization['recommendations']
            )
        
        self.optimizations.append(optimization)
        
        # Log to self-reflection if available
        if self.self_reflection:
            self.self_reflection.log_behavior(
                'optimization',
                f"Optimized {operation}",
                optimization
            )
        
        return optimization
    
    def recover_from_failure(
        self,
        component: str,
        failure_info: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Implement recovery strategy for a failed component.
        
        Args:
            component: Failed component
            failure_info: Information about the failure
            
        Returns:
            Recovery result
        """
        recovery = {
            'component': component,
            'failure_info': failure_info,
            'strategy': None,
            'success': False,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Select recovery strategy
        if component in self.recovery_strategies:
            recovery['strategy'] = self.recovery_strategies[component]
        else:
            recovery['strategy'] = self._select_recovery_strategy(
                component,
                failure_info
            )
        
        # Log recovery attempt
        self.logger.warning(
            f"Initiating recovery for {component} using strategy: {recovery['strategy']}"
        )
        
        # Simulate recovery (in real implementation, this would execute actual recovery)
        recovery['success'] = True  # Assume recovery succeeds
        recovery['actions_taken'] = self._execute_recovery_strategy(
            recovery['strategy'],
            component
        )
        
        # Learn from failure if self-reflection is available
        if self.self_reflection:
            self.self_reflection.consolidate_knowledge(
                f"Failure in {component}",
                f"Recovered using {recovery['strategy']}",
                'failure_recovery'
            )
        
        return recovery
    
    def learn_from_experience(
        self,
        experience_type: str,
        details: Dict[str, Any],
        outcome: str
    ) -> Dict[str, Any]:
        """
        Proactively learn from operational experiences.
        
        Args:
            experience_type: Type of experience (success, failure, anomaly)
            details: Details about the experience
            outcome: Result or outcome
            
        Returns:
            Learning summary
        """
        learning = {
            'type': experience_type,
            'details': details,
            'outcome': outcome,
            'insights': [],
            'actions': [],
            'timestamp': datetime.utcnow().isoformat()
        }
        
        # Extract insights
        if experience_type == 'failure':
            learning['insights'].append('Identify failure patterns')
            learning['actions'].append('Update recovery strategies')
        elif experience_type == 'success':
            learning['insights'].append('Identify success patterns')
            learning['actions'].append('Replicate successful approaches')
        elif experience_type == 'anomaly':
            learning['insights'].append('Investigate unusual patterns')
            learning['actions'].append('Enhance monitoring')
        
        # Store in self-reflection if available
        if self.self_reflection:
            self.self_reflection.consolidate_knowledge(
                f"{experience_type}: {details.get('description', 'N/A')}",
                f"Outcome: {outcome}",
                experience_type
            )
        
        return learning
    
    def get_resilience_report(self) -> Dict[str, Any]:
        """Generate resilience and operational report."""
        recent_checks = list(self.health_checks)[-20:] if self.health_checks else []
        
        if not recent_checks:
            return {
                'overall_health': 'unknown',
                'avg_health_score': 0.0,
                'total_checks': 0,
                'optimizations_performed': 0
            }
        
        avg_health = sum(c['health_score'] for c in recent_checks) / len(recent_checks)
        
        critical_count = sum(1 for c in recent_checks if c['status'] == 'critical')
        degraded_count = sum(1 for c in recent_checks if c['status'] == 'degraded')
        
        return {
            'overall_health': self.health_status,
            'avg_health_score': avg_health,
            'total_checks': len(self.health_checks),
            'critical_incidents': critical_count,
            'degraded_incidents': degraded_count,
            'optimizations_performed': len(self.optimizations),
            'recent_health_checks': recent_checks[-5:]
        }
    
    def _calculate_health_score(self, metrics: Dict[str, float]) -> float:
        """Calculate overall health score from metrics."""
        if not metrics:
            return 0.5
        
        # Common metric interpretations
        score = 1.0
        
        if 'error_rate' in metrics:
            # Lower error rate is better
            score -= min(metrics['error_rate'], 0.5)
        
        if 'response_time' in metrics:
            # Penalize high response times (assuming milliseconds)
            if metrics['response_time'] > 1000:
                score -= 0.3
            elif metrics['response_time'] > 500:
                score -= 0.1
        
        if 'availability' in metrics:
            # Higher availability is better (assuming 0-1 scale)
            score = score * metrics['availability']
        
        if 'success_rate' in metrics:
            # Higher success rate is better (assuming 0-1 scale)
            score = score * metrics['success_rate']
        
        return max(min(score, 1.0), 0.0)
    
    def _update_overall_health(self) -> None:
        """Update overall system health status."""
        if not self.health_checks:
            self.health_status = 'unknown'
            return
        
        recent = list(self.health_checks)[-10:]
        avg_score = sum(c['health_score'] for c in recent) / len(recent)
        
        if avg_score < 0.5:
            self.health_status = 'critical'
        elif avg_score < 0.7:
            self.health_status = 'degraded'
        elif avg_score < 0.9:
            self.health_status = 'warning'
        else:
            self.health_status = 'healthy'
    
    def _identify_bottlenecks(
        self,
        current: Dict[str, float],
        target: Optional[Dict[str, float]]
    ) -> List[str]:
        """Identify performance bottlenecks."""
        bottlenecks = []
        
        if not target:
            # Use heuristics for common bottlenecks
            if current.get('response_time', 0) > 500:
                bottlenecks.append('high_latency')
            if current.get('memory_usage', 0) > 0.8:
                bottlenecks.append('high_memory')
            if current.get('cpu_usage', 0) > 0.8:
                bottlenecks.append('high_cpu')
            return bottlenecks
        
        # Compare with targets
        for metric, target_value in target.items():
            current_value = current.get(metric, 0)
            if current_value > target_value * 1.2:  # 20% threshold
                bottlenecks.append(f'{metric}_exceeds_target')
        
        return bottlenecks
    
    def _generate_optimization(
        self,
        bottleneck: str,
        metrics: Dict[str, float]
    ) -> Dict[str, Any]:
        """Generate optimization recommendation for a bottleneck."""
        optimizations = {
            'high_latency': {
                'action': 'implement_caching',
                'priority': 'high',
                'expected_gain': '30-50% latency reduction'
            },
            'high_memory': {
                'action': 'optimize_data_structures',
                'priority': 'medium',
                'expected_gain': '20-40% memory reduction'
            },
            'high_cpu': {
                'action': 'parallelize_operations',
                'priority': 'high',
                'expected_gain': '25-60% cpu reduction'
            }
        }
        
        return optimizations.get(bottleneck, {
            'action': 'investigate_further',
            'priority': 'low',
            'expected_gain': 'unknown'
        })
    
    def _estimate_improvement(self, recommendations: List[Dict[str, Any]]) -> float:
        """Estimate overall improvement from recommendations."""
        priority_weights = {'high': 0.3, 'medium': 0.2, 'low': 0.1}
        
        total_improvement = sum(
            priority_weights.get(r.get('priority', 'low'), 0.1)
            for r in recommendations
        )
        
        return min(total_improvement, 0.7)  # Cap at 70% improvement
    
    def _select_recovery_strategy(
        self,
        component: str,
        failure_info: Dict[str, Any]
    ) -> str:
        """Select appropriate recovery strategy."""
        status = failure_info.get('status', 'unknown')
        
        if status == 'critical':
            return 'restart_component'
        elif status == 'degraded':
            return 'reduce_load'
        else:
            return 'monitor_and_wait'
    
    def _execute_recovery_strategy(
        self,
        strategy: str,
        component: str
    ) -> List[str]:
        """Execute recovery strategy and return actions taken."""
        actions = {
            'restart_component': [
                f'Gracefully shutdown {component}',
                f'Clear component state',
                f'Restart {component}',
                'Verify health after restart'
            ],
            'reduce_load': [
                f'Enable rate limiting for {component}',
                'Redirect traffic to healthy instances',
                'Monitor recovery progress'
            ],
            'monitor_and_wait': [
                f'Increase monitoring frequency for {component}',
                'Set up alerts for further degradation',
                'Continue normal operation'
            ]
        }
        
        return actions.get(strategy, ['Log issue and notify operators'])
