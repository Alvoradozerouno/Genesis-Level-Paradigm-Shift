"""
Ethical Kernel - Core ethical principles and validation
"""

from typing import Dict, List, Any, Optional
from enum import Enum
import logging


class EthicalPrinciple(Enum):
    """Core ethical principles."""
    TRANSPARENCY = "transparency"
    FAIRNESS = "fairness"
    PRIVACY = "privacy"
    ACCOUNTABILITY = "accountability"
    BENEFICENCE = "beneficence"
    NON_MALEFICENCE = "non_maleficence"
    AUTONOMY = "autonomy"
    JUSTICE = "justice"


class EthicalKernel:
    """
    Ethical Kernel implementing core ethical validation and principles.
    
    This class ensures all AI operations align with defined ethical standards.
    """
    
    def __init__(self, principles: Optional[List[str]] = None):
        """
        Initialize the Ethical Kernel.
        
        Args:
            principles: List of ethical principles to enforce. Defaults to all.
        """
        self.logger = logging.getLogger(__name__)
        
        if principles is None:
            self.active_principles = [p for p in EthicalPrinciple]
        else:
            self.active_principles = [
                EthicalPrinciple(p) for p in principles
            ]
        
        self.violations = []
        self.logger.info(f"Ethical Kernel initialized with {len(self.active_principles)} principles")
    
    def validate_operation(
        self,
        operation: str,
        data: Any,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Validate an operation against ethical principles.
        
        Args:
            operation: The operation to validate
            data: Data being processed
            context: Contextual information about the operation
            
        Returns:
            Validation result with approval status and recommendations
        """
        violations = []
        recommendations = []
        
        for principle in self.active_principles:
            result = self._check_principle(principle, operation, data, context)
            if not result['compliant']:
                violations.append(result)
            if result.get('recommendations'):
                recommendations.extend(result['recommendations'])
        
        is_approved = len(violations) == 0
        
        return {
            'approved': is_approved,
            'violations': violations,
            'recommendations': recommendations,
            'principles_checked': [p.value for p in self.active_principles]
        }
    
    def _check_principle(
        self,
        principle: EthicalPrinciple,
        operation: str,
        data: Any,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Check a specific ethical principle."""
        
        if principle == EthicalPrinciple.TRANSPARENCY:
            return self._check_transparency(operation, context)
        elif principle == EthicalPrinciple.FAIRNESS:
            return self._check_fairness(operation, data, context)
        elif principle == EthicalPrinciple.PRIVACY:
            return self._check_privacy(operation, data, context)
        elif principle == EthicalPrinciple.ACCOUNTABILITY:
            return self._check_accountability(operation, context)
        elif principle == EthicalPrinciple.NON_MALEFICENCE:
            return self._check_non_maleficence(operation, context)
        else:
            return {'compliant': True, 'principle': principle.value}
    
    def _check_transparency(self, operation: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Validate transparency principle."""
        has_purpose = 'purpose' in context
        has_documentation = 'description' in context or 'documentation' in context
        
        compliant = has_purpose
        recommendations = []
        
        if not has_purpose:
            recommendations.append("Add 'purpose' to context for transparency")
        if not has_documentation:
            recommendations.append("Consider adding operation documentation")
        
        return {
            'principle': EthicalPrinciple.TRANSPARENCY.value,
            'compliant': compliant,
            'recommendations': recommendations
        }
    
    def _check_fairness(self, operation: str, data: Any, context: Dict[str, Any]) -> Dict[str, Any]:
        """Validate fairness principle."""
        # Check for bias indicators
        bias_check = context.get('bias_assessment', True)
        
        return {
            'principle': EthicalPrinciple.FAIRNESS.value,
            'compliant': bias_check,
            'recommendations': [] if bias_check else ["Perform bias assessment"]
        }
    
    def _check_privacy(self, operation: str, data: Any, context: Dict[str, Any]) -> Dict[str, Any]:
        """Validate privacy principle."""
        has_consent = context.get('user_consent', False)
        has_anonymization = context.get('anonymized', False)
        
        # If processing personal data, require consent or anonymization
        is_personal_data = context.get('contains_personal_data', False)
        
        compliant = True
        recommendations = []
        
        if is_personal_data and not (has_consent or has_anonymization):
            compliant = False
            recommendations.append("Personal data requires consent or anonymization")
        
        return {
            'principle': EthicalPrinciple.PRIVACY.value,
            'compliant': compliant,
            'recommendations': recommendations
        }
    
    def _check_accountability(self, operation: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Validate accountability principle."""
        has_responsible_party = 'responsible_party' in context or 'owner' in context
        has_audit_enabled = context.get('audit_enabled', True)
        
        compliant = has_audit_enabled
        recommendations = []
        
        if not has_responsible_party:
            recommendations.append("Assign responsible party for accountability")
        
        return {
            'principle': EthicalPrinciple.ACCOUNTABILITY.value,
            'compliant': compliant,
            'recommendations': recommendations
        }
    
    def _check_non_maleficence(self, operation: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Validate non-maleficence (do no harm) principle."""
        harm_assessment = context.get('harm_assessment', 'unknown')
        
        compliant = harm_assessment == 'none' or harm_assessment == 'minimal'
        recommendations = []
        
        if harm_assessment == 'unknown':
            recommendations.append("Conduct harm assessment before proceeding")
            compliant = False
        elif harm_assessment in ['moderate', 'high']:
            recommendations.append("High harm risk detected - review operation")
            compliant = False
        
        return {
            'principle': EthicalPrinciple.NON_MALEFICENCE.value,
            'compliant': compliant,
            'recommendations': recommendations
        }
    
    def get_principle_description(self, principle: str) -> str:
        """Get description of an ethical principle."""
        descriptions = {
            'transparency': 'Operations must be clear, explainable, and well-documented',
            'fairness': 'Decisions must be unbiased and equitable across all groups',
            'privacy': 'Personal data must be protected and used with consent',
            'accountability': 'Clear responsibility and audit trails for all actions',
            'beneficence': 'Actions should actively promote well-being',
            'non_maleficence': 'Prevent harm and minimize negative impacts',
            'autonomy': 'Respect individual choice and self-determination',
            'justice': 'Fair distribution of benefits and burdens'
        }
        return descriptions.get(principle, 'No description available')
