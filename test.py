import configslicer
import time

while True:

    print("任意のBlockを入力(終了する場合はexitと入力)")
    blocks = input(">> ")

    if blocks.lower() == "exit":
        break
    else:
        print("任意のIDを入力")
        ids = input(">> ")

        print("任意のValueを入力")
        values = input(">> ")

        start = time.perf_counter()
            
        # ここに処理
        configslicer.file("test.txt").write(blocks,ids,values)

        '''
        with open("test.txt", mode='r', encoding='utf-8') as f:
            print("==========\n")
            print(f.read())
            print("==========\n")
        # ここに処理
        '''

        end = time.perf_counter()
        devtime = end - start
        print("Time: " + str(devtime) + "\n")