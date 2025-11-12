"""
Unit tests for Ethical Kernel
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from genesis10000.core.ethical_kernel import EthicalKernel, EthicalPrinciple


def test_ethical_kernel_initialization():
    """Test EthicalKernel initialization."""
    kernel = EthicalKernel()
    assert kernel is not None
    assert len(kernel.active_principles) > 0


def test_ethical_kernel_with_specific_principles():
    """Test EthicalKernel with specific principles."""
    kernel = EthicalKernel(['transparency', 'fairness'])
    assert len(kernel.active_principles) == 2
    assert EthicalPrinciple.TRANSPARENCY in kernel.active_principles
    assert EthicalPrinciple.FAIRNESS in kernel.active_principles


def test_validate_operation_approved():
    """Test operation validation that should be approved."""
    kernel = EthicalKernel(['transparency'])
    
    result = kernel.validate_operation(
        operation='test_op',
        data={'test': 'data'},
        context={'purpose': 'testing', 'audit_enabled': True}
    )
    
    assert result['approved'] == True
    assert 'principles_checked' in result


def test_validate_operation_rejected():
    """Test operation validation that should be rejected."""
    kernel = EthicalKernel(['privacy'])
    
    result = kernel.validate_operation(
        operation='data_processing',
        data={'personal': 'data'},
        context={
            'contains_personal_data': True,
            'user_consent': False,
            'anonymized': False
        }
    )
    
    assert result['approved'] == False
    assert len(result['violations']) > 0


def test_transparency_check():
    """Test transparency principle check."""
    kernel = EthicalKernel(['transparency'])
    
    # Should pass with purpose
    result = kernel.validate_operation(
        'test', {}, {'purpose': 'testing'}
    )
    assert result['approved'] == True
    
    # Should fail without purpose
    result = kernel.validate_operation(
        'test', {}, {}
    )
    assert result['approved'] == False


def test_get_principle_description():
    """Test getting principle descriptions."""
    kernel = EthicalKernel()
    
    description = kernel.get_principle_description('transparency')
    assert isinstance(description, str)
    assert len(description) > 0


if __name__ == '__main__':
    # Run tests manually
    print("Running Ethical Kernel tests...")
    test_ethical_kernel_initialization()
    print("✓ Initialization test passed")
    
    test_ethical_kernel_with_specific_principles()
    print("✓ Specific principles test passed")
    
    test_validate_operation_approved()
    print("✓ Operation approval test passed")
    
    test_validate_operation_rejected()
    print("✓ Operation rejection test passed")
    
    test_transparency_check()
    print("✓ Transparency check test passed")
    
    test_get_principle_description()
    print("✓ Principle description test passed")
    
    print("\n✓ All Ethical Kernel tests passed!")
