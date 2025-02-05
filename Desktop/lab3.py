hicheel1 = input("Хичээл 1-ийн нэр: ")
hicheel2 = input("Хичээл 2-ийн нэр: ")

bairlal = int(input("Хичээл 2-ын ямар дугаарт байгаа үсгийг хайх вэ?: "))

if 0 <= bairlal < len(hicheel2):  
    usug = hicheel2[bairlal]
    bairshil = hicheel1.find(usug)
    print(f"{bairlal} дугаар дахь '{usug}' үсэг хичээл 1-ийн нэрэнд {bairshil} дугаарт дээр олдлоо.")
else:
    print("Оруулсан индекс хичээл 2-ийн нэрийн уртаас хэтэрсэн байна!")
