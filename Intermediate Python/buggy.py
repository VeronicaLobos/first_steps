
def eligible_voters(people):

    vips = []

    for person in people:
        if person.get("age") > 17:
            if person.get("country").lower() == "germany":
                vips.append(person.get("name"))

    return vips

def main():
    people_list = [
        {"name": "Alice", "age": 20, "country": "Germany"},
        {"name": "Bob", "age": 17, "country": "Germany"},
        {"name": "Charlie", "age": 25, "country": "France"},
        {"name": "David", "age": 30, "country": "Germany"}
    ]

    print(eligible_voters(people_list))

    # Example usage:
    assert eligible_voters(people_list) == ['Alice', 'David']

if __name__ == "__main__":
    main()