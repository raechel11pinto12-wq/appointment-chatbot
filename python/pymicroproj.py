class AppointmentBot:
    def __init__(self,clinic_name):
        self.clinic=clinic_name
        self.appointments=[]

    def book_appointment(self):
        print(f"\n--- Booking for appointment at {self.clinic} ---")
        name=input("Bot: What is your full name? ").strip()

        while not name:
              name=input("Bot: Name cannot be blank. Please enter your name: ").strip()
        service=input("Bot: What service do you need? ").strip()
        date=input("Bot: Preferred date (e.g., Oct 15): ").strip()
        time_slot=input("Bot: Preferred time (e.g., 2:00 PM)").strip()

        booking={
            "id":len(self.appointments)+1,
            "name":name,
            "service":service,  
            "date":date,
            "time":time_slot,
             }

        self.appointments.append(booking)
        print(f"\nBot: Confirmed! Appointment #{booking['id']} booked for {name}.\n")
    def view_appointments(self):
     if not self.appointments:
         print("\nBot: No appointments on file yet.\n")
         return
     print(f"\n--- {self.clinic} Appointments ---")
     for appointment in self.appointments:
            print(f"ID #{appointment['id']} | {appointment['name']} | {appointment['service']} | {appointment['date']} @ {appointment['time']}")
    def start(self):
     print(f"Welcome to {self.clinic}'s Appointment Bot")

     while True:
            print("Options: [1] Book  [2] View All  [3] Quit")
            user_choice=input("You: ").strip().lower()
    
            if user_choice in ["1","book"]:
                self.book_appointment()
            elif user_choice in ["2","view"]:
                self.view_appointments()
            elif user_choice in ["3","quit","exit"]:
                print(f"\nBot: Thank you for choosing {self.clinic}. Goodbye!")
                break
if __name__ == "__main__":
   
    my_bot = AppointmentBot("Apex Dental Clinic")
    
    my_bot.start()

