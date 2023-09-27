class prime_Range:
    def display(self):
        l = []
        a = eval(input("Enter the starting  number: "))
        b = eval(input("Enter the ending number: "))
        for i in range(a, b + 1):
            c = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    c = c + 1
            if c == 2:
                l.append(i)
        print(f"prime numbers between {a} and {b} are {l}")
p1=prime_Range()
p1.display()