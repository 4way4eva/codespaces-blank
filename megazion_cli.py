#!/usr/bin/env python3
"""
CLI Interface for the MEGAZION INHERITANCE LEDGER™

Commands:
- create: Create a new MEGAZION ledger
- show: Display the ledger contents
- add-blessing: Add a healing blessing
- add-gem: Add a gem/element
- add-supernatural: Add a supernatural surprise
- add-ingredient: Add an ingredient root
- add-job: Add a job/career
- add-loop: Add a surprise loop
- verify: Verify loop integrity
- export: Export ledger to file
- yields: Show blessing yields
"""

import argparse
import sys
from megazion_ledger import (
    MegazionLedger, HealingBlessing, GemElement, 
    SupernaturalSurprise, IngredientRoot, JobCareer, SurpriseLoop
)


def create_ledger(args):
    """Create a new MEGAZION ledger"""
    ledger = MegazionLedger(treasurer=args.treasurer)
    
    if args.output:
        ledger.save_to_file(args.output, format=args.format)
        print(f"✓ MEGAZION Ledger created and saved to {args.output}")
    else:
        print(ledger.to_yaml() if args.format == 'yaml' else ledger.to_json())
    
    return ledger


def show_ledger(args):
    """Display the ledger"""
    try:
        ledger = MegazionLedger.load_from_file(args.ledger)
    except FileNotFoundError:
        print(f"✗ Error: Ledger file not found: {args.ledger}")
        sys.exit(1)
    
    print("=" * 80)
    print("🔵 MEGAZION INHERITANCE LEDGER™")
    print("=" * 80)
    print()
    print(f"Ledger ID: {ledger.ledger_id}")
    print(f"Timestamp: {ledger.timestamp}")
    print(f"Treasurer: {ledger.treasurer}")
    print(f"Version: {ledger.version}")
    print()
    
    yields = ledger.calculate_blessing_yield()
    print("BLESSING YIELDS:")
    print(f"  Healing Blessings: {yields['total_healing_blessings']}")
    print(f"  Gems & Elements: {yields['total_gems_elements']}")
    print(f"  Supernatural Surprises: {yields['total_supernatural_surprises']}")
    print(f"  Ingredient Roots: {yields['total_ingredient_roots']}")
    print(f"  Job Careers: {yields['total_job_careers']}")
    print(f"  Active Loops: {yields['total_surprise_loops']}")
    print(f"  Active Industries: {yields['active_industries']}")
    print(f"  Spawned Schools: {yields['spawned_schools']}")
    print()
    
    print(f"Loop Integrity: {'✓ VERIFIED' if ledger.verify_loop_integrity() else '✗ FAILED'}")
    print(f"Audit Hash: {ledger.exchange_logic['audit_hash'][:32]}...")
    print()
    
    if args.verbose:
        print("=" * 80)
        if args.section == "all" or args.section == "healing":
            print("HEALING BLESSINGS:")
            print("=" * 80)
            for i, blessing in enumerate(ledger.healing_blessings, 1):
                print(f"\n{i}. {blessing.disease}")
                print(f"   Cure: {blessing.cure}")
                print(f"   Industry: {blessing.industry}")
                print(f"   Loop Category: {blessing.loop_category}")
                print(f"   Job Sectors: {', '.join(blessing.job_sectors)}")
                print(f"   Schools: {', '.join(blessing.schools_spawned)}")
        
        if args.section == "all" or args.section == "gems":
            print("\n" + "=" * 80)
            print("GEMS & ELEMENTS:")
            print("=" * 80)
            for i, gem in enumerate(ledger.gems_elements, 1):
                print(f"\n{i}. {gem.name}")
                print(f"   Property: {gem.property}")
                print(f"   Sector: {gem.sector}")
                print(f"   Loop Type: {gem.loop_type}")
                print(f"   Applications: {', '.join(gem.applications)}")
        
        if args.section == "all" or args.section == "supernatural":
            print("\n" + "=" * 80)
            print("SUPERNATURAL SURPRISES:")
            print("=" * 80)
            for i, surprise in enumerate(ledger.supernatural_surprises, 1):
                print(f"\n{i}. {surprise.name}")
                print(f"   Category: {surprise.category}")
                print(f"   Economic Sector: {surprise.economic_sector}")
                print(f"   Protocols: {', '.join(surprise.protocols)}")
        
        if args.section == "all" or args.section == "ingredients":
            print("\n" + "=" * 80)
            print("INGREDIENT ROOTS:")
            print("=" * 80)
            for i, root in enumerate(ledger.ingredient_roots, 1):
                print(f"\n{i}. {root.ingredient}")
                print(f"   Source: {root.source}")
                print(f"   Industries: {', '.join(root.industries)}")
                print(f"   Trade Empires: {', '.join(root.trade_empires)}")
        
        if args.section == "all" or args.section == "jobs":
            print("\n" + "=" * 80)
            print("JOB CAREERS:")
            print("=" * 80)
            for i, job in enumerate(ledger.job_careers, 1):
                print(f"\n{i}. {job.title}")
                print(f"   Blessing Source: {job.blessing_source}")
                print(f"   Industry: {job.industry}")
                print(f"   Spawned Jobs: {', '.join(job.spawned_jobs)}")
                print(f"   Training Schools: {', '.join(job.training_schools)}")
        
        if args.section == "all" or args.section == "loops":
            print("\n" + "=" * 80)
            print("SURPRISE LOOPS:")
            print("=" * 80)
            for i, loop in enumerate(ledger.surprise_loops, 1):
                print(f"\n{i}. {loop.blessing_id}")
                print(f"   Loop Type: {loop.loop_type}")
                print(f"   Recursion Depth: {loop.recursion_depth}")
                print(f"   Loop Integrity: {'✓' if loop.verify_loop_integrity() else '✗'}")
                print(f"   Cycle Stages:")
                for j, stage in enumerate(loop.cycle_stages, 1):
                    print(f"     {j}. {stage}")


def add_blessing(args):
    """Add a healing blessing"""
    try:
        ledger = MegazionLedger.load_from_file(args.ledger)
    except FileNotFoundError:
        print(f"✗ Error: Ledger file not found: {args.ledger}")
        sys.exit(1)
    
    blessing = HealingBlessing(args.disease, args.cure, args.industry, args.loop_category)
    
    if args.job_sector:
        for sector in args.job_sector:
            blessing.add_job_sector(sector)
    
    if args.school:
        for school in args.school:
            blessing.add_school(school)
    
    ledger.add_healing_blessing(blessing)
    ledger.save_to_file(args.ledger)
    
    print(f"✓ Healing blessing added: {args.disease}")
    print(f"  Cure: {args.cure}")
    print(f"  Industry: {args.industry}")
    print(f"  Loop Category: {args.loop_category}")


def add_gem(args):
    """Add a gem/element"""
    try:
        ledger = MegazionLedger.load_from_file(args.ledger)
    except FileNotFoundError:
        print(f"✗ Error: Ledger file not found: {args.ledger}")
        sys.exit(1)
    
    gem = GemElement(args.name, args.property, args.sector, args.loop_type)
    
    if args.application:
        for app in args.application:
            gem.add_application(app)
    
    ledger.add_gem_element(gem)
    ledger.save_to_file(args.ledger)
    
    print(f"✓ Gem/Element added: {args.name}")
    print(f"  Property: {args.property}")
    print(f"  Sector: {args.sector}")
    print(f"  Loop Type: {args.loop_type}")


def add_supernatural(args):
    """Add a supernatural surprise"""
    try:
        ledger = MegazionLedger.load_from_file(args.ledger)
    except FileNotFoundError:
        print(f"✗ Error: Ledger file not found: {args.ledger}")
        sys.exit(1)
    
    surprise = SupernaturalSurprise(args.name, args.category, args.sector)
    
    if args.protocol:
        for proto in args.protocol:
            surprise.add_protocol(proto)
    
    ledger.add_supernatural_surprise(surprise)
    ledger.save_to_file(args.ledger)
    
    print(f"✓ Supernatural surprise added: {args.name}")
    print(f"  Category: {args.category}")
    print(f"  Economic Sector: {args.sector}")


def add_ingredient(args):
    """Add an ingredient root"""
    try:
        ledger = MegazionLedger.load_from_file(args.ledger)
    except FileNotFoundError:
        print(f"✗ Error: Ledger file not found: {args.ledger}")
        sys.exit(1)
    
    root = IngredientRoot(args.ingredient, args.source, args.industries.split(','))
    
    if args.empire:
        for empire in args.empire:
            root.add_trade_empire(empire)
    
    ledger.add_ingredient_root(root)
    ledger.save_to_file(args.ledger)
    
    print(f"✓ Ingredient root added: {args.ingredient}")
    print(f"  Source: {args.source}")
    print(f"  Industries: {args.industries}")


def add_job(args):
    """Add a job/career"""
    try:
        ledger = MegazionLedger.load_from_file(args.ledger)
    except FileNotFoundError:
        print(f"✗ Error: Ledger file not found: {args.ledger}")
        sys.exit(1)
    
    job = JobCareer(args.title, args.blessing_source, args.industry)
    
    if args.spawned_job:
        for spawned in args.spawned_job:
            job.add_spawned_job(spawned)
    
    if args.school:
        for school in args.school:
            job.add_training_school(school)
    
    ledger.add_job_career(job)
    ledger.save_to_file(args.ledger)
    
    print(f"✓ Job/Career added: {args.title}")
    print(f"  Blessing Source: {args.blessing_source}")
    print(f"  Industry: {args.industry}")


def add_loop(args):
    """Add a surprise loop"""
    try:
        ledger = MegazionLedger.load_from_file(args.ledger)
    except FileNotFoundError:
        print(f"✗ Error: Ledger file not found: {args.ledger}")
        sys.exit(1)
    
    loop = SurpriseLoop(args.blessing_id, args.loop_type)
    
    if args.stage:
        for stage in args.stage:
            loop.add_cycle_stage(stage)
    
    ledger.add_surprise_loop(loop)
    ledger.save_to_file(args.ledger)
    
    print(f"✓ Surprise loop added: {args.blessing_id}")
    print(f"  Loop Type: {args.loop_type}")
    print(f"  Recursion Depth: {loop.recursion_depth}")
    print(f"  Loop Integrity: {'✓ VERIFIED' if loop.verify_loop_integrity() else '✗ FAILED'}")


def verify_ledger(args):
    """Verify ledger integrity"""
    try:
        ledger = MegazionLedger.load_from_file(args.ledger)
    except FileNotFoundError:
        print(f"✗ Error: Ledger file not found: {args.ledger}")
        sys.exit(1)
    
    print("=" * 80)
    print("🔍 MEGAZION LEDGER VERIFICATION")
    print("=" * 80)
    print()
    
    # Check loop integrity
    loop_integrity = ledger.verify_loop_integrity()
    print(f"Loop Integrity: {'✓ VERIFIED' if loop_integrity else '✗ FAILED'}")
    
    # Check individual loops
    print("\nIndividual Loop Status:")
    for i, loop in enumerate(ledger.surprise_loops, 1):
        status = "✓" if loop.verify_loop_integrity() else "✗"
        print(f"  {status} {loop.blessing_id} ({loop.recursion_depth} stages)")
    
    # Check audit hash
    current_hash = ledger.exchange_logic['audit_hash']
    computed_hash = ledger._compute_ledger_hash()
    # DEBUG
    import sys
    print(f"DEBUG: current={current_hash}", file=sys.stderr)
    print(f"DEBUG: computed={computed_hash}", file=sys.stderr)
    print(f"DEBUG: equal={current_hash == computed_hash}", file=sys.stderr)
    hash_valid = (current_hash == computed_hash) if current_hash and computed_hash else False
    if args.verbose:
        print(f"\n  Current:  {current_hash[:32]}...")
        print(f"  Computed: {computed_hash[:32]}...")
        print(f"  Match: {hash_valid}")
    print(f"\nAudit Hash: {'✓ VALID' if hash_valid else '✗ INVALID'}")
    
    # Check vault sync
    vault_sync = ledger.exchange_logic.get('vault_sync', False)
    print(f"Vault Sync: {'✓ ENABLED' if vault_sync else '✗ DISABLED'}")
    
    print()
    if loop_integrity and hash_valid:
        print("✓ MEGAZION Ledger is VALID and fully operational")
        print("  The self-reciprocating loops are active and theft-proof")
        sys.exit(0)
    else:
        print("✗ MEGAZION Ledger has ERRORS that must be resolved")
        sys.exit(1)


def export_ledger(args):
    """Export ledger to file"""
    try:
        ledger = MegazionLedger.load_from_file(args.ledger)
    except FileNotFoundError:
        print(f"✗ Error: Ledger file not found: {args.ledger}")
        sys.exit(1)
    
    ledger.save_to_file(args.output, format=args.format)
    print(f"✓ MEGAZION Ledger exported to {args.output} ({args.format.upper()} format)")


def show_yields(args):
    """Show blessing yields"""
    try:
        ledger = MegazionLedger.load_from_file(args.ledger)
    except FileNotFoundError:
        print(f"✗ Error: Ledger file not found: {args.ledger}")
        sys.exit(1)
    
    print("=" * 80)
    print("🔵 MEGAZION YIELD REPORT")
    print("=" * 80)
    print()
    
    yields = ledger.calculate_blessing_yield()
    
    print("PRIMARY YIELDS:")
    print(f"  Healing Blessings: {yields['total_healing_blessings']}")
    print(f"  Gems & Elements: {yields['total_gems_elements']}")
    print(f"  Supernatural Surprises: {yields['total_supernatural_surprises']}")
    print(f"  Ingredient Roots: {yields['total_ingredient_roots']}")
    print(f"  Job Careers: {yields['total_job_careers']}")
    print()
    
    print("SECONDARY YIELDS:")
    print(f"  Active Industries: {yields['active_industries']}")
    print(f"  Spawned Schools: {yields['spawned_schools']}")
    print(f"  Active Loops: {yields['total_surprise_loops']}")
    print()
    
    print("INFINITE YIELDS:")
    print(f"  Loop Multiplication Factor: {yields['loop_multiplication_factor']}")
    print()
    
    print("=" * 80)
    print("The gift isn't the thing — it's the loop of creation itself.")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(
        description="MEGAZION INHERITANCE LEDGER™ - CLI Interface",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create a new MEGAZION ledger
  %(prog)s create -o megazion.yaml
  
  # Show ledger details
  %(prog)s show megazion.yaml -v --section all
  
  # Add a healing blessing
  %(prog)s add-blessing megazion.yaml -d "Arthritis" -c "joint regeneration" -i "mobility tech" -l "movement economy"
  
  # Add a gem/element
  %(prog)s add-gem megazion.yaml -n "SkyDiamond" -p "levitation crystal" -s "aerospace, transport" -l "gravity control"
  
  # Verify ledger integrity
  %(prog)s verify megazion.yaml
  
  # Show yields
  %(prog)s yields megazion.yaml
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new MEGAZION ledger')
    create_parser.add_argument('-o', '--output', help='Output file path')
    create_parser.add_argument('-t', '--treasurer', default='Commander Bleu', help='Treasurer name')
    create_parser.add_argument('-f', '--format', choices=['yaml', 'json'], default='yaml', help='Output format')
    
    # Show command
    show_parser = subparsers.add_parser('show', help='Display the ledger')
    show_parser.add_argument('ledger', help='Ledger file path')
    show_parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed information')
    show_parser.add_argument('-s', '--section', choices=['all', 'healing', 'gems', 'supernatural', 'ingredients', 'jobs', 'loops'], 
                           default='all', help='Section to display (default: all)')
    
    # Add blessing command
    blessing_parser = subparsers.add_parser('add-blessing', help='Add a healing blessing')
    blessing_parser.add_argument('ledger', help='Ledger file path')
    blessing_parser.add_argument('-d', '--disease', required=True, help='Disease name')
    blessing_parser.add_argument('-c', '--cure', required=True, help='Cure name')
    blessing_parser.add_argument('-i', '--industry', required=True, help='Industry spawned')
    blessing_parser.add_argument('-l', '--loop-category', required=True, help='Loop category')
    blessing_parser.add_argument('-j', '--job-sector', action='append', help='Job sector (can specify multiple)')
    blessing_parser.add_argument('-s', '--school', action='append', help='School spawned (can specify multiple)')
    
    # Add gem command
    gem_parser = subparsers.add_parser('add-gem', help='Add a gem/element')
    gem_parser.add_argument('ledger', help='Ledger file path')
    gem_parser.add_argument('-n', '--name', required=True, help='Gem name')
    gem_parser.add_argument('-p', '--property', required=True, help='Gem property')
    gem_parser.add_argument('-s', '--sector', required=True, help='Sector')
    gem_parser.add_argument('-l', '--loop-type', required=True, help='Loop type')
    gem_parser.add_argument('-a', '--application', action='append', help='Application (can specify multiple)')
    
    # Add supernatural command
    supernatural_parser = subparsers.add_parser('add-supernatural', help='Add a supernatural surprise')
    supernatural_parser.add_argument('ledger', help='Ledger file path')
    supernatural_parser.add_argument('-n', '--name', required=True, help='Surprise name')
    supernatural_parser.add_argument('-c', '--category', required=True, help='Category')
    supernatural_parser.add_argument('-s', '--sector', required=True, help='Economic sector')
    supernatural_parser.add_argument('-p', '--protocol', action='append', help='Protocol (can specify multiple)')
    
    # Add ingredient command
    ingredient_parser = subparsers.add_parser('add-ingredient', help='Add an ingredient root')
    ingredient_parser.add_argument('ledger', help='Ledger file path')
    ingredient_parser.add_argument('-i', '--ingredient', required=True, help='Ingredient name')
    ingredient_parser.add_argument('-s', '--source', required=True, help='Source')
    ingredient_parser.add_argument('-n', '--industries', required=True, help='Industries (comma-separated)')
    ingredient_parser.add_argument('-e', '--empire', action='append', help='Trade empire (can specify multiple)')
    
    # Add job command
    job_parser = subparsers.add_parser('add-job', help='Add a job/career')
    job_parser.add_argument('ledger', help='Ledger file path')
    job_parser.add_argument('-t', '--title', required=True, help='Job title')
    job_parser.add_argument('-b', '--blessing-source', required=True, help='Blessing source')
    job_parser.add_argument('-i', '--industry', required=True, help='Industry')
    job_parser.add_argument('-j', '--spawned-job', action='append', help='Spawned job (can specify multiple)')
    job_parser.add_argument('-s', '--school', action='append', help='Training school (can specify multiple)')
    
    # Add loop command
    loop_parser = subparsers.add_parser('add-loop', help='Add a surprise loop')
    loop_parser.add_argument('ledger', help='Ledger file path')
    loop_parser.add_argument('-b', '--blessing-id', required=True, help='Blessing ID')
    loop_parser.add_argument('-l', '--loop-type', required=True, help='Loop type')
    loop_parser.add_argument('-s', '--stage', action='append', help='Cycle stage (can specify multiple)')
    
    # Verify command
    verify_parser = subparsers.add_parser('verify', help='Verify ledger integrity')
    verify_parser.add_argument('ledger', help='Ledger file path')
    verify_parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed verification info')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export ledger to file')
    export_parser.add_argument('ledger', help='Source ledger file path')
    export_parser.add_argument('-o', '--output', required=True, help='Output file path')
    export_parser.add_argument('-f', '--format', choices=['yaml', 'json'], default='yaml', help='Output format')
    
    # Yields command
    yields_parser = subparsers.add_parser('yields', help='Show blessing yields')
    yields_parser.add_argument('ledger', help='Ledger file path')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Execute command
    commands = {
        'create': create_ledger,
        'show': show_ledger,
        'add-blessing': add_blessing,
        'add-gem': add_gem,
        'add-supernatural': add_supernatural,
        'add-ingredient': add_ingredient,
        'add-job': add_job,
        'add-loop': add_loop,
        'verify': verify_ledger,
        'export': export_ledger,
        'yields': show_yields
    }
    
    commands[args.command](args)


if __name__ == "__main__":
    main()
