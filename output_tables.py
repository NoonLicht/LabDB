from tabulate import tabulate
from app.models import Main, Name, LastName, MiddleName, Street
from app import db

def output_all_tables():
    print("\n=== Main Table ===")
    main_entries = Main.query.all()
    print(tabulate([entry.__dict__ for entry in main_entries], headers="keys", tablefmt="pretty"))

    print("\n=== Name Table ===")
    name_entries = Name.query.all()
    print(tabulate([entry.__dict__ for entry in name_entries], headers="keys", tablefmt="pretty"))

    print("\n=== LastName Table ===")
    last_name_entries = LastName.query.all()
    print(tabulate([entry.__dict__ for entry in last_name_entries], headers="keys", tablefmt="pretty"))

    print("\n=== MiddleName Table ===")
    middle_name_entries = MiddleName.query.all()
    print(tabulate([entry.__dict__ for entry in middle_name_entries], headers="keys", tablefmt="pretty"))

    print("\n=== Street Table ===")
    street_entries = Street.query.all()
    print(tabulate([entry.__dict__ for entry in street_entries], headers="keys", tablefmt="pretty"))

if __name__ == "__main__":
    output_all_tables()
