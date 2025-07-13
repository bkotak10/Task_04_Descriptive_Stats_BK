import sys
import csv
import math
from collections import defaultdict, Counter

# ======= DATA SOURCE: Uncomment the one you're currently using =======

DATA_FILE = '2024_fb_ads_president_scored_anon.csv'           # Facebook Ads
# DATA_FILE = '2024_fb_posts_president_scored_anon.csv'       # Facebook Posts
# DATA_FILE = '2024_tw_posts_president_scored_anon.csv'       # Twitter Posts

GROUP_COLUMNS = ['Page Id', 'Ad Id']  # Update these manually if needed
PRINT_GROUP_LIMIT = 5

# Allow CLI overrides (optional)
if len(sys.argv) > 1:
    DATA_FILE = sys.argv[1]
if len(sys.argv) > 2:
    GROUP_COLUMNS = sys.argv[2:]

print(f"\nUSING FILE: {DATA_FILE}")
print(f"GROUPING BY: {GROUP_COLUMNS}")

def try_float(val):
    try:
        return float(val)
    except:
        return None

def load_csv_rows(path):
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f))

def detect_column_types(rows):
    if not rows:
        return [], []
    example = rows[0]
    numeric = [col for col in example if any(key in col.lower() for key in ['count', 'like', 'spend', 'view', 'amount', 'score', 'impression'])]
    categorical = [col for col in example if col not in numeric]
    return numeric, categorical

def median(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n == 0:
        return None
    return (sorted_vals[n//2] if n % 2 != 0 else (sorted_vals[n//2 - 1] + sorted_vals[n//2]) / 2)

def describe_group(records, numeric_cols, cat_cols):
    stats = {}

    for col in numeric_cols:
        nums = [try_float(r[col]) for r in records if try_float(r.get(col)) is not None]
        if nums:
            mean = sum(nums) / len(nums)
            std = math.sqrt(sum((x - mean) ** 2 for x in nums) / len(nums))
            stats[col] = {
                'count': len(nums),
                'mean': round(mean, 2),
                'median': round(median(nums), 2),
                'std_dev': round(std, 2),
                'min': min(nums),
                'max': max(nums)
            }

    for col in cat_cols:
        values = [r[col] for r in records if r.get(col)]
        if values:
            freq = Counter(values)
            stats[col] = {
                'unique_count': len(freq),
                'most_common': freq.most_common(1)[0]
            }

    return stats

def group_by_keys(records, keys):
    grouped = defaultdict(list)
    for row in records:
        key = tuple(row.get(k, 'NA') for k in keys)
        grouped[key].append(row)
    return grouped

def main():
    rows = load_csv_rows(DATA_FILE)
    print(f"Total Records Loaded: {len(rows)}")

    num_cols, cat_cols = detect_column_types(rows)

    print("\n=== Overall Summary ===")
    print(describe_group(rows, num_cols, cat_cols))

    print("\n=== Grouped Summary ===")
    grouped = group_by_keys(rows, GROUP_COLUMNS)
    for i, (key, grp) in enumerate(grouped.items()):
        if i >= PRINT_GROUP_LIMIT:
            break
        print(f"\nGroup: {key}")
        print(describe_group(grp, num_cols, cat_cols))

if __name__ == "__main__":
    main()