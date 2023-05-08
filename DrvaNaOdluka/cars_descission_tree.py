import csv

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder

def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]
    return dataset


# KLlasifikator drva na odluka koe ke odreduva dali avtomobilot e prifatliv ili ne
if __name__ == '__main__':
    dataset = read_file('car.csv')

    # Koga stanuva zbor za kategoriski atr, treba da se napravi enkodiranje na atributite, vo numericki vrednosti -->  Ordinal encoder
    # Povtrono go delime na treniranje i testiranje na mnozestvoto

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset]) #Mapira se osven klasata od podatocnoto mnozestvo

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    # Klasifikator shto ke bide drvo na odluka
    # Kreirame instanca, prvin pisuvame spored koj atr sakame da se pravi podelba na dr atr vo drvoto ->pr entropy

    # clasifier = DecisionTreeClassifier(criterion='entropy', max_depth=5, max_leaf_nodes=20, random_state=0) # --> najmnogu pet nivoa

    #max_depth, maks dlabocina za vrednost na drvoto, random_state -> go kontrolira stepenot na slucajnost na atributi na podelba

    clasifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
    clasifier.fit(train_x, train_y) #trenirame

    print(f'Depth: {clasifier.get_depth()}')
    print(f'Number of leaves: {clasifier.get_n_leaves()}')

    accuracy = 0
    for i in range(len(test_set)):
        predicted_class = clasifier.predict([test_x[i]])[0] #predvidena klasa
        true_class = test_y[i] #vistinska klasa
        #proverka dali se ednakvi
        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)

    print(f'Accuracy: {accuracy}')

    #Koja karakteristika vlijaela najmnogu a koja najmalku vo procesot na treniranje
    #Najvazna i najmalku vazna karakteristika


    feature_importances = list(clasifier.feature_importances_)
    print(f'Feature importances: {feature_importances}')

    most_important_feature = feature_importances.index(max(feature_importances))
    print(f'Most important feature: {most_important_feature}')

    least_important_feature = feature_importances.index(min(feature_importances))
    print(f'Least important feature: {least_important_feature}')

    #Da se otstrani nekoja od karakteristikite i da proverime dali i kako ke vlijae na tocnosta

    #Ako ja otstranime najbitnata/najnebitnata karakteristika

    train_x_2 = list() #kopija na mnozestvoto, da go smestime celoto mnozestvo osven taa shto e najvazna
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != most_important_feature]
        train_x_2.append(row)

    test_x_2 = list()
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != most_important_feature]
        test_x_2.append(row)

    train_x_3 = list() #kopija na mnozestvoto, da go smestime celoto mnozestvo osven taa shto e najnevazna
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != least_important_feature]
        train_x_3.append(row)

    test_x_3 = list()
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != least_important_feature]
        test_x_3.append(row)

#Pravime nov klasifikator za novite mnozestva

    #Bez najvaznata karakteristika
    clasifier2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    clasifier2.fit(train_x_2, train_y)

    # Bez najmalku vaznata karakteristika
    clasifier3 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    clasifier3.fit(train_x_3, train_y)

    print(f'Depth (without most important feature): {clasifier2.get_depth()}')
    print(f'Number of leaves (without most important feature): {clasifier2.get_n_leaves()}')

    print(f'Depth (without least important feature): {clasifier3.get_depth()}')
    print(f'Number of leaves (without least important feature): {clasifier3.get_n_leaves()}')

    accuracy2 = 0
    for i in range(len(test_set)):
        predicted_class = clasifier2.predict([test_x_2[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy2 += 1

    accuracy2 = accuracy2 / len(test_set)

    print(f'Accuracy2: {accuracy2}')

    accuracy3 = 0
    for i in range(len(test_set)):
        predicted_class = clasifier3.predict([test_x_3[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy3 += 1
    accuracy3 = accuracy3 / len(test_set)

    print(f'Accuracy3: {accuracy3}')
