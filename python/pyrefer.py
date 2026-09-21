class AppointmentBot:
    def __init__(self, business_name):
        """Initializes the bot's memory and settings."""
        self.business_name = business_name
        self.appointments = []  # Bot's internal memory/database

    def book_appointment(self):
        """Method to handle booking a new slot."""
        print(f"\n--- Booking for {self.business_name} ---")

        name = input("Bot: What is your full name? ").strip()
        while not name:
            name = input("Bot: Name cannot be blank. Please enter your name: ").strip()

        service = input("Bot: What service do you need? ").strip()
        date = input("Bot: Preferred date (e.g., Oct 15): ").strip()
        time_slot = input("Bot: Preferred time (e.g., 2:00 PM): ").strip()

        # Build booking record
        booking = {
            "id": len(self.appointments) + 1,
            "name": name,
            "service": service,
            "date": date,
            "time": time_slot,
        }

        self.appointments.append(booking)
        print(f"\nBot: Confirmed! Appointment #{booking['id']} booked for {name}.\n")

    def view_appointments(self):
        """Method to view all saved appointments."""
        if not self.appointments:
            print("\nBot: No appointments on file yet.\n")
            return

        print(f"\n--- {self.business_name} Appointments ---")
        for appt in self.appointments:
            print(
                f"ID #{appt['id']} | {appt['name']} | {appt['service']} | {appt['date']} @ {appt['time']}"
            )
        print("-" * 35 + "\n")

    def start(self):
        """Main loop driving the chatbot interaction."""
        print(f"==========================================")
        print(f" Welcome to {self.business_name}'s Booking Bot ")
        print(f"==========================================")

        while True:
            print("Options: [1] Book  [2] View All  [3] Quit")
            user_choice = input("You: ").strip().lower()

            if user_choice in ["1", "book"]:
                self.book_appointment()
            elif user_choice in ["2", "view"]:
                self.view_appointments()
            elif user_choice in ["3", "quit", "exit"]:
                print(f"\nBot: Thank you for choosing {self.business_name}. Goodbye!")
                break
            else:
                print("Bot: Invalid option. Please enter 1, 2, or 3.\n")


# --- Running the Program ---
if __name__ == "__main__":
    # Create an instance of the class
    my_bot = AppointmentBot("Apex Dental Clinic")
    
    # Launch the bot
    my_bot.start()