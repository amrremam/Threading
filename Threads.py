import multiprocessing

import multiprocessing.process
import time


start = time.perf_counter()


def some():
    time.sleep(1)
    print("sleeping...")



if __name__ == '__main__' :
    start = time.perf_counter()

    prosseces = []
    for _ in range(10) :
        p = multiprocessing.Process(target=some)
        p.start()
        prosseces.append(p)

    for process in prosseces :
        process.join()

    finish = time.perf_counter()
    print(f"finished in {round(finish - start, 2)} second(s)")




