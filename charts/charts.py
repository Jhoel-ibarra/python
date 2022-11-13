import matplotlib.pyplot as plt 

# para crear una grafica redondo (pie)
def generate_pie_chart():
    labels = ["a", "b", "c"]
    values = [200, 43, 120]

    fig , ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig("pie.png") #para crear una carpeta y guardar la grafica 
    plt.close()

# para crear una grafica en barra lili (bar) 
labels = ["a", "b", "c"]
values = [200, 43, 120]

def generate_bar_chart(labels , values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig("bar.png")
  plt.close()

 ## plt.show()  para q se detenga en ese punto 