import time


def watch(file):
    file.seek(0)
    while True:
        currentPos = file.tell()  # tell current postion
        # print("currentPos", currentPos)
        file.seek(0, 2)  # seek to the end of the file
        # this tell the size of the file cause current the pointer is at the end
        endPos = file.tell()
        # print("endPos", endPos)

        if currentPos < endPos:  # check the position of current and end
            file.seek(currentPos)
            chs = file.read(endPos - currentPos)  # read until the end
        else:
            time.sleep(0.1)
            continue
        yield chs  # it keeps generator new character to a sequence, I guess.  similar to return, but return only return once


if __name__ == '__main__':
    file = open("client.txt", "r")
    chs = watch(file)
    for ch in chs:
        print(ch, end='', flush=True)
