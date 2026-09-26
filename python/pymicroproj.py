import json
import os
class AppointmentBot:

    def __init__(self,clinic_name):
        self.clinic = clinic_name
        self.appointments = []
        self.nxtid= 1
        self.timeslots=  ["9:00 AM", "10:00 AM", "11:00 AM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM"]

        self.load_appointments()

    def save_appointments(self):
    
        with open("appointments.json", "w") as file:
            json.dump(self.appointments, file, indent=4)

    def load_appointments(self):
                
         if os.path.exists("appointments.json"):
                    
             with open("appointments.json", "r") as file:
                self.appointments = json.load(file)

                       
         if self.appointments:
             self.nxtid = max(app['id'] for app in self.appointments) + 1

    def book_appointment(self):
            print(f"---Book Appointment at {self.clinic}!---")

            fname=input("Bot: Enter your first name: ").strip()
            while not fname:
                print("Bot: Kindly enter name. This field cannot be blank")
                fname = input("Bot: Enter your first name: ").strip()
            lname = input("Bot: Enter your full name: ").strip()
            while not lname:
                print("Bot: Kindly enter last name. This field cannot be blank")
                lname = input("Bot: Enter your lasst name: ").strip()
            service=input("Bot: Enter your service: ").strip()
            date=input("Bot: Enter your preferred date (DD/MM/YYYY): ").strip()
            while True:
                time=input(f"Bot: Enter your preferred time {self.timeslots}: ").strip()

                conflict=any(app['date'].lower() == date.lower() and app['time'].lower() == time.lower() for app in self.appointments)
                if conflict:
                    print(f"Sorry {fname}, Appointment {time} on {date} already taken. Please enter again.")

                    takenslots= [ app['time'].lower() for app in self.appointments
                    if app['date'].lower() == date.lower()]

                    available_slots = [
                        slot for slot in self.timeslots
                        if slot.lower() not in takenslots
                    ]

                    if available_slots:
                        print(f"Bot: Available slots for {date}: {', '.join(available_slots)}")
                    else:
                        print(f"Bot: No slots available on {date}. Please try a different date or time.")
                        print("Please try entering another time slot.\n")
                else:

                   break

            booking = {
                     "id": self.nxtid,
                     "fname": fname,
                     "lname": lname,
                     "service": service,
                     "date": date,
                     "time": time,
                    }
            self.appointments.append(booking)
            self.nxtid += 1

            self.save_appointments()
            print(f"\nBot: Confirmed! Appointment #{booking['id']} booked for {fname} on {date} at {time}.\n")

    def view_appointments(self):
        if not self.appointments:
            print("\nBot: No appointments on file yet.\n")
            return

        print(f"\n--- {self.clinic} Appointments ---")
        for app in self.appointments:
            print(f"ID #{app['id']} | {app['fname']} |{app['lname']} | {app['service']} | {app['date']} @ {app['time']}")
        print()

    def clear_all_data(self):
        confirm = input("\nBot: Are you sure you want to delete ALL appointments? (yes/no): ").strip().lower()
        if confirm in ["yes", "y"]:
            
            self.appointments = []
            self.nxtid = 1

            
            if os.path.exists("appointments.json"):
                os.remove("appointments.json")

            print("Bot: All appointment data has been permanently cleared.\n")
        else:
            print("Bot: Action cancelled.\n")

    def start(self):
        print(f"Welcome to {self.clinic}'s Appointment Bot\n")

        while True:
            print("Options: [1] Book  [2] View All  [3] Clear  [4] Quit")
            user_choice = input("You: ").strip().lower()

            if user_choice in ["1", "book"]:
                self.book_appointment()
            elif user_choice in ["2", "view"]:
                self.view_appointments()
            elif user_choice in ["3", "clear"]:
                self.clear_all_data()
            elif user_choice in ["4", "quit", "exit"]:
                print(f"\nBot: Thank you for choosing {self.clinic}. Goodbye!")
                break
            else:
                print("\nBot: Invalid option. Please choose 1, 2, 3 or 4.\n")


if __name__ == "__main__":
   my_bot = AppointmentBot("The John Melon Clinic")
   my_bot.start()