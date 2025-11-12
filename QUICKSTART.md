# Quick Start Guide

## Installation

```bash
# Clone the repository
git clone https://github.com/Alvoradozerouno/Genesis-Level-Paradigm-Shift.git
cd Genesis-Level-Paradigm-Shift

# Install (optional - framework works without installation)
pip install -e .
```

## 5-Minute Quick Start

### 1. Basic Usage

```python
from genesis10000 import GenesisFramework

# Initialize framework
genesis = GenesisFramework(
    ethical_kernels=['transparency', 'fairness', 'privacy'],
    enable_eira=True,
    enable_orion=True
)

# Execute operation with ethical oversight
result = genesis.execute_with_oversight(
    operation="data_analysis",
    data={"values": [1, 2, 3, 4, 5]},
    context={
        "purpose": "statistical_analysis",
        "harm_assessment": "none"
    }
)

print(f"Success: {result['success']}")
print(f"Approved: {result['oversight']['approved']}")
```

### 2. Ethical Blocking Example

```python
# Framework will block unethical operations
result = genesis.execute_with_oversight(
    operation="data_collection",
    data={"personal_info": "sensitive"},
    context={
        "purpose": "analysis",
        "contains_personal_data": True,
        "user_consent": False  # No consent = blocked!
    }
)

print(f"Blocked: {result.get('blocked', False)}")
print(f"Guidance: {result.get('guidance')}")
```

### 3. System Health Monitoring

```python
# Check system health
health = genesis.get_system_health()
print(f"Framework: {health['framework_status']}")
print(f"OR1ON Health: {health['orion_report']['overall_health']}")
print(f"EIRA Approval Rate: {health['eira_report']['approval_rate']:.0%}")
```

### 4. Compliance and Auditing

```python
# Get compliance report
report = genesis.get_compliance_report()
print(f"Operations: {report['total_operations']}")
print(f"Decisions: {report['total_decisions']}")
print(f"Audit Verified: {report['audit_integrity']['integrity_verified']}")
```

## Run Examples

```bash
# Run the comprehensive example
python examples/basic_usage.py
```

## Run Tests

```bash
# Run all tests
python tests/unit/test_ethical_kernel.py
python tests/unit/test_framework.py
```

## What's Next?

- Read the [API Documentation](docs/API.md)
- Learn about [Configuration](docs/CONFIGURATION.md)
- Review [Contributing Guidelines](CONTRIBUTING.md)
- Explore more examples in the `examples/` directory

## Key Concepts

### EIRA (Ethical Intelligence & Responsible Architecture)
- Provides ethical oversight for all operations
- Assesses impact and potential harm
- Verifies value alignment
- Prevents harmful actions

### OR1ON (Operational Resilience & Intelligent Optimization Network)
- Monitors system health
- Optimizes performance
- Recovers from failures
- Learns from experiences

### Ethical Kernels
Core principles that guide AI behavior:
- **Transparency**: Clear and explainable operations
- **Fairness**: Unbiased decisions
- **Privacy**: Protected personal data
- **Accountability**: Clear responsibility
- **Non-maleficence**: Do no harm

### Conscious Design
- Reflective reasoning on decisions
- Intent recognition and validation
- Context-aware operations
- Goal alignment verification

### Adaptive Self-Reflection
- Performance monitoring
- Behavior analysis
- Strategy adaptation
- Knowledge consolidation

## Need Help?

Open an issue on GitHub or check the documentation in the `docs/` directory.
