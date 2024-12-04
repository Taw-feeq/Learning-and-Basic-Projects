class laptop():
    def variables(self):
        price=""
        processor=""
        ram=""
        print("Price:",self.price)
        print("Processor:", self.processor)
        print("Ram:",self.ram)

hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price="5000"
hp.processor="p4"
hp.ram="2"

dell.price="12000"
dell.processor="i3"
dell.ram="4"

lenovo.price="50000"
lenovo.processor="i9"
lenovo.ram="12"

hp.variables()
dell.variables()
lenovo.variables()