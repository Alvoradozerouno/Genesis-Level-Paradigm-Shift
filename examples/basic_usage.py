"""
Example Usage of Genesis10000+ Framework

Demonstrates basic usage patterns and capabilities.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from genesis10000 import GenesisFramework

def basic_example():
    """Basic framework usage example."""
    print("=" * 60)
    print("Genesis10000+ Basic Example")
    print("=" * 60)
    
    # Initialize the framework
    genesis = GenesisFramework(
        ethical_kernels=['transparency', 'fairness', 'privacy'],
        enable_eira=True,
        enable_orion=True,
        enable_audit=True
    )
    
    print("\n✓ Framework initialized with EIRA, OR1ON, and Audit modules")
    
    # Execute an operation with ethical oversight
    print("\n→ Executing data processing operation...")
    result = genesis.execute_with_oversight(
        operation="data_processing",
        data={"user_id": "12345", "values": [1, 2, 3, 4, 5]},
        context={
            "purpose": "statistical_analysis",
            "contains_personal_data": False,
            "harm_assessment": "none"
        },
        actor="example_system"
    )
    
    print(f"  Success: {result['success']}")
    print(f"  Operation approved by EIRA: {result['oversight']['approved']}")
    print(f"  Intent alignment score: {result['intent']['alignment_score']:.2f}")
    print(f"  Reflection confidence: {result['reflection']['confidence']:.2f}")
    
    # Check system health
    print("\n→ Checking system health...")
    health = genesis.get_system_health()
    print(f"  Framework status: {health['framework_status']}")
    print(f"  OR1ON overall health: {health['orion_report']['overall_health']}")
    print(f"  EIRA approval rate: {health['eira_report']['approval_rate']:.2%}")
    
    # Get compliance report
    print("\n→ Generating compliance report...")
    compliance = genesis.get_compliance_report()
    print(f"  Total operations logged: {compliance['total_operations']}")
    print(f"  Total decisions made: {compliance['total_decisions']}")
    print(f"  Audit integrity verified: {compliance['audit_integrity']['integrity_verified']}")
    
    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


def ethical_blocking_example():
    """Example showing ethical blocking of problematic operations."""
    print("\n" + "=" * 60)
    print("Genesis10000+ Ethical Blocking Example")
    print("=" * 60)
    
    genesis = GenesisFramework(
        ethical_kernels=['privacy', 'non_maleficence'],
        enable_eira=True
    )
    
    print("\n✓ Framework initialized with privacy and harm prevention")
    
    # Try to execute operation without proper consent
    print("\n→ Attempting operation with privacy concerns...")
    result = genesis.execute_with_oversight(
        operation="data_collection",
        data={"sensitive_info": "personal_data"},
        context={
            "purpose": "analysis",
            "contains_personal_data": True,
            "user_consent": False,  # No consent!
            "harm_assessment": "minimal"
        }
    )
    
    print(f"  Success: {result['success']}")
    print(f"  Blocked: {result.get('blocked', False)}")
    print(f"  Reason: {result.get('reason', 'N/A')}")
    if result.get('guidance'):
        print(f"  Guidance: {result['guidance']}")
    
    print("\n" + "=" * 60)


def resilience_example():
    """Example demonstrating OR1ON resilience capabilities."""
    print("\n" + "=" * 60)
    print("Genesis10000+ Resilience Example")
    print("=" * 60)
    
    genesis = GenesisFramework(enable_orion=True)
    
    print("\n✓ Framework initialized with OR1ON module")
    
    # Simulate health monitoring
    print("\n→ Monitoring component health...")
    if genesis.orion:
        health = genesis.orion.monitor_health(
            component="data_processor",
            metrics={
                "response_time": 150,
                "error_rate": 0.02,
                "availability": 0.99
            }
        )
        
        print(f"  Health score: {health['health_score']:.2f}")
        print(f"  Status: {health['status']}")
    
    # Trigger optimization
    print("\n→ Optimizing system performance...")
    optimization = genesis.optimize_system()
    print(f"  Recommendations: {len(optimization.get('recommendations', []))}")
    if optimization.get('recommendations'):
        for rec in optimization['recommendations']:
            print(f"    - {rec.get('action', 'N/A')} (Priority: {rec.get('priority', 'N/A')})")
    
    print("\n" + "=" * 60)


def alignment_example():
    """Example demonstrating value alignment verification."""
    print("\n" + "=" * 60)
    print("Genesis10000+ Value Alignment Example")
    print("=" * 60)
    
    genesis = GenesisFramework(enable_eira=True)
    
    print("\n✓ Framework initialized with EIRA module")
    
    # Verify alignment
    print("\n→ Verifying value alignment...")
    alignment = genesis.verify_alignment(
        intended_values=['transparency', 'fairness', 'safety'],
        observed_behavior={
            'documented': True,
            'explained': True,
            'unbiased': True,
            'tested': True,
            'safe': True
        }
    )
    
    print(f"  Is aligned: {alignment['is_aligned']}")
    print(f"  Overall alignment: {alignment['overall_alignment']:.2%}")
    print(f"  Individual scores:")
    for value, score in alignment['alignment_scores'].items():
        print(f"    - {value}: {score:.2%}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    # Run all examples
    basic_example()
    ethical_blocking_example()
    resilience_example()
    alignment_example()
    
    print("\n🎉 All examples completed successfully!")
    print("Genesis10000+ is ready for paradigm-shifting AI operations!")
