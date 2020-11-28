class computer:
    def config(self,ram,cpu):
        self.ram=ram
        self.cpu=cpu
        print(f"{self} has config as " ,cpu,ram)
dell=computer()
compact=computer()

dell.config("8gb","i5")
compact.config("4gb","i3")



