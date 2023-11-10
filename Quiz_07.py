import random

def generate_lotto_numbers():
    results = []

    for _ in range(6):
        number = random.randint(1, 45)

        # 중복된 숫자가 없도록 확인
        while number in results:
            number = random.randint(1, 45)

        results.append(number)
        print(number)

    return results

def main():
    generated_numbers = generate_lotto_numbers()
    numbers_str = ', '.join(map(str, generated_numbers))
    print(f"생성된 로또 번호는 {numbers_str} 입니다")

if __name__ == "__main__":
    main()
