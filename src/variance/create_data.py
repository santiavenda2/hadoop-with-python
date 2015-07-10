
import random


def main():
    with open('data.csv', 'wb') as f:
        for i in range(100000):
            f.write(str(random.gauss(mu=0, sigma=0.25)))
            f.write("\n")


if __name__ == "__main__":
    main()
