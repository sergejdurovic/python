def main():
    try:
        n = int(input("Input n: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    i = 0
    q = 0

    while (i * i) <= n:
        q = i * i
        i = i + 1

    print(q)

if __name__ == "__main__":
    main()
# looks like i learned how to use git today
