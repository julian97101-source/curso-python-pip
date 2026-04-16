import matplotlib.pyplot as plt

def generate_bar_char(name,lables, values):
    fig, ax = plt.subplots()
    ax.bar(lables,values)
    plt.savefig(f"./imgs/{name}.png")
    plt.close()

def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis("equal")
    plt.savefig("pie.png")
    plt.close()

if __name__ == "__main__":
    lables = ["a","b","c"]
    values = [45,70,60]
    #generate_bar_char(lables,values)
    generate_pie_chart(lables,values)