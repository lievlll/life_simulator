from ecosystem import Ecosystem
from utils import print_status, print_result

REPO_URL = "https://github.com/lievlll/life_simulator"

def main():
    eco = Ecosystem()
    eco.setup(rabbit_count=10, fox_count=3)

    print("Симулятор жизни запущен!")
    print_status(eco)

    while not eco.is_over() and eco.day < 20:
        eco.simulate_day()
        print_status(eco)

    print_result(eco)

if __name__ == "__main__":
    main()
