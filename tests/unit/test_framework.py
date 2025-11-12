"""
Unit tests for Genesis Framework
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from genesis10000 import GenesisFramework


def test_framework_initialization():
    """Test framework initialization."""
    framework = GenesisFramework()
    assert framework is not None
    assert framework.ethical_kernel is not None
    assert framework.conscious_design is not None
    assert framework.self_reflection is not None


def test_framework_with_eira_orion():
    """Test framework with EIRA and OR1ON enabled."""
    framework = GenesisFramework(
        enable_eira=True,
        enable_orion=True
    )
    
    assert framework.eira is not None
    assert framework.orion is not None


def test_execute_with_oversight():
    """Test executing operation with oversight."""
    framework = GenesisFramework(
        ethical_kernels=['transparency'],
        enable_eira=True
    )
    
    result = framework.execute_with_oversight(
        operation='test_operation',
        data={'test': 'data'},
        context={
            'purpose': 'testing',
            'harm_assessment': 'none'
        }
    )
    
    assert 'success' in result
    assert 'oversight' in result
    assert 'intent' in result
    assert 'reflection' in result


def test_ethical_blocking():
    """Test that unethical operations are blocked."""
    framework = GenesisFramework(
        ethical_kernels=['privacy'],
        enable_eira=True
    )
    
    result = framework.execute_with_oversight(
        operation='data_collection',
        data={'sensitive': 'info'},
        context={
            'purpose': 'testing',
            'contains_personal_data': True,
            'user_consent': False,
            'anonymized': False
        }
    )
    
    assert result['success'] == False
    assert result.get('blocked', False) == True


def test_get_system_health():
    """Test getting system health report."""
    framework = GenesisFramework(
        enable_eira=True,
        enable_orion=True
    )
    
    health = framework.get_system_health()
    
    assert 'framework_status' in health
    assert 'enabled_modules' in health
    assert health['framework_status'] == 'operational'


def test_verify_alignment():
    """Test value alignment verification."""
    framework = GenesisFramework(enable_eira=True)
    
    result = framework.verify_alignment(
        intended_values=['transparency', 'fairness'],
        observed_behavior={'documented': True, 'unbiased': True}
    )
    
    assert 'is_aligned' in result
    assert 'alignment_scores' in result
    assert 'overall_alignment' in result


def test_audit_trail():
    """Test audit trail functionality."""
    framework = GenesisFramework(enable_audit=True)
    
    # Execute an operation
    framework.execute_with_oversight(
        operation='test',
        data={},
        context={'purpose': 'testing', 'harm_assessment': 'none'}
    )
    
    # Get audit trail
    trail = framework.get_audit_trail()
    
    assert isinstance(trail, list)
    assert len(trail) > 0


if __name__ == '__main__':
    # Run tests manually
    print("Running Genesis Framework tests...")
    
    test_framework_initialization()
    print("✓ Framework initialization test passed")
    
    test_framework_with_eira_orion()
    print("✓ EIRA/OR1ON test passed")
    
    test_execute_with_oversight()
    print("✓ Execute with oversight test passed")
    
    test_ethical_blocking()
    print("✓ Ethical blocking test passed")
    
    test_get_system_health()
    print("✓ System health test passed")
    
    test_verify_alignment()
    print("✓ Alignment verification test passed")
    
    test_audit_trail()
    print("✓ Audit trail test passed")
    
    print("\n✓ All Genesis Framework tests passed!")
