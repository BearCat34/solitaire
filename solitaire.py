
class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def peeklast(self):
        return self.items[0]

    def printall(self, index):
        if len(self.items) != 0:
            if index == 0:
                count = 1
                print(self.items[0], end = ' ')
                while count != len(self.items):
                    print('*', end = ' ')
                    count += 1
                print('')
            else:
                for item in self.items:
                    print(item, end = ' ')
                print('')

        else:
            print('')


class Solitaire:
    def __init__(self, ncards):
        self.t = []
        self.__CardNo = len(ncards)
        self.__ColNo = (self.__CardNo // 8) + 3
        self.__ChanceNo = self.__CardNo * 2
        for i in range(self.__ColNo):
            self.t.append(Deque())
        for i in range(self.__CardNo):
            self.t[0].add_front(ncards[i])

    def display(self):
        i = 0
        while i != self.__ColNo:
            print(i, ':', sep = '', end = ' ')
            self.t[i].printall(i)
            i += 1

    def move(self, c1, c2):
        if c1 == 0 and c2 == 0:
            self.t[0].add_front(self.t[0].remove_rear())

        elif c1 == 0 and c2 > 0:
            if self.t[c2].size() != 0:
                if self.t[c2].peek() > self.t[c1].peeklast():
                    self.t[c2].add_front(self.t[c1].remove_rear())
            else:
                self.t[c2].add_front(self.t[c1].remove_rear())

        elif c1 > 0 and c2 > 0:
            if self.t[c2].size() != 0:
                if self.t[c2].peek() > self.t[c1].peeklast():
                    while self.t[c1].size() != 0:
                        self.t[c2].add_front(self.t[c1].remove_rear())
            else:
                self.t[c2].add_front(self.t[c1].remove_rear())


    def IsComplete(self):
        con1 = False
        con2 = False
        if self.t[0].size() == 0:
            con1 = True
        for i in range(1, self.__ColNo):
            if self.t[i].size() == self.__CardNo:
                con2 = True
        return con1 and con2

    def play(self):
        print("*****************************************NEW GAME***************************************")
        for game_iter in range(self.__ChanceNo):
            self.display()
            print("Round", game_iter+1, "out of", self.__ChanceNo, end = ": ")
            col1 = int(input("Move from row no.:"),10)
            print("Round", game_iter+1, "out of", self.__ChanceNo, end = ": ")
            col2 = int(input("Move to row no.:"),10)
            if col1 >= 0 and col2 >= 0 and col1 < self.__ColNo and col2 < self.__ColNo:
                self.move(col1, col2)
            if (self.IsComplete() == True):
                print("You Win in", game_iter+1, "steps!")
                break;
            else:
                if game_iter+1 == self.__ChanceNo:
                   print("You Loss!")
        print()

play()
