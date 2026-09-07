import json

data = json.load(open('scratch/visual_audit_report.json', encoding='utf-8'))
print(f"Total flagged: {data['total_flagged']}")
print(f"White backgrounds: {len(data['white_backgrounds'])}")
print(f"\nRatios anómalos ({len(data['ratio_skewed'])}):")
for c in data['ratio_skewed']:
    print(f"  {c['id']}: {c['detail']} | {c['file']}")
