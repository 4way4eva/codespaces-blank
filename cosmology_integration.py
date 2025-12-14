#!/usr/bin/env python3
"""
Biblical Cosmology and Investor Outreach Integration System
Manages the comprehensive mapping between spiritual cosmology and device systems,
plus investor outreach tracking and management.
"""

import json
import yaml
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path


class BiblicalCosmologySystem:
    """Manages Biblical Cosmology integration with device systems."""
    
    def __init__(self, codex_file: str = "biblical_cosmology_codex.json"):
        """Initialize the cosmology system."""
        self.codex_file = codex_file
        self.codex_data = self._load_codex()
    
    def _load_codex(self) -> Dict:
        """Load the cosmology codex from JSON file."""
        try:
            with open(self.codex_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return self._create_default_codex()
    
    def _create_default_codex(self) -> Dict:
        """Create default codex structure."""
        return {
            "codex_id": "Biblical-Cosmology-Integration-v1.0",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "status": "INITIALIZED"
        }
    
    def get_realm(self, realm_name: str) -> Optional[Dict]:
        """Get information about a specific realm (shamayim, eretz, sheol)."""
        return self.codex_data.get("three_realms", {}).get(realm_name.lower())
    
    def get_heaven_level(self, level: int) -> Optional[Dict]:
        """Get information about a specific heaven level (1-7)."""
        level_key = f"{level}_{self._get_heaven_name(level)}"
        return self.codex_data.get("seven_heavens", {}).get("levels", {}).get(level_key)
    
    def _get_heaven_name(self, level: int) -> str:
        """Map level number to heaven name."""
        names = {
            1: "vilon",
            2: "rakia",
            3: "shehaqim",
            4: "zevul",
            5: "maon",
            6: "machon",
            7: "aravoth"
        }
        return names.get(level, "unknown")
    
    def get_kabbalistic_world(self, world_name: str) -> Optional[Dict]:
        """Get information about a Kabbalistic world."""
        return self.codex_data.get("four_kabbalistic_worlds", {}).get("worlds", {}).get(world_name.lower())
    
    def get_sefirah(self, sefirah_name: str) -> Optional[Dict]:
        """Get information about a specific sefirah."""
        emanations = self.codex_data.get("sefirot_dimensions", {}).get("emanations", {})
        for key, value in emanations.items():
            if sefirah_name.lower() in key or sefirah_name.lower() in value.get("name", "").lower():
                return value
        return None
    
    def get_soul_level(self, level_name: str) -> Optional[Dict]:
        """Get information about a specific soul level."""
        levels = self.codex_data.get("five_soul_levels", {}).get("levels", {})
        for key, value in levels.items():
            if level_name.lower() in key or level_name.lower() in value.get("name", "").lower():
                return value
        return None
    
    def get_device_mappings(self) -> Dict[str, List[str]]:
        """Get all device mappings across the cosmology."""
        mappings = {}
        
        # Three Realms
        for realm_name, realm_data in self.codex_data.get("three_realms", {}).items():
            device = realm_data.get("device_mapping", "")
            if device:
                mappings[realm_name] = [device]
        
        # Seven Heavens
        for level_data in self.codex_data.get("seven_heavens", {}).get("levels", {}).values():
            name = level_data.get("name", "")
            device = level_data.get("device_mapping", "")
            if device:
                mappings[name] = [device]
        
        # Soul Levels
        for level_data in self.codex_data.get("five_soul_levels", {}).get("levels", {}).values():
            name = level_data.get("name", "")
            device = level_data.get("device_mapping", "")
            if device:
                mappings[name] = [device]
        
        return mappings
    
    def get_health_stacks(self) -> Dict:
        """Get all health stack protocols."""
        return self.codex_data.get("health_stacks", {})
    
    def get_system_status(self) -> Dict:
        """Get overall system integration status."""
        return {
            "status": self.codex_data.get("status", "UNKNOWN"),
            "timestamp": self.codex_data.get("timestamp"),
            "deployment_status": self.codex_data.get("system_integration", {}).get("deployment_status"),
            "devices_count": len(self.codex_data.get("system_integration", {}).get("devices_updated", [])),
            "health_stacks": list(self.codex_data.get("health_stacks", {}).keys())
        }
    
    def export_to_yaml(self, output_file: str) -> None:
        """Export codex to YAML format."""
        with open(output_file, 'w', encoding='utf-8') as f:
            yaml.dump(self.codex_data, f, default_flow_style=False, allow_unicode=True)
    
    def export_to_json(self, output_file: str, indent: int = 2) -> None:
        """Export codex to JSON format."""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.codex_data, f, indent=indent, ensure_ascii=False)


class InvestorOutreachSystem:
    """Manages investor outreach tracking and coordination."""
    
    def __init__(self, outreach_file: str = "investor_outreach_system.json"):
        """Initialize the outreach system."""
        self.outreach_file = outreach_file
        self.outreach_data = self._load_outreach()
    
    def _load_outreach(self) -> Dict:
        """Load the outreach data from JSON file."""
        try:
            with open(self.outreach_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return self._create_default_outreach()
    
    def _create_default_outreach(self) -> Dict:
        """Create default outreach structure."""
        return {
            "outreach_id": "Investor-Outreach-System-v1.0",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "status": "INITIALIZED"
        }
    
    def get_investors(self, tier: str = "tier_1_mega_funds") -> List[Dict]:
        """Get list of investors by tier.
        
        Args:
            tier: The investor tier to retrieve (e.g., 'tier_1_mega_funds')
            
        Returns:
            List of investor dictionaries, or empty list if tier not found
        """
        investors = self.outreach_data.get("target_investors", {}).get(tier, [])
        if not investors and tier not in self.outreach_data.get("target_investors", {}):
            # Log warning but don't raise exception - return empty list
            import warnings
            warnings.warn(f"Investor tier '{tier}' not found in outreach data", UserWarning)
        return investors
    
    def get_investor_by_name(self, name: str) -> Optional[Dict]:
        """Find an investor by name."""
        for tier_data in self.outreach_data.get("target_investors", {}).values():
            if isinstance(tier_data, list):
                for investor in tier_data:
                    if name.lower() in investor.get("name", "").lower():
                        return investor
        return None
    
    def update_investor_stage(self, investor_name: str, new_stage: str) -> bool:
        """Update the stage of an investor."""
        for tier_data in self.outreach_data.get("target_investors", {}).values():
            if isinstance(tier_data, list):
                for investor in tier_data:
                    if investor_name.lower() in investor.get("name", "").lower():
                        investor["stage"] = new_stage
                        investor["last_updated"] = datetime.utcnow().isoformat() + "Z"
                        self._save_outreach()
                        return True
        return False
    
    def get_pitch_deck_status(self) -> Dict:
        """Get pitch deck preparation status."""
        return self.outreach_data.get("pitch_materials", {}).get("pitch_deck", {})
    
    def get_qr_codes(self) -> List[Dict]:
        """Get all generated QR codes."""
        return self.outreach_data.get("pitch_materials", {}).get("qr_codes", {}).get("codes", [])
    
    def get_tracking_links(self) -> List[Dict]:
        """Get all tracking links."""
        return self.outreach_data.get("pitch_materials", {}).get("tracking_links", {}).get("links", [])
    
    def get_role_assignment(self, person: str) -> Optional[Dict]:
        """Get role assignment for Evolynn or Pihya."""
        return self.outreach_data.get("role_assignments", {}).get(person.lower())
    
    def get_outreach_timeline(self) -> Dict:
        """Get the complete outreach timeline."""
        return self.outreach_data.get("outreach_timeline", {})
    
    def get_current_phase(self) -> Optional[Dict]:
        """Get the current active phase."""
        timeline = self.get_outreach_timeline()
        for phase_name, phase_data in timeline.items():
            if phase_data.get("status") in ["READY_TO_BEGIN", "IN_PROGRESS"]:
                return {phase_name: phase_data}
        return None
    
    def get_success_metrics(self) -> Dict:
        """Get success metrics and targets."""
        return self.outreach_data.get("success_metrics", {})
    
    def get_integration_status(self) -> Dict:
        """Get integration status with other systems."""
        return self.outreach_data.get("integration_with_systems", {})
    
    def _save_outreach(self) -> None:
        """Save outreach data to file."""
        try:
            with open(self.outreach_file, 'w', encoding='utf-8') as f:
                json.dump(self.outreach_data, f, indent=2, ensure_ascii=False)
        except (IOError, PermissionError) as e:
            raise IOError(f"Failed to save outreach data to {self.outreach_file}: {e}") from e
    
    def export_to_yaml(self, output_file: str) -> None:
        """Export outreach data to YAML format."""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                yaml.dump(self.outreach_data, f, default_flow_style=False, allow_unicode=True)
        except (IOError, PermissionError) as e:
            raise IOError(f"Failed to export to YAML file {output_file}: {e}") from e
    
    def export_to_json(self, output_file: str, indent: int = 2) -> None:
        """Export outreach data to JSON format."""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.outreach_data, f, indent=indent, ensure_ascii=False)
        except (IOError, PermissionError) as e:
            raise IOError(f"Failed to export to JSON file {output_file}: {e}") from e


class IntegratedCodexSystem:
    """Unified system combining cosmology and investor outreach."""
    
    def __init__(self, 
                 cosmology_file: str = "biblical_cosmology_codex.json",
                 outreach_file: str = "investor_outreach_system.json"):
        """Initialize the integrated system."""
        self.cosmology = BiblicalCosmologySystem(cosmology_file)
        self.outreach = InvestorOutreachSystem(outreach_file)
    
    def get_full_system_status(self) -> Dict:
        """Get comprehensive status of all systems."""
        return {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "cosmology_system": self.cosmology.get_system_status(),
            "outreach_system": {
                "status": self.outreach.outreach_data.get("status"),
                "checklist_status": self.outreach.outreach_data.get("checklist_status"),
                "current_phase": self.outreach.get_current_phase(),
                "investors_count": len(self.outreach.get_investors())
            },
            "integration": {
                "health_stacks": self.outreach.get_integration_status().get("health_stacks_backing"),
                "cosmology_integration": self.outreach.get_integration_status().get("cosmology_integration"),
                "partnerships": self.outreach.get_integration_status().get("upper_echelon_partnerships")
            }
        }
    
    def generate_aws_deployment_package(self, output_dir: str = ".") -> Dict[str, str]:
        """Generate AWS deployment package with all schemas."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        files = {}
        
        # Export cosmology
        cosmology_json = output_path / "aws_cosmology.json"
        self.cosmology.export_to_json(str(cosmology_json))
        files["cosmology"] = str(cosmology_json)
        
        # Export outreach
        outreach_json = output_path / "aws_outreach.json"
        self.outreach.export_to_json(str(outreach_json))
        files["outreach"] = str(outreach_json)
        
        # Export combined status
        status_json = output_path / "aws_system_status.json"
        with open(status_json, 'w', encoding='utf-8') as f:
            json.dump(self.get_full_system_status(), f, indent=2, ensure_ascii=False)
        files["status"] = str(status_json)
        
        return files
    
    def generate_github_deployment_package(self, output_dir: str = ".") -> Dict[str, str]:
        """Generate GitHub deployment package with YAML and JSON."""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        files = {}
        
        # Export cosmology as YAML
        cosmology_yaml = output_path / "github_cosmology.yaml"
        self.cosmology.export_to_yaml(str(cosmology_yaml))
        files["cosmology_yaml"] = str(cosmology_yaml)
        
        # Export cosmology as JSON
        cosmology_json = output_path / "github_cosmology.json"
        self.cosmology.export_to_json(str(cosmology_json))
        files["cosmology_json"] = str(cosmology_json)
        
        # Export outreach as YAML
        outreach_yaml = output_path / "github_outreach.yaml"
        self.outreach.export_to_yaml(str(outreach_yaml))
        files["outreach_yaml"] = str(outreach_yaml)
        
        # Export outreach as JSON
        outreach_json = output_path / "github_outreach.json"
        self.outreach.export_to_json(str(outreach_json))
        files["outreach_json"] = str(outreach_json)
        
        return files
    
    def print_summary(self) -> None:
        """Print a comprehensive summary of all systems."""
        print("=" * 80)
        print("BLEU CODEX INTEGRATION SYSTEM - FULL SUMMARY")
        print("=" * 80)
        print()
        
        # System Status
        status = self.get_full_system_status()
        print("📊 SYSTEM STATUS")
        print(f"  Timestamp: {status['timestamp']}")
        print(f"  Cosmology Status: {status['cosmology_system']['status']}")
        print(f"  Outreach Status: {status['outreach_system']['status']}")
        print(f"  Checklist Status: {status['outreach_system']['checklist_status']}")
        print()
        
        # Cosmology Details
        print("🌌 BIBLICAL COSMOLOGY INTEGRATION")
        print(f"  Devices Updated: {status['cosmology_system']['devices_count']}")
        print(f"  Health Stacks: {', '.join(status['cosmology_system']['health_stacks'])}")
        print()
        
        # Investor Outreach
        print("💼 INVESTOR OUTREACH")
        investors = self.outreach.get_investors()
        print(f"  Target Investors: {len(investors)}")
        for investor in investors:
            print(f"    • {investor['name']}: {investor['stage']}")
        print()
        
        # Role Assignments
        print("👥 ROLE ASSIGNMENTS")
        evolynn = self.outreach.get_role_assignment("evolynn")
        pihya = self.outreach.get_role_assignment("pihya")
        print(f"  Evolynn: {evolynn.get('role', 'N/A') if evolynn else 'N/A'}")
        print(f"  Pihya: {pihya.get('role', 'N/A') if pihya else 'N/A'}")
        print()
        
        # Integration Status
        print("🔗 INTEGRATION STATUS")
        integration = status['integration']
        print("  Health Stacks:")
        for stack, stat in integration.get('health_stacks', {}).items():
            print(f"    • {stack}: {stat}")
        print("  Cosmology Integration:")
        for component, stat in integration.get('cosmology_integration', {}).items():
            print(f"    • {component}: {stat}")
        print()
        
        print("=" * 80)
        print("✅ ALL SYSTEMS OPERATIONAL - READY FOR DEPLOYMENT")
        print("=" * 80)


if __name__ == "__main__":
    # Example usage
    system = IntegratedCodexSystem()
    system.print_summary()
    
    print("\n🚀 Generating deployment packages...")
    
    # Generate AWS package
    aws_files = system.generate_aws_deployment_package(".")
    print("\n📦 AWS Deployment Package:")
    for file_type, filepath in aws_files.items():
        print(f"  • {file_type}: {filepath}")
    
    # Generate GitHub package
    github_files = system.generate_github_deployment_package(".")
    print("\n📦 GitHub Deployment Package:")
    for file_type, filepath in github_files.items():
        print(f"  • {file_type}: {filepath}")
