"""
Audit Logger - Secure audit trail and traceability
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import logging
import json


class AuditLogger:
    """
    Provides secure audit trail and traceability for all operations.
    
    Ensures complete transparency and accountability.
    """
    
    def __init__(self, log_file: Optional[str] = None):
        """
        Initialize Audit Logger.
        
        Args:
            log_file: Optional file path for persistent audit logs
        """
        self.logger = logging.getLogger(__name__)
        self.log_file = log_file
        self.audit_trail = []
        self.decision_log = []
        self.access_log = []
        
        if log_file:
            self._setup_file_logging()
    
    def log_operation(
        self,
        operation: str,
        actor: str,
        data_summary: str,
        context: Dict[str, Any],
        result: str
    ) -> None:
        """
        Log an operation to the audit trail.
        
        Args:
            operation: Operation performed
            actor: Who/what performed the operation
            data_summary: Summary of data involved
            context: Contextual information
            result: Result of the operation
        """
        entry = {
            'type': 'operation',
            'operation': operation,
            'actor': actor,
            'data_summary': data_summary,
            'context': context,
            'result': result,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        self.audit_trail.append(entry)
        self._persist_entry(entry)
    
    def log_decision(self, decision: Dict[str, Any]) -> None:
        """
        Log an ethical or operational decision.
        
        Args:
            decision: Decision details
        """
        entry = {
            'type': 'decision',
            'decision': decision,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        self.decision_log.append(entry)
        self.audit_trail.append(entry)
        self._persist_entry(entry)
    
    def log_access(
        self,
        resource: str,
        accessor: str,
        action: str,
        granted: bool
    ) -> None:
        """
        Log access to a resource.
        
        Args:
            resource: Resource being accessed
            accessor: Who is accessing
            action: Type of access
            granted: Whether access was granted
        """
        entry = {
            'type': 'access',
            'resource': resource,
            'accessor': accessor,
            'action': action,
            'granted': granted,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        self.access_log.append(entry)
        self.audit_trail.append(entry)
        self._persist_entry(entry)
    
    def log_event(
        self,
        event_type: str,
        description: str,
        details: Dict[str, Any]
    ) -> None:
        """
        Log a general event.
        
        Args:
            event_type: Type of event
            description: Event description
            details: Additional details
        """
        entry = {
            'type': 'event',
            'event_type': event_type,
            'description': description,
            'details': details,
            'timestamp': datetime.utcnow().isoformat()
        }
        
        self.audit_trail.append(entry)
        self._persist_entry(entry)
    
    def get_audit_trail(
        self,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        event_type: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve audit trail with optional filtering.
        
        Args:
            start_time: Optional start timestamp (ISO format)
            end_time: Optional end timestamp (ISO format)
            event_type: Optional event type filter
            
        Returns:
            Filtered audit trail entries
        """
        filtered = self.audit_trail
        
        if start_time:
            filtered = [e for e in filtered if e['timestamp'] >= start_time]
        
        if end_time:
            filtered = [e for e in filtered if e['timestamp'] <= end_time]
        
        if event_type:
            filtered = [e for e in filtered if e.get('type') == event_type]
        
        return filtered
    
    def get_compliance_report(self) -> Dict[str, Any]:
        """
        Generate compliance report from audit trail.
        
        Returns:
            Compliance report with statistics and summaries
        """
        total_operations = len([e for e in self.audit_trail if e['type'] == 'operation'])
        total_decisions = len(self.decision_log)
        total_accesses = len(self.access_log)
        
        denied_accesses = len([e for e in self.access_log if not e['granted']])
        
        return {
            'total_operations': total_operations,
            'total_decisions': total_decisions,
            'total_accesses': total_accesses,
            'denied_accesses': denied_accesses,
            'total_audit_entries': len(self.audit_trail),
            'audit_period': {
                'start': self.audit_trail[0]['timestamp'] if self.audit_trail else None,
                'end': self.audit_trail[-1]['timestamp'] if self.audit_trail else None
            }
        }
    
    def verify_integrity(self) -> Dict[str, Any]:
        """
        Verify integrity of audit trail.
        
        Returns:
            Integrity verification result
        """
        # Simple integrity check
        # In production, this would use cryptographic hashes
        
        is_complete = len(self.audit_trail) > 0
        is_chronological = self._verify_chronological_order()
        
        return {
            'is_complete': is_complete,
            'is_chronological': is_chronological,
            'total_entries': len(self.audit_trail),
            'integrity_verified': is_complete and is_chronological
        }
    
    def _setup_file_logging(self) -> None:
        """Setup file-based logging for persistence."""
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        )
        self.logger.addHandler(file_handler)
    
    def _persist_entry(self, entry: Dict[str, Any]) -> None:
        """Persist audit entry to file if configured."""
        if self.log_file:
            try:
                with open(self.log_file, 'a') as f:
                    f.write(json.dumps(entry) + '\n')
            except Exception as e:
                self.logger.error(f"Failed to persist audit entry: {e}")
    
    def _verify_chronological_order(self) -> bool:
        """Verify audit trail is in chronological order."""
        if len(self.audit_trail) < 2:
            return True
        
        for i in range(1, len(self.audit_trail)):
            if self.audit_trail[i]['timestamp'] < self.audit_trail[i-1]['timestamp']:
                return False
        
        return True
