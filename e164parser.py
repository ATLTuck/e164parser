import csv
import phonenumbers
import sys

def convert_to_e164(number):
    try:
        parsed_number = phonenumbers.parse(number, None)
        return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
    except phonenumbers.phonenumberutil.NumberParseException:
        return None

def convert_phone_numbers_in_csv(file_path, column_name):
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Find the index of the column we want to process
    column_index = next(i for i, v in enumerate(reader.fieldnames) if v == column_name)

    for row in rows:
        original_number = row[column_index]
        e164_number = convert_to_e164(original_number)
        row[column_index] = e164_number

    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    file_path = sys.argv[1]
    column_name = sys.argv[2]
    convert_phone_numbers_in_csv(file_path, column_name)
