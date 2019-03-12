import pickle
import re
f = open("item1.txt","rb")
f1 = open("item_result.txt","wb")
d_past = pickle.load(f)
while True:
    try:
        d_last = pickle.load(f)
        p = "http://www.baike.com"
        if re.search(p,str(d_last)):
            pickle.dump(d_last,f1)
        else:
            pickle.dump(d_past,f1)
            d_past = d_last
    except:
        pickle.dump(d_past,f1)
        break
