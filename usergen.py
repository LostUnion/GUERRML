import re
import random
import argparse

class USERGEN:
    @staticmethod
    def get_username():
        first_names = [
            "James", "John", "Robert",
            "Michael", "William", "David",
            "Richard", "Joseph", "Charles",
            "Thomas", "Christopher",
            "Daniel", "Matthew", "Anthony",
            "Donald", "Mark", "Paul",
            "Steven", "Andrew", "Kenneth",
            "Joshua", "Kevin", "Brian",
            "George", "Edward", "Ronald",
            "Timothy", "Jason", "Jeffrey",
            "Ryan", "Jacob", "Gary",
            "Nicholas", "Eric", "Jonathan",
            "Stephen", "Larry", "Justin",
            "Scott", "Brandon", "Benjamin",
            "Samuel", "Gregory", "Alexander",
            "Patrick", "Frank", "Raymond",
            "Jack", "Dennis", "Jerry"]

        last_names = [
            "Smith", "Johnson", "Williams",
            "Brown", "Jones", "Garcia",
            "Miller", "Davis", "Rodriguez",
            "Martinez", "Hernandez", "Lopez",
            "Gonzalez", "Wilson", "Anderson",
            "Thomas","Taylor", "Moore",
            "Jackson", "Martin", "Lee",
            "Perez", "Thompson", "White",
            "Harris", "Sanchez", "Clark",
            "Ramirez", "Lewis", "Robinson",
            "Walker", "Young", "Allen", "King",
            "Wright", "Scott", "Torres",
            "Nguyen", "Hill", "Flores", "Green",
            "Adams", "Nelson", "Baker", "Hall",
            "Rivera", "Campbell", "Mitchell",
            "Carter", "Roberts"]

        clean_first_name = [name for name in first_names if len(name) <= 9]
        clean_last_name = [name for name in last_names if len(name) <= 9]

        first_name = random.choice(clean_first_name)
        last_name = random.choice(clean_last_name)

        number = random.randint(12, 99)

        return f"{first_name}{last_name}{number}"
    
    @staticmethod
    def get_email():
        def insert_underscores(username):
            return re.sub(r'(?<!^)(?=[A-Z])', '_', username)

        def insert_dots_between_letters_and_digits(username):
            return re.sub(r'(?<=\D)(?=\d)', '.', username)

        def variant_composer(username, sep1="_", sep2="."):
            u = re.sub(r'(?<!^)(?=[A-Z])', sep1, username)
            u = re.sub(r'(?<=\D)(?=\d)', sep2, u)
            return u
        
        username = USERGEN.get_username()
            
        email_variants = [
            insert_underscores(username),
            insert_dots_between_letters_and_digits(username),
            variant_composer(username, "_", "."),
            variant_composer(username, ".", "."),
        ]

        return random.choice(email_variants).lower()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="USER GENERATION")
    parser.add_argument("--option", "-opt", type=str, help="Option: username or email", required=True)
    parser.add_argument("--count", "-c", type=int, default=1, help="How many to generate")
    args = parser.parse_args()

    for _ in range(args.count):
        if args.option == "username":
            print(USERGEN.get_username())
        elif args.option == "email":
            print(USERGEN.get_email())
        else:
            parser.print_help()
            break