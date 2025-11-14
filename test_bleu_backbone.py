#!/usr/bin/env python3
"""
Test suite for the BLEU Backbone Full Report system

Run with: python test_bleu_backbone.py
"""

import os
import json
import tempfile
from bleu_backbone import BleuBackbone, Product


def test_product_creation():
    """Test product creation"""
    print("Testing product creation...")
    
    product = Product(
        "Test Product",
        "Test signal",
        "Test use case",
        150.0,
        500.0
    )
    
    assert product.name == "Test Product"
    assert product.signal == "Test signal"
    assert product.use_case == "Test use case"
    assert product.roi_percent == 150.0
    assert product.overscale_billions == 500.0
    
    # Test to_dict
    product_dict = product.to_dict()
    assert product_dict["name"] == "Test Product"
    assert product_dict["roi_percent"] == 150.0
    
    print("✓ Product creation tests passed")


def test_report_creation():
    """Test report creation and initialization"""
    print("Testing report creation...")
    
    report = BleuBackbone()
    assert report.report_id == "BLEU-BACKBONE-FULL-REPORT"
    assert report.treasurer == "Commander Bleu"
    assert report.version == "1.0.0"
    assert report.report_metadata["total_sectors"] == 8
    assert report.report_metadata["vault_sync"] is True
    assert report.report_metadata["ceremonial_status"] == "Active"
    
    # Check that default products were loaded
    assert report.report_metadata["total_products"] == 28
    assert len(report.healing_medicine_biology) == 6
    assert len(report.energy_agriculture_planet) == 5
    assert len(report.defense_military_security) == 3
    assert len(report.memory_legacy_knowledge) == 4
    assert len(report.travel_expansion_mobility) == 4
    assert len(report.education_justice) == 3
    assert len(report.culture_sports_influence) == 2
    assert len(report.economy_commerce_finance) == 1
    
    print("✓ Report creation tests passed")


def test_default_products():
    """Test that all default products are correctly loaded"""
    print("Testing default products...")
    
    report = BleuBackbone()
    
    # Test healing products
    healing_names = [p.name for p in report.healing_medicine_biology]
    assert "CryoLife Vaultlets" in healing_names
    assert "Soul Recode Pods" in healing_names
    assert "NanoHeal Clouds" in healing_names
    assert "Immortality Credits" in healing_names
    assert "SkyyBleu Serums" in healing_names
    assert "Quantum Detox Chambers" in healing_names
    
    # Test energy products
    energy_names = [p.name for p in report.energy_agriculture_planet]
    assert "Ziphonate Cores" in energy_names
    assert "PlasmaPearl Reactors" in energy_names
    assert "HeavenGold Bonds" in energy_names
    assert "InfinityLoop Vaultlets" in energy_names
    assert "HydroDome Farms" in energy_names
    
    # Test defense products
    defense_names = [p.name for p in report.defense_military_security]
    assert "Codex Authority Badges" in defense_names
    assert "PhaseWalk Cannons" in defense_names
    assert "MirrorGuard Shields" in defense_names
    
    # Test memory products
    memory_names = [p.name for p in report.memory_legacy_knowledge]
    assert "Ancestral Engrams" in memory_names
    assert "Eternal Archive Nodes" in memory_names
    assert "Lineage Bridges" in memory_names
    assert "History Rewrite Modules" in memory_names
    
    # Test travel products
    travel_names = [p.name for p in report.travel_expansion_mobility]
    assert "Portal Key Tokens" in travel_names
    assert "WarpJump Engines" in travel_names
    assert "HoverLane 8 Pods" in travel_names
    assert "BLEUFleet Outposts" in travel_names
    
    # Test education products
    education_names = [p.name for p in report.education_justice]
    assert "MetaCurriculum Pods" in education_names
    assert "Combat Academies" in education_names
    assert "BLEUJustice Domes" in education_names
    
    # Test culture products
    culture_names = [p.name for p in report.culture_sports_influence]
    assert "HoloConcert Domes" in culture_names
    assert "BLEU SportsVerse Arenas" in culture_names
    
    # Test economy products
    economy_names = [p.name for p in report.economy_commerce_finance]
    assert "SmartAd Beacons" in economy_names
    
    print("✓ Default products tests passed")


def test_add_product():
    """Test adding products to sectors"""
    print("Testing product addition...")
    
    report = BleuBackbone()
    initial_count = report.report_metadata["total_products"]
    
    # Add a new product
    new_product = Product(
        "Test Innovation",
        "Revolutionary tech",
        "Testing",
        175.0,
        600.0
    )
    
    report.add_product("healing_medicine_biology", new_product)
    
    assert report.report_metadata["total_products"] == initial_count + 1
    assert len(report.healing_medicine_biology) == 7
    assert report.healing_medicine_biology[-1].name == "Test Innovation"
    
    # Test invalid sector
    try:
        report.add_product("invalid_sector", new_product)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Invalid sector" in str(e)
    
    print("✓ Product addition tests passed")


def test_get_all_products():
    """Test getting all products"""
    print("Testing get all products...")
    
    report = BleuBackbone()
    all_products = report.get_all_products()
    
    assert len(all_products) == 28
    assert all(isinstance(p, Product) for p in all_products)
    
    print("✓ Get all products tests passed")


def test_get_sector_products():
    """Test getting products from specific sectors"""
    print("Testing get sector products...")
    
    report = BleuBackbone()
    
    healing_products = report.get_sector_products("healing_medicine_biology")
    assert len(healing_products) == 6
    
    energy_products = report.get_sector_products("energy_agriculture_planet")
    assert len(energy_products) == 5
    
    # Test invalid sector
    try:
        report.get_sector_products("invalid_sector")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
    
    print("✓ Get sector products tests passed")


def test_sector_metrics():
    """Test sector metrics calculation"""
    print("Testing sector metrics...")
    
    report = BleuBackbone()
    
    healing_metrics = report.calculate_sector_metrics("healing_medicine_biology")
    assert healing_metrics["sector"] == "healing_medicine_biology"
    assert healing_metrics["product_count"] == 6
    assert healing_metrics["average_roi"] > 0
    assert healing_metrics["total_overscale"] > 0
    assert healing_metrics["min_roi"] > 0
    assert healing_metrics["max_roi"] > healing_metrics["min_roi"]
    
    # Test specific values for healing sector
    # Products: CryoLife (176%), Soul Recode (184%), NanoHeal (184%), 
    #           Immortality (204%), SkyyBleu (194%), Quantum Detox (206%)
    expected_avg = (176 + 184 + 184 + 204 + 194 + 206) / 6
    assert abs(healing_metrics["average_roi"] - expected_avg) < 0.01
    
    print("✓ Sector metrics tests passed")


def test_top_products():
    """Test getting top products by various metrics"""
    print("Testing top products...")
    
    report = BleuBackbone()
    
    # Test top by ROI
    top_roi = report.get_top_products_by_roi(5)
    assert len(top_roi) == 5
    assert top_roi[0].roi_percent >= top_roi[1].roi_percent
    assert top_roi[1].roi_percent >= top_roi[2].roi_percent
    
    # Highest ROI should be BLEU SportsVerse Arenas at 248%
    assert top_roi[0].name == "BLEU SportsVerse Arenas"
    assert top_roi[0].roi_percent == 248.0
    
    # Test top by overscale
    top_overscale = report.get_top_products_by_overscale(5)
    assert len(top_overscale) == 5
    assert top_overscale[0].overscale_billions >= top_overscale[1].overscale_billions
    
    # Highest overscale should be Ziphonate Cores at $1200B
    assert top_overscale[0].name == "Ziphonate Cores"
    assert top_overscale[0].overscale_billions == 1200.0
    
    print("✓ Top products tests passed")


def test_metrics_update():
    """Test that metrics update correctly"""
    print("Testing metrics update...")
    
    report = BleuBackbone()
    
    initial_avg_roi = report.report_metadata["total_roi_average"]
    initial_overscale = report.report_metadata["total_overscale_billions"]
    
    # Add a high-ROI product
    high_roi_product = Product("Super Product", "Amazing", "Testing", 300.0, 100.0)
    report.add_product("healing_medicine_biology", high_roi_product)
    
    # Metrics should have updated
    assert report.report_metadata["total_roi_average"] > initial_avg_roi
    assert report.report_metadata["total_overscale_billions"] > initial_overscale
    
    print("✓ Metrics update tests passed")


def test_audit_hash():
    """Test audit hash generation and validation"""
    print("Testing audit hash...")
    
    report = BleuBackbone()
    
    # Check hash exists and is correct length
    audit_hash = report.report_metadata["audit_hash"]
    assert len(audit_hash) == 64  # SHA3-256
    
    # Add a product and verify hash changes
    old_hash = audit_hash
    new_product = Product("Test", "Test", "Test", 100.0, 100.0)
    report.add_product("healing_medicine_biology", new_product)
    new_hash = report.report_metadata["audit_hash"]
    assert old_hash != new_hash
    
    print("✓ Audit hash tests passed")


def test_yaml_export():
    """Test YAML export"""
    print("Testing YAML export...")
    
    report = BleuBackbone()
    yaml_str = report.to_yaml()
    
    assert "report_id: BLEU-BACKBONE-FULL-REPORT" in yaml_str
    assert "CryoLife Vaultlets" in yaml_str
    assert "Ziphonate Cores" in yaml_str
    assert "healing_medicine_biology" in yaml_str
    
    print("✓ YAML export tests passed")


def test_json_export():
    """Test JSON export"""
    print("Testing JSON export...")
    
    report = BleuBackbone()
    json_str = report.to_json()
    data = json.loads(json_str)
    
    assert data["report_id"] == "BLEU-BACKBONE-FULL-REPORT"
    assert len(data["sectors"]["healing_medicine_biology"]) == 6
    assert len(data["sectors"]["energy_agriculture_planet"]) == 5
    assert data["report_metadata"]["total_products"] == 28
    
    print("✓ JSON export tests passed")


def test_file_operations():
    """Test saving and loading from files"""
    print("Testing file operations...")
    
    # Create report
    report = BleuBackbone()
    
    # Save to temporary files
    with tempfile.TemporaryDirectory() as tmpdir:
        yaml_file = os.path.join(tmpdir, "test_report.yaml")
        json_file = os.path.join(tmpdir, "test_report.json")
        
        # Save
        report.save_to_file(yaml_file, format="yaml")
        report.save_to_file(json_file, format="json")
        
        # Load YAML
        loaded_yaml = BleuBackbone.load_from_file(yaml_file)
        assert loaded_yaml.report_id == report.report_id
        assert loaded_yaml.report_metadata["total_products"] == 28
        assert len(loaded_yaml.healing_medicine_biology) == 6
        
        # Load JSON
        loaded_json = BleuBackbone.load_from_file(json_file)
        assert loaded_json.report_id == report.report_id
        assert loaded_json.report_metadata["total_products"] == 28
        assert len(loaded_json.energy_agriculture_planet) == 5
    
    print("✓ File operations tests passed")


def test_round_trip():
    """Test round-trip conversion (save -> load -> save)"""
    print("Testing round-trip conversion...")
    
    # Create report with custom products
    report1 = BleuBackbone()
    
    # Add a custom product
    custom_product = Product(
        "Custom Innovation",
        "Next-gen tech",
        "Advanced testing",
        225.0,
        850.0
    )
    report1.add_product("travel_expansion_mobility", custom_product)
    
    # Convert to dict and back
    data = report1.to_dict()
    report2 = BleuBackbone.from_dict(data)
    
    # Verify
    assert report2.report_id == report1.report_id
    assert report2.report_metadata["total_products"] == report1.report_metadata["total_products"]
    assert len(report2.travel_expansion_mobility) == 5  # 4 default + 1 custom
    assert report2.travel_expansion_mobility[-1].name == "Custom Innovation"
    
    print("✓ Round-trip conversion tests passed")


def test_summary_table():
    """Test summary table generation"""
    print("Testing summary table generation...")
    
    report = BleuBackbone()
    summary = report.generate_summary_table()
    
    assert "BLEU BACKBONE FULL REPORT" in summary
    assert "Healing, Medicine & Biology" in summary
    assert "Energy, Agriculture & Planet Systems" in summary
    assert "CryoLife Vaultlets" in summary
    assert "Ziphonate Cores" in summary
    assert "Total Products: 28" in summary
    
    print("✓ Summary table tests passed")


def test_string_representation():
    """Test string representation"""
    print("Testing string representation...")
    
    report = BleuBackbone()
    str_repr = str(report)
    
    assert "BLEU Backbone" in str_repr
    assert "28 products" in str_repr
    assert "Avg ROI" in str_repr
    assert "Total Overscale" in str_repr
    
    print("✓ String representation tests passed")


def run_all_tests():
    """Run all tests"""
    print("=" * 100)
    print("🧪 BLEU BACKBONE TEST SUITE")
    print("=" * 100)
    print()
    
    tests = [
        test_product_creation,
        test_report_creation,
        test_default_products,
        test_add_product,
        test_get_all_products,
        test_get_sector_products,
        test_sector_metrics,
        test_top_products,
        test_metrics_update,
        test_audit_hash,
        test_yaml_export,
        test_json_export,
        test_file_operations,
        test_round_trip,
        test_summary_table,
        test_string_representation,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ Test failed: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ Test error: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
    
    print()
    print("=" * 100)
    print("TEST RESULTS")
    print("=" * 100)
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total:  {passed + failed}")
    print()
    
    if failed == 0:
        print("✨ All tests passed! The BLEU Backbone is fully operational. 🔵📊💎")
        return 0
    else:
        print(f"⚠ {failed} test(s) failed. Please review and fix.")
        return 1


if __name__ == "__main__":
    exit(run_all_tests())
