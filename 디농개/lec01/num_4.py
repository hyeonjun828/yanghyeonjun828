from lec01.num_3 import is_prime

def main():
    # 여기서 프로그램의 주 로직을 작성합니다.
    # 예를 들어, 사용자가 입력한 숫자가 소수인지 확인할 수 있습니다.
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

if __name__ == "__main__":
    main()
