# fibonacci.py

def fib():
    fibs = [1, 2]
    for i in range(1,101):
        num=fibs[-2]+fibs[-1]
        fibs.append(num)
    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
