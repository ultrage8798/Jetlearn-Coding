class Q:
    def __init__ (self,size):
        self.q = [None]*size
        self.front = 0
        self.rear = 0
        self.size = size
        self.available=size

    def enq(self,item):
        if self.available == 0:
            print("Queue Overflow!")
        else:
            self.q[self.rear] = item
            self.rear = (self.rear +1) % self.size
            self.available -= 1
    
    def deq(self):
        if self.available == self.size:
            print("Queue Underflow!")
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.size
            self.available += 1

    def peek(self):
        print(self.q[self.front])

    def getrear(self):
        print(self.q[self.rear])

    def print_q(self):
        print(self.q)

q1 = Q(4)
q1.enq(10)
q1.peek()
q1.getrear()
q1.enq(20)
q1.deq()
q1.peek()
q1.print_q()