import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

#データを用意
datasets = np.array([[4,7], [8,10], [13,11], [17,14]])
x = datasets[:,0]
y = datasets[:,1]

#点で描画
plt.scatter(x, y, color="black", label="dataset")
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="best")
plt.show()

#線グラフ1
def function(x):
  return (x-10)**2

x2 = np.linspace(4, 17, 5) 
y2 = function(x2)           
plt.plot(x2, y2, color="blue", linewidth=3, label="plot example")
plt.show()

#線グラフ２
x2 = np.linspace(4, 17, 100)
y2 = function(x2)
plt.plot(x2, y2, color="blue", linewidth=3, label="plot example")
plt.show()

#複数のグラフを描画
plt.scatter(x, y, color="black", label="dataset")
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x2, y2, color="blue", linewidth=3, label="plot example")
plt.legend(loc="best")
plt.show()

#ラベル変更
plt.scatter(x, y, color="black", label="データセット")
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x2, y2, color="blue", linewidth=3, label="プロット例")
plt.legend(loc="best")
plt.show()