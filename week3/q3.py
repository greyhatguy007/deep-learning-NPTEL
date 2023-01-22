def mse(y,y_hat):
    mse=0
    for i,j in zip(y,y_hat):
        mse += (i-j)**2
    return mse/len(y)

y = [10, 5, 7, 8, 6]
y_hat = [9, 6, 5, 7, 5]

print(mse(y=y,y_hat=y_hat))

## output : 1.6