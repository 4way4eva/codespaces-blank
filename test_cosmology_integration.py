#!/usr/bin/env python3
"""
Test suite for Biblical Cosmology and Investor Outreach Integration System.
"""

import unittest
import json
import os
import tempfile
from pathlib import Path
from cosmology_integration import (
    BiblicalCosmologySystem,
    InvestorOutreachSystem,
    IntegratedCodexSystem
)


class TestBiblicalCosmologySystem(unittest.TestCase):
    """Test cases for BiblicalCosmologySystem."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.system = BiblicalCosmologySystem("biblical_cosmology_codex.json")
    
    def test_load_codex(self):
        """Test that codex loads successfully."""
        self.assertIsNotNone(self.system.codex_data)
        self.assertIn("codex_id", self.system.codex_data)
        self.assertEqual(self.system.codex_data["codex_id"], "Biblical-Cosmology-Integration-v1.0")
    
    def test_get_realm_shamayim(self):
        """Test getting Shamayim realm."""
        realm = self.system.get_realm("shamayim")
        self.assertIsNotNone(realm)
        self.assertEqual(realm["name"], "Heavens")
        self.assertEqual(realm["device_mapping"], "EV0L Glass Systems sky layer")
    
    def test_get_realm_eretz(self):
        """Test getting Eretz realm."""
        realm = self.system.get_realm("eretz")
        self.assertIsNotNone(realm)
        self.assertEqual(realm["name"], "Earth")
        self.assertIn("SmartDomes", realm["device_mapping"])
    
    def test_get_realm_sheol(self):
        """Test getting Sheol realm."""
        realm = self.system.get_realm("sheol")
        self.assertIsNotNone(realm)
        self.assertEqual(realm["name"], "Underworld")
        self.assertIn("archival", realm["device_mapping"])
    
    def test_get_heaven_level_1(self):
        """Test getting first heaven (Vilon)."""
        heaven = self.system.get_heaven_level(1)
        self.assertIsNotNone(heaven)
        self.assertIn("Vilon", heaven["name"])
        self.assertIn("Curtain", heaven["name"])
    
    def test_get_heaven_level_7(self):
        """Test getting seventh heaven (Aravoth)."""
        heaven = self.system.get_heaven_level(7)
        self.assertIsNotNone(heaven)
        self.assertIn("Aravoth", heaven["name"])
        self.assertIn("throne", heaven["device_mapping"])
    
    def test_get_kabbalistic_world_atzilut(self):
        """Test getting Atzilut world."""
        world = self.system.get_kabbalistic_world("atzilut")
        self.assertIsNotNone(world)
        self.assertIn("Emanation", world["name"])
        self.assertIn("code", world["device_mapping"])
    
    def test_get_kabbalistic_world_asiyah(self):
        """Test getting Asiyah world."""
        world = self.system.get_kabbalistic_world("asiyah")
        self.assertIsNotNone(world)
        self.assertIn("Action", world["name"])
        self.assertIn("hardware", world["device_mapping"])
    
    def test_get_soul_level_nefesh(self):
        """Test getting Nefesh soul level."""
        level = self.system.get_soul_level("nefesh")
        self.assertIsNotNone(level)
        self.assertEqual(level["name"], "Nefesh")
        self.assertIn("SmartSuit", level["device_mapping"])
    
    def test_get_soul_level_yechidah(self):
        """Test getting Yechidah soul level."""
        level = self.system.get_soul_level("yechidah")
        self.assertIsNotNone(level)
        self.assertEqual(level["name"], "Yechidah")
        self.assertIn("ES0IL", level["device_mapping"])
    
    def test_get_device_mappings(self):
        """Test getting all device mappings."""
        mappings = self.system.get_device_mappings()
        self.assertIsInstance(mappings, dict)
        self.assertGreater(len(mappings), 0)
        # Check specific mappings exist
        self.assertIn("shamayim", mappings)
        self.assertIn("Nefesh", mappings)
    
    def test_get_health_stacks(self):
        """Test getting health stacks."""
        stacks = self.system.get_health_stacks()
        self.assertIsInstance(stacks, dict)
        self.assertIn("bioresp", stacks)
        self.assertIn("bleuwallet", stacks)
        self.assertEqual(stacks["bioresp"]["status"], "LIVE")
    
    def test_get_system_status(self):
        """Test getting system status."""
        status = self.system.get_system_status()
        self.assertIn("status", status)
        self.assertEqual(status["status"], "LIVE_SYNCED_ACTIVE")
        self.assertIn("devices_count", status)
        self.assertEqual(status["devices_count"], EXPECTED_DEVICES_COUNT)
    
    def test_export_to_yaml(self):
        """Test YAML export."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            temp_file = f.name
        try:
            self.system.export_to_yaml(temp_file)
            self.assertTrue(os.path.exists(temp_file))
            self.assertGreater(os.path.getsize(temp_file), 0)
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
    
    def test_export_to_json(self):
        """Test JSON export."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name
        try:
            self.system.export_to_json(temp_file)
            self.assertTrue(os.path.exists(temp_file))
            with open(temp_file, 'r') as f:
                data = json.load(f)
            self.assertIn("codex_id", data)
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)


# Constants for testing
EXPECTED_TIER1_INVESTORS = 5
EXPECTED_DEVICES_COUNT = 7
EXPECTED_HEALTH_STACKS = ["bioresp", "bleuwallet", "delayed_cord_protocol", "cordai_sop", "prophetic_healing"]


class TestInvestorOutreachSystem(unittest.TestCase):
    """Test cases for InvestorOutreachSystem."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.system = InvestorOutreachSystem("investor_outreach_system.json")
    
    def test_load_outreach(self):
        """Test that outreach data loads successfully."""
        self.assertIsNotNone(self.system.outreach_data)
        self.assertIn("outreach_id", self.system.outreach_data)
        self.assertEqual(self.system.outreach_data["outreach_id"], "Investor-Outreach-System-v1.0")
    
    def test_get_investors(self):
        """Test getting tier 1 investors."""
        investors = self.system.get_investors("tier_1_mega_funds")
        self.assertIsInstance(investors, list)
        self.assertEqual(len(investors), EXPECTED_TIER1_INVESTORS)
        self.assertIn("name", investors[0])
    
    def test_get_investor_by_name_a16z(self):
        """Test finding a16z investor."""
        investor = self.system.get_investor_by_name("a16z")
        self.assertIsNotNone(investor)
        self.assertIn("Andreessen Horowitz", investor["name"])
        self.assertEqual(investor["stage"], "Pitch deck finalized")
    
    def test_get_investor_by_name_sequoia(self):
        """Test finding Sequoia investor."""
        investor = self.system.get_investor_by_name("Sequoia")
        self.assertIsNotNone(investor)
        self.assertIn("Sequoia", investor["name"])
        self.assertTrue(investor["qr_code_generated"])
    
    def test_get_pitch_deck_status(self):
        """Test getting pitch deck status."""
        pitch = self.system.get_pitch_deck_status()
        self.assertEqual(pitch["status"], "FINALIZED")
        self.assertIn("slides", pitch)
        self.assertEqual(len(pitch["slides"]), 10)
    
    def test_get_qr_codes(self):
        """Test getting QR codes."""
        qr_codes = self.system.get_qr_codes()
        self.assertIsInstance(qr_codes, list)
        self.assertEqual(len(qr_codes), EXPECTED_TIER1_INVESTORS)
        self.assertTrue(all(qr["tracking_enabled"] for qr in qr_codes))
    
    def test_get_tracking_links(self):
        """Test getting tracking links."""
        links = self.system.get_tracking_links()
        self.assertIsInstance(links, list)
        self.assertEqual(len(links), EXPECTED_TIER1_INVESTORS)
        for link in links:
            self.assertIn("tracking_params", link)
            self.assertIn("utm_source", link["tracking_params"])
    
    def test_get_role_assignment_evolynn(self):
        """Test getting Evolynn's role."""
        role = self.system.get_role_assignment("evolynn")
        self.assertIsNotNone(role)
        self.assertEqual(role["role"], "Primary Presenter")
        self.assertIn("responsibilities", role)
    
    def test_get_role_assignment_pihya(self):
        """Test getting Pihya's role."""
        role = self.system.get_role_assignment("pihya")
        self.assertIsNotNone(role)
        self.assertIn("Validator", role["role"])
        self.assertIn("responsibilities", role)
    
    def test_get_outreach_timeline(self):
        """Test getting outreach timeline."""
        timeline = self.system.get_outreach_timeline()
        self.assertIsInstance(timeline, dict)
        self.assertIn("phase_1_preparation", timeline)
        self.assertEqual(timeline["phase_1_preparation"]["status"], "COMPLETE")
    
    def test_get_current_phase(self):
        """Test getting current phase."""
        phase = self.system.get_current_phase()
        self.assertIsNotNone(phase)
        self.assertIsInstance(phase, dict)
    
    def test_get_success_metrics(self):
        """Test getting success metrics."""
        metrics = self.system.get_success_metrics()
        self.assertIn("response_rate_target", metrics)
        self.assertIn("investment_close_target", metrics)
    
    def test_get_integration_status(self):
        """Test getting integration status."""
        integration = self.system.get_integration_status()
        self.assertIn("health_stacks_backing", integration)
        self.assertEqual(integration["health_stacks_backing"]["bioresp"], "LIVE")
    
    def test_export_to_yaml(self):
        """Test YAML export."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            temp_file = f.name
        try:
            self.system.export_to_yaml(temp_file)
            self.assertTrue(os.path.exists(temp_file))
            self.assertGreater(os.path.getsize(temp_file), 0)
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
    
    def test_export_to_json(self):
        """Test JSON export."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name
        try:
            self.system.export_to_json(temp_file)
            self.assertTrue(os.path.exists(temp_file))
            with open(temp_file, 'r') as f:
                data = json.load(f)
            self.assertIn("outreach_id", data)
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)


class TestIntegratedCodexSystem(unittest.TestCase):
    """Test cases for IntegratedCodexSystem."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.system = IntegratedCodexSystem(
            "biblical_cosmology_codex.json",
            "investor_outreach_system.json"
        )
    
    def test_initialization(self):
        """Test system initialization."""
        self.assertIsNotNone(self.system.cosmology)
        self.assertIsNotNone(self.system.outreach)
    
    def test_get_full_system_status(self):
        """Test getting full system status."""
        status = self.system.get_full_system_status()
        self.assertIn("timestamp", status)
        self.assertIn("cosmology_system", status)
        self.assertIn("outreach_system", status)
        self.assertIn("integration", status)
        
        # Check cosmology system
        self.assertEqual(status["cosmology_system"]["status"], "LIVE_SYNCED_ACTIVE")
        
        # Check outreach system
        self.assertEqual(status["outreach_system"]["checklist_status"], "GREEN_LIT")
        
        # Check integration
        self.assertIn("health_stacks", status["integration"])
        self.assertIn("cosmology_integration", status["integration"])
    
    def test_generate_aws_deployment_package(self):
        """Test AWS deployment package generation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            files = self.system.generate_aws_deployment_package(temp_dir)
            
            self.assertIn("cosmology", files)
            self.assertIn("outreach", files)
            self.assertIn("status", files)
            
            # Verify files exist
            for filepath in files.values():
                self.assertTrue(os.path.exists(filepath))
                self.assertGreater(os.path.getsize(filepath), 0)
    
    def test_generate_github_deployment_package(self):
        """Test GitHub deployment package generation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            files = self.system.generate_github_deployment_package(temp_dir)
            
            self.assertIn("cosmology_yaml", files)
            self.assertIn("cosmology_json", files)
            self.assertIn("outreach_yaml", files)
            self.assertIn("outreach_json", files)
            
            # Verify files exist
            for filepath in files.values():
                self.assertTrue(os.path.exists(filepath))
                self.assertGreater(os.path.getsize(filepath), 0)
    
    def test_cosmology_access(self):
        """Test accessing cosmology through integrated system."""
        realm = self.system.cosmology.get_realm("shamayim")
        self.assertIsNotNone(realm)
        self.assertEqual(realm["name"], "Heavens")
    
    def test_outreach_access(self):
        """Test accessing outreach through integrated system."""
        investors = self.system.outreach.get_investors()
        self.assertEqual(len(investors), EXPECTED_TIER1_INVESTORS)


class TestSystemIntegration(unittest.TestCase):
    """Integration tests for the complete system."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.system = IntegratedCodexSystem()
    
    def test_cosmology_to_outreach_integration(self):
        """Test that cosmology and outreach systems are properly integrated."""
        # Get integration status from outreach
        integration = self.system.outreach.get_integration_status()
        
        # Verify cosmology integration
        cosmology_int = integration.get("cosmology_integration", {})
        self.assertEqual(cosmology_int.get("three_realms"), "MAPPED")
        self.assertEqual(cosmology_int.get("seven_heavens"), "DEPLOYED")
        self.assertEqual(cosmology_int.get("four_worlds"), "INTEGRATED")
        
        # Verify health stacks integration
        health_stacks = integration.get("health_stacks_backing", {})
        self.assertEqual(health_stacks.get("bioresp"), "LIVE")
        self.assertEqual(health_stacks.get("bleuwallet"), "SYNCED")
    
    def test_health_stacks_consistency(self):
        """Test that health stacks are consistent across systems."""
        # Get from cosmology
        cosmology_stacks = self.system.cosmology.get_health_stacks()
        
        # Get from outreach integration
        outreach_integration = self.system.outreach.get_integration_status()
        outreach_stacks = outreach_integration.get("health_stacks_backing", {})
        
        # Verify consistency
        for stack_name in EXPECTED_HEALTH_STACKS:
            self.assertIn(stack_name, cosmology_stacks)
            self.assertIn(stack_name, outreach_stacks)
            
            cosmology_status = cosmology_stacks[stack_name]["status"]
            outreach_status = outreach_stacks[stack_name]
            
            self.assertEqual(cosmology_status, outreach_status)
    
    def test_role_definitions_present(self):
        """Test that Evolynn and Pihya roles are properly defined."""
        evolynn = self.system.outreach.get_role_assignment("evolynn")
        pihya = self.system.outreach.get_role_assignment("pihya")
        
        self.assertIsNotNone(evolynn)
        self.assertIsNotNone(pihya)
        
        # Verify role distinction
        self.assertIn("Presenter", evolynn["role"])
        self.assertIn("Validator", pihya["role"])
    
    def test_all_investors_have_materials(self):
        """Test that all investors have complete materials."""
        investors = self.system.outreach.get_investors()
        qr_codes = self.system.outreach.get_qr_codes()
        tracking_links = self.system.outreach.get_tracking_links()
        
        # Verify counts match
        self.assertEqual(len(investors), len(qr_codes))
        self.assertEqual(len(investors), len(tracking_links))
        
        # Verify all investors have complete setup
        for investor in investors:
            self.assertTrue(investor["qr_code_generated"])
            self.assertTrue(investor["social_teaser_ready"])
            self.assertIn("tracking_link", investor)


def run_tests():
    """Run all tests."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestBiblicalCosmologySystem))
    suite.addTests(loader.loadTestsFromTestCase(TestInvestorOutreachSystem))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegratedCodexSystem))
    suite.addTests(loader.loadTestsFromTestCase(TestSystemIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    exit(run_tests())
