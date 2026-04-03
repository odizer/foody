foods = ["chapatii", "rice", "dengu", "sukuma", "matoke", "beans", "ugali", "pilau", "mandazi", "samosa"]
def foods_available():
    print("The following foods are available:")
    for food in foods:
        print(food)
    if "chapati" in foods:
        print("Chapati is available.")  
    else:
        print("Chapati is not available now.")

foods_available()