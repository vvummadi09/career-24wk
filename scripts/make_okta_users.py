"""Generate synthetic users as a CSV for Okta import."""
import csv

# Okta's template header, split into a list of column names
HEADER = "login,firstName,lastName,middleName,honorificPrefix,honorificSuffix,email,title,displayName,nickName,profileUrl,secondEmail,mobilePhone,primaryPhone,streetAddress,city,state,zipCode,countryCode,postalAddress,preferredLanguage,locale,timezone,userType,employeeNumber,costCenter,organization,division,department,managerId,manager".split(",")

DOMAIN = "example.com"  # reserved for examples: no real person gets mail

PEOPLE = [
    ("Ava", "Patel", "Software Engineer", "Engineering"),
    ("Liam", "Chen", "Engineering Manager", "Engineering"),
    ("Sofia", "Garcia", "Financial Analyst", "Finance"),
    ("Noah", "Kim", "Accounts Payable Clerk", "Finance"),
    ("Mia", "Johnson", "HR Generalist", "Human Resources"),
    ("Ethan", "Brown", "Sales Representative", "Sales"),
    ("Zara", "Ali", "IT Administrator", "IT"),
]

with open("okta_users.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=HEADER, restval="")
    writer.writeheader()
    for first, last, title, dept in PEOPLE:
        email = f"{first.lower()}.{last.lower()}@{DOMAIN}"
        writer.writerow({
            "login": email,
            "email": email,
            "firstName": first,
            "lastName": last,
            "title": title,
            "department": dept,
        })

print(f"Wrote {len(PEOPLE)} users to okta_users.csv")