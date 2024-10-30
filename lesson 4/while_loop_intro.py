a = 5

# while a < 10:
#     if a == 7:
#         break
#     print(a, "10 dan kichik")
#     a += 1
# else:
#     print("Loop finished")

# print('Outside of the loop')

while True:
    a = float(input('a = '))
    b = float(input('b = '))

    print('a + b = ', a + b)

    prompt = input('Do you want to add more numbers? (yes or no) ')

    if prompt != 'yes':
        break
