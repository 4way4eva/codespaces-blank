#!/usr/bin/env python3
"""
BLEU BACKBONE EXAMPLE
Demonstration of the BLEU Backbone Full Report system
"""

from bleu_backbone import BleuBackbone, Product


def main():
    print("=" * 100)
    print("🔵 BLEU BACKBONE FULL REPORT™ - EXAMPLE DEMONSTRATION")
    print("=" * 100)
    print()
    
    # Example 1: Create a report with default products
    print("Example 1: Creating a new BLEU Backbone report")
    print("-" * 100)
    report = BleuBackbone(treasurer="Commander Bleu")
    print(f"✓ Created report: {report}")
    print(f"  Total Products: {report.report_metadata['total_products']}")
    print(f"  Average ROI: {report.report_metadata['total_roi_average']:.1f}%")
    print(f"  Total Overscale: ${report.report_metadata['total_overscale_billions']:.0f}B")
    print()
    
    # Example 2: Get products from a specific sector
    print("Example 2: Retrieving products from Energy sector")
    print("-" * 100)
    energy_products = report.get_sector_products("energy_agriculture_planet")
    for product in energy_products:
        print(f"  • {product}")
    print()
    
    # Example 3: Calculate sector metrics
    print("Example 3: Calculating sector metrics for Defense")
    print("-" * 100)
    defense_metrics = report.calculate_sector_metrics("defense_military_security")
    print(f"  Sector: {defense_metrics['sector']}")
    print(f"  Product Count: {defense_metrics['product_count']}")
    print(f"  Average ROI: {defense_metrics['average_roi']:.1f}%")
    print(f"  Total Overscale: ${defense_metrics['total_overscale']:.0f}B")
    print(f"  ROI Range: {defense_metrics['min_roi']:.0f}% - {defense_metrics['max_roi']:.0f}%")
    print()
    
    # Example 4: Get top products by ROI
    print("Example 4: Top 5 products by ROI")
    print("-" * 100)
    top_roi = report.get_top_products_by_roi(5)
    for i, product in enumerate(top_roi, 1):
        print(f"  {i}. {product.name} - {product.roi_percent}% ROI")
    print()
    
    # Example 5: Get top products by overscale value
    print("Example 5: Top 5 products by overscale value")
    print("-" * 100)
    top_overscale = report.get_top_products_by_overscale(5)
    for i, product in enumerate(top_overscale, 1):
        print(f"  {i}. {product.name} - ${product.overscale_billions:.0f}B")
    print()
    
    # Example 6: Add a new product
    print("Example 6: Adding a new product to the report")
    print("-" * 100)
    new_product = Product(
        name="QuantumLeap Bridges",
        signal="Teleport instantly. Anywhere.",
        use_case="Instant transportation",
        roi_percent=280.0,
        overscale_billions=950.0
    )
    report.add_product("travel_expansion_mobility", new_product)
    print(f"✓ Added product: {new_product.name}")
    print(f"  New total products: {report.report_metadata['total_products']}")
    print(f"  Updated average ROI: {report.report_metadata['total_roi_average']:.1f}%")
    print()
    
    # Example 7: Save to file
    print("Example 7: Saving report to files")
    print("-" * 100)
    report.save_to_file("/tmp/bleu_backbone_example.yaml", format="yaml")
    report.save_to_file("/tmp/bleu_backbone_example.json", format="json")
    print("✓ Saved report to:")
    print("  • /tmp/bleu_backbone_example.yaml")
    print("  • /tmp/bleu_backbone_example.json")
    print()
    
    # Example 8: Load from file
    print("Example 8: Loading report from file")
    print("-" * 100)
    loaded_report = BleuBackbone.load_from_file("/tmp/bleu_backbone_example.yaml")
    print(f"✓ Loaded report: {loaded_report}")
    print(f"  Products match: {loaded_report.report_metadata['total_products'] == report.report_metadata['total_products']}")
    print()
    
    # Example 9: Generate summary table
    print("Example 9: Generating full summary table")
    print("-" * 100)
    summary = report.generate_summary_table()
    print(summary)
    print()
    
    # Example 10: Working with multiple sectors
    print("Example 10: Analyzing all sectors")
    print("-" * 100)
    sectors = [
        "healing_medicine_biology",
        "energy_agriculture_planet",
        "defense_military_security",
        "memory_legacy_knowledge",
        "travel_expansion_mobility",
        "education_justice",
        "culture_sports_influence",
        "economy_commerce_finance"
    ]
    
    print(f"{'Sector':<40} {'Products':>10} {'Avg ROI':>12} {'Total Overscale':>18}")
    print("-" * 100)
    for sector in sectors:
        metrics = report.calculate_sector_metrics(sector)
        sector_name = sector.replace('_', ' ').title()
        print(
            f"{sector_name:<40} {metrics['product_count']:>10} "
            f"{metrics['average_roi']:>11.1f}% ${metrics['total_overscale']:>15.0f}B"
        )
    print()
    
    print("=" * 100)
    print("✨ BLEU Backbone demonstration complete! 🔵📊💎")
    print("=" * 100)


if __name__ == "__main__":
    main()
