#!/usr/bin/env python3
"""
CLI tool for managing Biblical Cosmology and Investor Outreach systems.
"""

import argparse
import json
import sys
from cosmology_integration import (
    BiblicalCosmologySystem,
    InvestorOutreachSystem,
    IntegratedCodexSystem
)


def cmd_cosmology_status(args):
    """Show cosmology system status."""
    system = BiblicalCosmologySystem(args.cosmology_file)
    status = system.get_system_status()
    
    print("🌌 BIBLICAL COSMOLOGY SYSTEM STATUS")
    print("=" * 60)
    print(f"Status: {status['status']}")
    print(f"Timestamp: {status['timestamp']}")
    print(f"Deployment Status: {status['deployment_status']}")
    print(f"Devices Updated: {status['devices_count']}")
    print(f"Health Stacks: {', '.join(status['health_stacks'])}")
    print("=" * 60)


def cmd_cosmology_realms(args):
    """Show three realms information."""
    system = BiblicalCosmologySystem(args.cosmology_file)
    
    print("🌌 THREE REALMS")
    print("=" * 60)
    
    for realm_name in ["shamayim", "eretz", "sheol"]:
        realm = system.get_realm(realm_name)
        if realm:
            print(f"\n{realm['name']} ({realm_name.upper()})")
            print(f"  Description: {realm['description']}")
            print(f"  Device Mapping: {realm['device_mapping']}")
            print(f"  Systems: {', '.join(realm['systems'])}")
    
    print("=" * 60)


def cmd_cosmology_heavens(args):
    """Show seven heavens information."""
    system = BiblicalCosmologySystem(args.cosmology_file)
    
    print("🌌 SEVEN HEAVENS")
    print("=" * 60)
    
    for level in range(1, 8):
        heaven = system.get_heaven_level(level)
        if heaven:
            print(f"\n{level}. {heaven['name']} ({heaven.get('hebrew', '')})")
            print(f"   Description: {heaven['description']}")
            print(f"   Device: {heaven['device_mapping']}")
            print(f"   Function: {heaven['function']}")
    
    print("=" * 60)


def cmd_cosmology_worlds(args):
    """Show four Kabbalistic worlds."""
    system = BiblicalCosmologySystem(args.cosmology_file)
    
    print("🌌 FOUR KABBALISTIC WORLDS")
    print("=" * 60)
    
    for world_name in ["atzilut", "beriah", "yetzirah", "asiyah"]:
        world = system.get_kabbalistic_world(world_name)
        if world:
            print(f"\n{world['name']} ({world.get('hebrew', '')})")
            print(f"  Description: {world['description']}")
            print(f"  Device: {world['device_mapping']}")
            print(f"  Characteristics:")
            for char in world.get('characteristics', []):
                print(f"    • {char}")
    
    print("=" * 60)


def cmd_cosmology_souls(args):
    """Show five soul levels."""
    system = BiblicalCosmologySystem(args.cosmology_file)
    
    print("🌌 FIVE SOUL LEVELS")
    print("=" * 60)
    
    for level_name in ["nefesh", "ruach", "neshamah", "chayah", "yechidah"]:
        level = system.get_soul_level(level_name)
        if level:
            print(f"\n{level['name']} ({level.get('hebrew', '')})")
            print(f"  Level: {level['level']}")
            print(f"  Description: {level['description']}")
            print(f"  Device: {level['device_mapping']}")
            print(f"  Functions:")
            for func in level.get('functions', []):
                print(f"    • {func}")
    
    print("=" * 60)


def cmd_outreach_status(args):
    """Show investor outreach status."""
    system = InvestorOutreachSystem(args.outreach_file)
    
    print("💼 INVESTOR OUTREACH STATUS")
    print("=" * 60)
    print(f"Status: {system.outreach_data.get('status')}")
    print(f"Checklist Status: {system.outreach_data.get('checklist_status')}")
    print(f"Timestamp: {system.outreach_data.get('timestamp')}")
    print("=" * 60)


def cmd_outreach_investors(args):
    """List all target investors."""
    system = InvestorOutreachSystem(args.outreach_file)
    investors = system.get_investors()
    
    print("💼 TARGET INVESTORS (Tier 1)")
    print("=" * 60)
    
    for investor in investors:
        print(f"\n{investor['name']}")
        print(f"  Focus: {investor['focus']}")
        print(f"  Stage: {investor['stage']}")
        print(f"  Contact Status: {investor['contact_status']}")
        print(f"  Tracking Link: {investor['tracking_link']}")
        print(f"  QR Code: {'✓' if investor['qr_code_generated'] else '✗'}")
        print(f"  Social Teaser: {'✓' if investor['social_teaser_ready'] else '✗'}")
    
    print("=" * 60)
    print(f"Total: {len(investors)} investors")


def cmd_outreach_pitch(args):
    """Show pitch deck status."""
    system = InvestorOutreachSystem(args.outreach_file)
    pitch = system.get_pitch_deck_status()
    
    print("💼 PITCH DECK STATUS")
    print("=" * 60)
    print(f"Status: {pitch.get('status')}")
    print(f"Version: {pitch.get('version')}")
    print(f"Slides: {len(pitch.get('slides', []))}")
    print(f"Formats: {', '.join(pitch.get('formats_available', []))}")
    
    if args.detailed:
        print("\nSlide Breakdown:")
        for slide in pitch.get('slides', []):
            print(f"\n  Slide {slide['slide']}: {slide['title']}")
            print(f"    {slide['content']}")
    
    print("=" * 60)


def cmd_outreach_roles(args):
    """Show role assignments."""
    system = InvestorOutreachSystem(args.outreach_file)
    
    print("💼 ROLE ASSIGNMENTS")
    print("=" * 60)
    
    for person in ["evolynn", "pihya"]:
        role = system.get_role_assignment(person)
        if role:
            print(f"\n{person.upper()}")
            print(f"  Role: {role['role']}")
            print(f"  Responsibilities:")
            for resp in role.get('responsibilities', []):
                print(f"    • {resp}")
    
    print("=" * 60)


def cmd_outreach_timeline(args):
    """Show outreach timeline."""
    system = InvestorOutreachSystem(args.outreach_file)
    timeline = system.get_outreach_timeline()
    
    print("💼 OUTREACH TIMELINE")
    print("=" * 60)
    
    for phase_name, phase_data in timeline.items():
        print(f"\n{phase_name.replace('_', ' ').upper()}")
        print(f"  Status: {phase_data.get('status')}")
        print(f"  Duration: {phase_data.get('duration')}")
        
        if 'deliverables' in phase_data:
            print("  Deliverables:")
            for item in phase_data['deliverables']:
                print(f"    {item}")
        
        if 'activities' in phase_data:
            print("  Activities:")
            for item in phase_data['activities']:
                print(f"    • {item}")
    
    print("=" * 60)


def cmd_integrated_status(args):
    """Show integrated system status."""
    system = IntegratedCodexSystem(args.cosmology_file, args.outreach_file)
    system.print_summary()


def cmd_integrated_deploy(args):
    """Generate deployment packages."""
    system = IntegratedCodexSystem(args.cosmology_file, args.outreach_file)
    
    print("🚀 GENERATING DEPLOYMENT PACKAGES")
    print("=" * 60)
    
    if args.target in ["aws", "all"]:
        print("\n📦 AWS Deployment Package:")
        aws_files = system.generate_aws_deployment_package(args.output_dir)
        for file_type, filepath in aws_files.items():
            print(f"  ✓ {file_type}: {filepath}")
    
    if args.target in ["github", "all"]:
        print("\n📦 GitHub Deployment Package:")
        github_files = system.generate_github_deployment_package(args.output_dir)
        for file_type, filepath in github_files.items():
            print(f"  ✓ {file_type}: {filepath}")
    
    print("\n" + "=" * 60)
    print("✅ Deployment packages generated successfully")


def main():
    parser = argparse.ArgumentParser(
        description="Biblical Cosmology and Investor Outreach Management CLI"
    )
    
    # Global options
    parser.add_argument(
        '--cosmology-file',
        default='biblical_cosmology_codex.json',
        help='Path to cosmology codex file'
    )
    parser.add_argument(
        '--outreach-file',
        default='investor_outreach_system.json',
        help='Path to outreach system file'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Cosmology commands
    cosmology = subparsers.add_parser('cosmology', help='Cosmology system commands')
    cosmology_sub = cosmology.add_subparsers(dest='subcommand')
    
    cosmology_sub.add_parser('status', help='Show cosmology system status').set_defaults(func=cmd_cosmology_status)
    cosmology_sub.add_parser('realms', help='Show three realms').set_defaults(func=cmd_cosmology_realms)
    cosmology_sub.add_parser('heavens', help='Show seven heavens').set_defaults(func=cmd_cosmology_heavens)
    cosmology_sub.add_parser('worlds', help='Show four Kabbalistic worlds').set_defaults(func=cmd_cosmology_worlds)
    cosmology_sub.add_parser('souls', help='Show five soul levels').set_defaults(func=cmd_cosmology_souls)
    
    # Outreach commands
    outreach = subparsers.add_parser('outreach', help='Investor outreach commands')
    outreach_sub = outreach.add_subparsers(dest='subcommand')
    
    outreach_sub.add_parser('status', help='Show outreach status').set_defaults(func=cmd_outreach_status)
    outreach_sub.add_parser('investors', help='List target investors').set_defaults(func=cmd_outreach_investors)
    
    pitch_cmd = outreach_sub.add_parser('pitch', help='Show pitch deck status')
    pitch_cmd.add_argument('--detailed', action='store_true', help='Show detailed slide breakdown')
    pitch_cmd.set_defaults(func=cmd_outreach_pitch)
    
    outreach_sub.add_parser('roles', help='Show role assignments').set_defaults(func=cmd_outreach_roles)
    outreach_sub.add_parser('timeline', help='Show outreach timeline').set_defaults(func=cmd_outreach_timeline)
    
    # Integrated commands
    integrated = subparsers.add_parser('integrated', help='Integrated system commands')
    integrated_sub = integrated.add_subparsers(dest='subcommand')
    
    integrated_sub.add_parser('status', help='Show full integrated status').set_defaults(func=cmd_integrated_status)
    
    deploy_cmd = integrated_sub.add_parser('deploy', help='Generate deployment packages')
    deploy_cmd.add_argument('--target', choices=['aws', 'github', 'all'], default='all',
                           help='Deployment target')
    deploy_cmd.add_argument('--output-dir', default='.', help='Output directory')
    deploy_cmd.set_defaults(func=cmd_integrated_deploy)
    
    # Parse arguments
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    if hasattr(args, 'func'):
        args.func(args)
        return 0
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
