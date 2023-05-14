from sklearn.neural_network import MLPClassifier



def read_dataset():
    data = []
    with open('winequality.csv') as f:
        _ = f.readline() #Prviot red go ignorirame
        while True:
            line = f.readline().strip()
            #Iterirame se dodeka ne dojdeme do prazen string
            if line == '':
                break
            parts = line.split(';')
            data.append(list(map(float, parts[:-1])) + parts[-1:])

    return data

#Gi delime na treniracko, validacisko i treniracko
def divide_sets(dataset):
        bad_classes = [x for x in dataset if x[-1] == 'bad']
        good_classes = [x for x in dataset if x[-1] == 'good']
        train_set = bad_classes[:int(len(bad_classes)* 0.7)] + good_classes[:int(len(good_classes) * 0.7)]
        #Gade sto sme zastanale so trenirackoto, plus pomnozuyvame za 10 procenti
        val_set = bad_classes[int(len(bad_classes) * 0.7):int(len(bad_classes) * 0.8)] + good_classes[int(len(good_classes) * 0.7) : int(len(good_classes) * 0.8)]
        test_set = bad_classes[int(len(bad_classes) * 0.8):] + good_classes[int(len(good_classes) * 0.8):]

        return train_set, val_set, test_set


if __name__ == '__main__':
    dataset = read_dataset()
    train_set, val_set, test_set = divide_sets(dataset)

    #Karakteristikite da gi imame kako edna vrednost vo dadenio0t klasifikator, a labelitge da se vo posebna promenliva

    #Site elementi osven klasata, gi kreiravme dadenite podatocni mnzoestva

    train_x = [x[:-1] for x in train_set]
    train_y = [x[-1] for x in train_set]

    val_x = [x[:-1] for x in val_set]
    val_y = [x[-1] for x in val_set]

    test_x = [x[:-1] for x in test_set]
    test_y = [x[-1] for x in test_set]

    #So val mnoz da se odbere najdobriot broj nevroni od 5, 10 i 100
    #3 klasifikatrori i sekoj da ima razlicen br nevroni vo skrieniot sloj

    classifier = MLPClassifier(5, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(100, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)


    #Da gi istrenirame
    classifier.fit(train_x, train_y)
    classifier2.fit(train_x, train_y)
    classifier3.fit(train_x, train_y)

    #Validacija so validacisko mnozestvo
    #Finalniot klasifikator so najdobra tocnost

    final_classifier = None
    max_Acc = 0 #tocnosta na modelot - inicijalizacija

    for i, c in enumerate([classifier, classifier2, classifier3]): #go izmenuva sekoj el i mu dodava element na sekoj element za pozicijata vo listata, torka od index i el.
        val_predictions = c.predict(val_x)
        val_acc = 0
        #dali imame poklopuvanje na vistinskata klasa i toa sho go pominuvame
        for true, pred in zip(val_y, val_predictions):
            if true == pred:
                val_acc += 1

        val_acc = val_acc/ len(val_y)

        print(f'Klasifikatorot {i} ima tocnost so validacisko mnozestvo od {val_acc}')

        if val_acc > max_Acc:
            max_Acc = val_acc
            final_classifier = c

        # Go naogjame klasifikatorot so najdobra tocnost


        #Presmetka na tocnosta so testirackoto so finalniot klasifikator

        acc = 0
        predictions = final_classifier.predict(test_x)

        for true, pred in zip(test_y, predictions):
            if true == pred:
                acc += 1

        acc = acc/len(test_y)

    print(f'Tocnosta so testirackoto mnozestvo e: {acc}')
