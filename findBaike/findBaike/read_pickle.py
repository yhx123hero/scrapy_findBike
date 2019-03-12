import pickle
f = open("item_result.txt","rb")
while True:
    try:
        d = pickle.load(f)
        print(d)
    except:
        break