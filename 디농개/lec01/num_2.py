from lec01.num import is_even

def main():
    total =0

    for i in range(1,100):
        if is_even(i):
            total += i
    print(f"1부터 100까지 짝수의 합은 {total}입니다")

    # 지능형 리스트
    #even_100= {i 

if __name__ == '__main__':
    main()