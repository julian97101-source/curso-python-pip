import csv

def read_csv(path):
    with open(path, "r") as csvfile:
        reader= csv.reader(csvfile, delimiter= ",")
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data
    



if __name__ == "__main__":
    data= read_csv("./11-app/data.csv")
    #print(data[0])

    #Esta fue la solucion que con mi propio esfuerzo y ayuda de claud por pedazos
    #logre crear un diccionario solo de los años y poblacion por año
    #population_per_year= list(map(lambda d: {key: d[key] for key in d if key.endswith("Population")}, data))
    #print(population_per_year[0])
    