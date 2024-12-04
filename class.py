class goa():
    name=""
    drink=""
    club=""
    def party(self):
        print("Let's Party")
    def beach(self):
        print("Enjoying the beach view")

ramesh=goa()
suresh=goa()

ramesh.name="Ramesh Rajasekar"
suresh.name="Suresh Chandrasekar"

ramesh.drink="Yes"
suresh.drink="No"

ramesh.club="Yes"
suresh.club="No"

print(ramesh.name,"\n",ramesh.drink,"\n",ramesh.club)
ramesh.party()
print(suresh.name,"\n",suresh.drink,"\n",suresh.club)
suresh.beach()
n=int(input("Enter:"))
