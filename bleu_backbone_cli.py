#!/usr/bin/env python3
"""
BLEU BACKBONE CLI
Command-line interface for managing BLEU Backbone Full Reports
"""

import argparse
import sys
from bleu_backbone import BleuBackbone, Product


def create_report(args):
    """Create a new BLEU Backbone report"""
    report = BleuBackbone(treasurer=args.treasurer)
    report.save_to_file(args.output, format=args.format)
    print(f"✓ Created BLEU Backbone report: {args.output}")
    print(f"  Total products: {report.report_metadata['total_products']}")
    print(f"  Average ROI: {report.report_metadata['total_roi_average']:.1f}%")
    print(f"  Total Overscale: ${report.report_metadata['total_overscale_billions']:.0f}B")


def show_report(args):
    """Show report details"""
    report = BleuBackbone.load_from_file(args.report)
    
    if args.verbose:
        print(report.generate_summary_table())
    else:
        print(report)
        print()
        print(f"Treasurer: {report.treasurer}")
        print(f"Timestamp: {report.timestamp}")
        print(f"Total Products: {report.report_metadata['total_products']}")
        print(f"Average ROI: {report.report_metadata['total_roi_average']:.1f}%")
        print(f"Total Overscale: ${report.report_metadata['total_overscale_billions']:.0f}B")


def show_sector(args):
    """Show products in a specific sector"""
    report = BleuBackbone.load_from_file(args.report)
    
    try:
        products = report.get_sector_products(args.sector)
        metrics = report.calculate_sector_metrics(args.sector)
        
        print(f"=" * 80)
        print(f"SECTOR: {args.sector.replace('_', ' ').title()}")
        print(f"=" * 80)
        print(f"Product Count: {metrics['product_count']}")
        print(f"Average ROI: {metrics['average_roi']:.1f}%")
        print(f"Total Overscale: ${metrics['total_overscale']:.0f}B")
        print(f"ROI Range: {metrics['min_roi']:.0f}% - {metrics['max_roi']:.0f}%")
        print()
        
        if products:
            print(f"{'Product':<35} {'Signal':<40} {'Use-case':<25} {'ROI %':>8} {'Overscale':>10}")
            print("-" * 120)
            for product in products:
                print(
                    f"{product.name:<35} {product.signal:<40} {product.use_case:<25} "
                    f"{product.roi_percent:>7.0f}% ${product.overscale_billions:>8.0f}B"
                )
        else:
            print("No products in this sector.")
    
    except ValueError as e:
        print(f"✗ Error: {e}")
        return 1


def add_product(args):
    """Add a product to a sector"""
    report = BleuBackbone.load_from_file(args.report)
    
    product = Product(
        name=args.name,
        signal=args.signal,
        use_case=args.use_case,
        roi_percent=args.roi,
        overscale_billions=args.overscale
    )
    
    try:
        report.add_product(args.sector, product)
        report.save_to_file(args.report, format=args.format)
        print(f"✓ Added product '{args.name}' to sector '{args.sector}'")
        print(f"  Total products: {report.report_metadata['total_products']}")
    except ValueError as e:
        print(f"✗ Error: {e}")
        return 1


def top_products(args):
    """Show top products by metric"""
    report = BleuBackbone.load_from_file(args.report)
    
    if args.metric == "roi":
        products = report.get_top_products_by_roi(args.limit)
        title = f"TOP {args.limit} PRODUCTS BY ROI"
    else:
        products = report.get_top_products_by_overscale(args.limit)
        title = f"TOP {args.limit} PRODUCTS BY OVERSCALE"
    
    print("=" * 120)
    print(title)
    print("=" * 120)
    print(f"{'#':<4} {'Product':<35} {'Signal':<40} {'Use-case':<25} {'ROI %':>8} {'Overscale':>10}")
    print("-" * 120)
    
    for i, product in enumerate(products, 1):
        print(
            f"{i:<4} {product.name:<35} {product.signal:<40} {product.use_case:<25} "
            f"{product.roi_percent:>7.0f}% ${product.overscale_billions:>8.0f}B"
        )


def export_report(args):
    """Export report to a different format"""
    report = BleuBackbone.load_from_file(args.report)
    report.save_to_file(args.output, format=args.format)
    print(f"✓ Exported report to {args.output} in {args.format.upper()} format")


def main():
    parser = argparse.ArgumentParser(
        description="BLEU BACKBONE CLI - Manage ceremonial economic infrastructure reports",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new report')
    create_parser.add_argument('-o', '--output', required=True, help='Output file path')
    create_parser.add_argument('-t', '--treasurer', default='Commander Bleu', help='Treasurer name')
    create_parser.add_argument('-f', '--format', choices=['yaml', 'json'], default='yaml', help='Output format')
    create_parser.set_defaults(func=create_report)
    
    # Show command
    show_parser = subparsers.add_parser('show', help='Show report details')
    show_parser.add_argument('report', help='Report file path')
    show_parser.add_argument('-v', '--verbose', action='store_true', help='Show full report details')
    show_parser.set_defaults(func=show_report)
    
    # Show sector command
    sector_parser = subparsers.add_parser('show-sector', help='Show products in a specific sector')
    sector_parser.add_argument('report', help='Report file path')
    sector_parser.add_argument('-s', '--sector', required=True, 
                               choices=[
                                   'healing_medicine_biology',
                                   'energy_agriculture_planet',
                                   'defense_military_security',
                                   'memory_legacy_knowledge',
                                   'travel_expansion_mobility',
                                   'education_justice',
                                   'culture_sports_influence',
                                   'economy_commerce_finance'
                               ],
                               help='Sector name')
    sector_parser.set_defaults(func=show_sector)
    
    # Add product command
    add_parser = subparsers.add_parser('add-product', help='Add a product to a sector')
    add_parser.add_argument('report', help='Report file path')
    add_parser.add_argument('-s', '--sector', required=True,
                            choices=[
                                'healing_medicine_biology',
                                'energy_agriculture_planet',
                                'defense_military_security',
                                'memory_legacy_knowledge',
                                'travel_expansion_mobility',
                                'education_justice',
                                'culture_sports_influence',
                                'economy_commerce_finance'
                            ],
                            help='Sector name')
    add_parser.add_argument('-n', '--name', required=True, help='Product name')
    add_parser.add_argument('-g', '--signal', required=True, help='Product signal/tagline')
    add_parser.add_argument('-u', '--use-case', required=True, help='Product use case')
    add_parser.add_argument('-r', '--roi', type=float, required=True, help='ROI percentage')
    add_parser.add_argument('-o', '--overscale', type=float, required=True, help='Overscale value in billions')
    add_parser.add_argument('-f', '--format', choices=['yaml', 'json'], default='yaml', help='Output format')
    add_parser.set_defaults(func=add_product)
    
    # Top products command
    top_parser = subparsers.add_parser('top', help='Show top products by metric')
    top_parser.add_argument('report', help='Report file path')
    top_parser.add_argument('-m', '--metric', choices=['roi', 'overscale'], default='roi', 
                           help='Metric to sort by')
    top_parser.add_argument('-l', '--limit', type=int, default=10, help='Number of products to show')
    top_parser.set_defaults(func=top_products)
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export report to a different format')
    export_parser.add_argument('report', help='Report file path')
    export_parser.add_argument('-o', '--output', required=True, help='Output file path')
    export_parser.add_argument('-f', '--format', choices=['yaml', 'json'], required=True, help='Output format')
    export_parser.set_defaults(func=export_report)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    try:
        result = args.func(args)
        return result if result is not None else 0
    except Exception as e:
        print(f"✗ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
