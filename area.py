def area(length,width):
    print(str(length * width) + ' square feet')
    return length * width
    print(str(length * width))

def main ():
    house = area(50,20)
    yard = area(50,50)
    total = house + yard

    print('House is ' + str(house) + ' square feet')
    print(str(yard) + ' square feet')
    print(str(total) + ' square feet')

main()
