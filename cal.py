def calculate_bmi(weight, height):
    """計算 BMI 並返回值與分類"""
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "過輕"
    elif 18.5 <= bmi < 24:
        category = "正常"
    elif 24 <= bmi < 27:
        category = "過重"
    elif 27 <= bmi < 30:
        category = "輕度肥胖"
    elif 30 <= bmi < 35:
        category = "中度肥胖"
    else:
        category = "重度肥胖"
    return bmi, category

def main():
    print("歡迎使用 BMI 計算機")
    try:
        height = float(input("請輸入身高（公尺）："))
        weight = float(input("請輸入體重（公斤）："))
        bmi, category = calculate_bmi(weight, height)
        print(f"您的 BMI 為：{bmi:.2f}")
        print(f"體重分類：{category}")
    except ValueError:
        print("請輸入有效的數字。")

if __name__ == "__main__":
    main()