class Fruit:
    def __init__(self,color,taste,shape,prefrence):
        self.color=color
        self.shape=shape
        self.prefrence=prefrence
        self.taste=taste
    def get_shape(self):
        return self.shape
    def set_shape(self,new_shape):
        self.shape=new_shape
    def increase_prefrence(self):
        self.prefrence=self.prefrence+1
    def show_fruit(self):
        print("Hello I am a fruit with {}, {}, {}, {}".format(self.color, self.shape, self.prefrence, self.taste))
apple=Fruit("red","sour","sphere",1)
apple.show_fruit()
apple.increase_prefrence()
apple.show_fruit()
print(apple.get_shape())
apple.set_shape("square")
apple.show_fruit()

orange=Fruit("orange","sweet","sphere",1)
orange.show_fruit()
orange.increase_prefrence()
orange.show_fruit()