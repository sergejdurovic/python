def main():
    n = 0
    s = 0
    
    try:
        x = int(input("Enter x: "))
    except ValueError:
        return

    while True:
        if x == -1:
            if n == 0:
                m = -1
                a = -1
            else:
                a = s / n
            
            print(f"{n}, {s}, {m}, {a}")
            break
        else:
            n = n + 1
            s = s + x
            
            if n == 1:
                m = x
            else:
                if x < m:
                    m = x
            
            try:
                x = int(input("Enter x: "))
            except ValueError:
                break

if __name__ == "__main__":
    main()