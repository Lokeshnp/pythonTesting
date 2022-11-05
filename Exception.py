ItemsInCart=0
#2 items will be added to cart

# if ItemsInCart!= 2:
#     raise Exception("Products cart count not matching")


# assert (ItemsInCart == 2)

#Try catch mechanism we will use except instead of catch

# try:
#     with open('filelog.txt', 'r') as reader:
#         reader.read()
#
# except:
#     print("Some how I have reached this block coz there is failure")
#

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up records")


