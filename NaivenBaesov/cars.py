import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
#go cita csv file-ot
def read_file(file_name):
    #prvin go otavarame fileot
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]

    return dataset
if __name__ == '__main__':
    #da go vcitame mnozestvoto, kako lista od listi
    # sekoj red e na sekoj primerok
    dataset = read_file('car.csv')
    encoder = OrdinalEncoder() #da gi pretvori vo brojki, zborovite
    encoder.fit([row[:-1] for row in dataset]) #da se mapiraat site vrednosti kako karakteristiki, osven poslednata kolona shto pretstavuva klasa

    #go delime na dve podmnozestva

    #70% treniranje na modelot ---> int(0.7*len(dataset))
    train_set = dataset[:int(0.7*len(dataset))]
    #od prva do pretposledna --> karakteristiki, vlez
    train_x = [row[:-1] for row in train_set]
    #samo poslednata kolona --> predviduvanje, izlez
    train_y = [row[-1] for row in train_set]

    train_x = encoder.transform(train_x)

    test_set = dataset[int(0.7*len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    #moze da treba poslednite a ne prvite, vnimavaj na toj del!
    test_x = encoder.transform(test_x)
    #da ja mapirame strin kategorijata vo int so encoder

#treniranje na modelot
    classifier = CategoricalNB()
    classifier.fit(train_x, train_y) #shto e vlez, shto izlez --> fit samo so terniranje

    accuracy = 0
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0] #predvidena klasa
        true_class = test_y[i] #vistinska klasa
        #proverka dali se ednakvi
        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)

    print(f'Accuracy: {accuracy}')
    #Nov primerok
    entry = [el for el in input().split(' ')]
    encoded_entry = encoder.transform([entry]) #da gi transformirame

    predicted_class = classifier.predict(encoded_entry)[0]
    print(predicted_class)