"""
Integration tests for Genesis10000+ Framework

Tests the complete framework with all modules working together.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from genesis10000 import GenesisFramework


def test_full_framework_integration():
    """Test complete framework integration with all modules."""
    print("\n=== Full Framework Integration Test ===")
    
    # Initialize with all modules
    framework = GenesisFramework(
        ethical_kernels=['transparency', 'fairness', 'privacy', 'accountability'],
        enable_eira=True,
        enable_orion=True,
        enable_audit=True
    )
    
    print("✓ Framework initialized")
    
    # Test 1: Successful operation
    result = framework.execute_with_oversight(
        operation="data_processing",
        data={"values": [1, 2, 3, 4, 5]},
        context={
            "purpose": "statistical_analysis",
            "harm_assessment": "none",
            "contains_personal_data": False
        },
        actor="test_system"
    )
    
    assert result['success'] == True, "Operation should succeed"
    assert result['oversight']['approved'] == True, "Should be approved by EIRA"
    print("✓ Test 1: Successful operation passed")
    
    # Test 2: Blocked unethical operation
    result = framework.execute_with_oversight(
        operation="data_collection",
        data={"sensitive": "data"},
        context={
            "purpose": "testing",
            "contains_personal_data": True,
            "user_consent": False,
            "anonymized": False
        }
    )
    
    assert result['success'] == False, "Operation should fail"
    assert result.get('blocked') == True, "Should be blocked"
    print("✓ Test 2: Ethical blocking passed")
    
    # Test 3: System health check
    health = framework.get_system_health()
    
    assert health['framework_status'] == 'operational', "Framework should be operational"
    assert 'orion_report' in health, "Should have OR1ON report"
    assert 'eira_report' in health, "Should have EIRA report"
    print("✓ Test 3: System health check passed")
    
    # Test 4: Audit trail
    trail = framework.get_audit_trail()
    
    assert len(trail) > 0, "Should have audit entries"
    assert any(e['type'] == 'operation' for e in trail), "Should have operation logs"
    print("✓ Test 4: Audit trail passed")
    
    # Test 5: Value alignment
    alignment = framework.verify_alignment(
        intended_values=['transparency', 'fairness'],
        observed_behavior={'documented': True, 'unbiased': True, 'explained': True}
    )
    
    assert 'alignment_scores' in alignment, "Should have alignment scores"
    assert 'overall_alignment' in alignment, "Should have overall alignment"
    print("✓ Test 5: Value alignment passed")
    
    # Test 6: Performance optimization
    if framework.orion:
        optimization = framework.optimize_system()
        assert 'recommendations' in optimization, "Should have recommendations"
        print("✓ Test 6: Performance optimization passed")
    
    # Test 7: Compliance report
    compliance = framework.get_compliance_report()
    
    assert compliance['total_operations'] >= 2, "Should have logged operations"
    assert 'audit_integrity' in compliance, "Should have integrity check"
    assert compliance['audit_integrity']['integrity_verified'] == True, "Integrity should be verified"
    print("✓ Test 7: Compliance report passed")
    
    # Test 8: Multiple operations in sequence
    for i in range(3):
        result = framework.execute_with_oversight(
            operation=f"test_operation_{i}",
            data={"test": i},
            context={
                "purpose": "sequential_testing",
                "harm_assessment": "none"
            }
        )
        assert result['success'] == True, f"Operation {i} should succeed"
    
    print("✓ Test 8: Sequential operations passed")
    
    # Final health check
    final_health = framework.get_system_health()
    print(f"\nFinal System Status:")
    print(f"  Framework: {final_health['framework_status']}")
    print(f"  OR1ON Health: {final_health['orion_report']['overall_health']}")
    print(f"  EIRA Approval Rate: {final_health['eira_report']['approval_rate']:.0%}")
    print(f"  Total Operations: {final_health['eira_report']['total_decisions']}")
    
    print("\n✓ All integration tests passed!")
    return True


def test_eira_orion_interaction():
    """Test interaction between EIRA and OR1ON modules."""
    print("\n=== EIRA-OR1ON Interaction Test ===")
    
    framework = GenesisFramework(
        ethical_kernels=['transparency', 'fairness'],
        enable_eira=True,
        enable_orion=True
    )
    
    # Execute operation that triggers both modules
    result = framework.execute_with_oversight(
        operation="complex_analysis",
        data={"large_dataset": "simulated"},
        context={
            "purpose": "comprehensive_analysis",
            "harm_assessment": "minimal",
            "bias_assessment": True
        }
    )
    
    # Verify both modules were involved
    assert 'oversight' in result, "EIRA oversight should be present"
    assert 'reflection' in result, "Self-reflection should be present"
    
    # Check OR1ON health monitoring
    health = framework.get_system_health()
    assert health['orion_report']['total_checks'] > 0, "OR1ON should have health checks"
    
    print("✓ EIRA-OR1ON interaction test passed")
    return True


def test_conscious_design_reflection():
    """Test conscious design and self-reflection capabilities."""
    print("\n=== Conscious Design & Reflection Test ===")
    
    framework = GenesisFramework()
    
    # Execute operations to build history
    for i in range(5):
        result = framework.execute_with_oversight(
            operation=f"learning_operation_{i}",
            data={"iteration": i},
            context={
                "purpose": "learning_test",
                "harm_assessment": "none"
            }
        )
        
        # Verify conscious design elements
        assert 'intent' in result, "Should have intent recognition"
        assert 'reflection' in result, "Should have reflection"
        assert 'goal_validation' in result, "Should have goal validation"
    
    # Check self-reflection summary
    health = framework.get_system_health()
    reflection_summary = health['reflection_summary']
    
    assert reflection_summary['total_operations'] >= 5, "Should have tracked operations"
    
    print("✓ Conscious design and reflection test passed")
    return True


if __name__ == '__main__':
    print("\n" + "="*60)
    print("Running Genesis10000+ Integration Tests")
    print("="*60)
    
    try:
        test_full_framework_integration()
        test_eira_orion_interaction()
        test_conscious_design_reflection()
        
        print("\n" + "="*60)
        print("🎉 ALL INTEGRATION TESTS PASSED!")
        print("="*60)
        print("\nGenesis10000+ framework is fully operational and ready for use.")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
