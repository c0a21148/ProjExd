import random
global x,y
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
x = 10
y = 2

def main():
    print("対象文字")
    for i in range(10):
        x.append(alpha[random.sample(alpha,25)])
    print(x)
    print("表示文字")
    for j in range(8):
        y.append(x[random.randint(0,9)])
    print(y)