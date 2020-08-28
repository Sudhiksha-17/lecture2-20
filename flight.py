class Flight():
 def__init__(self, capacity):
     self.capacity = capacity
     self.passengers =[]
 def add_passengers(self, name):
      if  not self.open_seats()   #if self.open_seats==0
         return False
      self.passengers.append(name) 
          return True
 def open_seats(self):
      return self.capacity - len(self.passengers)
flight= Flight(3)

people=["Harry", "Ron", "Hermione", "Ginny", "Draco"]
for  person in people:
    success= flight.add_passenger(person)
     if success:
         print(f"Added{person} to flight successfully")
    else
         print(f"No availabeseats for{person}")
         sss
