def quadrado(x):
    return x * x

def main():
    for i in range (10):
        print("{} ao quadrado é {}".format(i, quadrado(i)))

if __name__ == "__main__":
    main()