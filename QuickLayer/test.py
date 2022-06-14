import time
import quicklayer

while True:

    print("任意の階層値を入力(終了する場合はexitと入力)")
    inp = input(">> ")

    if inp.lower() == "exit":
        break
    else:
        layer = quicklayer.get(__file__, inp)
        start = time.perf_counter()

        if layer == None:
            print("Response: None\n 何らかのエラーが発生しました。\n")
        else:
            print("\nResponse: " + layer +"\n")
            
        end = time.perf_counter()
        devtime = end - start
        print("Time: " + str(devtime) + "\n")