import json
import re

def parse_license_file(input_file, output_file):
    # Regex to capture: INCREMENT "feat" "issue" "expiry" "count" "SUPERSEDE \
    pattern = re.compile(
        r'^INCREMENT\s+"([^"]+)"\s+"([^"]+)"\s+"([^"]+)"\s+"(\d+)"\s+"SUPERSEDE \\'
    )

    results = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line.startswith("INCREMENT"):
                match = pattern.match(line)
                if match:
                    feature_name, issue_date, expiry_date, count = match.groups()
                    
                    results.append({
                        "feature_name": feature_name,
                        "issue_date": issue_date,
                        "expiry_date": expiry_date,
                        "count": int(count)
                    })

    # Save to JSON
    with open(output_file, 'w', encoding='utf-8') as out:
        json.dump(results, out, indent=4)

    print(f"Extracted {len(results)} feature records → saved to {output_file}")


# Example usage:
input_license_file = r"C:\temp\license.lic"
output_json_file = r"C:\temp\Lic_Features.txt"

parse_license_file(input_license_file, output_json_file)
