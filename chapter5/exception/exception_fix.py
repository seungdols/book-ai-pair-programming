def main():
    try:
        divisor = 1  # 수정: 0에서 1로 변경하여 0으로 나누는 상황 방지
        x = 1 / divisor
    except Exception as e:
        print("Error", e)

    try:
        my_dict = {'name': 'Alice'}
        age = my_dict.get('age', 0)  # 'age' 키가 없으면 0을 반환
    except Exception as e:
        print("Error", e)

    try:
        # 수정: 변환 가능한 문자열 사용
        number = int('123')  # 'abc' 대신 '123' 사용
    except ValueError as e:
        print("Error", e)
        # 예외 발생 시 대응 코드
        # 예: 사용자에게 다시 입력 요청 또는 기본값 설정
        number = 0

if __name__ == "__main__":
    main()
