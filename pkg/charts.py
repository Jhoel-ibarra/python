import matplotlib.pyplot as plt

def generate_bar_chart(name ,labels , values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f"./imgs/{name}png")
  plt.close()

def generate_pie_chart(labels , values):
  fig, ax = plt.subplots()
  ax.pie(values , labels = labels)
  plt.savefig("pie.png")
  plt.close()

if __name__ == '__main__':
  labels=["a", "b", "f","c"]
  values= [25 , 25,50]
  #generar_bar_chart(label, values)
  generate_pie_chart(labels, values)