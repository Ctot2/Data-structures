x = "Did you know that an owl has eyes that are more than twice as big as the eyes of other birds of comparable weight? And that when an owl partially closes its eyes during the day, it is just blocking out light? Sometimes I wish I could be an owl too."

def owl_count(x):
    y = x.split()
    print(y)
    owl_counter = 0

    for i in range(len(y)):
        if y[i] == "owl":
            owl_counter = owl_counter + 1

    return owl_counter

print(owl_count(x))
