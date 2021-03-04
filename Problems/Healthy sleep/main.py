A = int(input())  # не менее А часов
B = int(input())  # не следует спать более B часов
H = int(input())  # Анн спит Н часов в сутки
if A <= H <= B:
    print("Normal")
elif A <= H >= B:
    print("Excess")
elif A >= H <= B:
    print("Deficiency")
