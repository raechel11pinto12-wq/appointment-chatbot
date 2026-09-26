from datetime import datetime, timedelta
import json
import os


def get_valid_date(prompt: str) -> str:
    while True:
        date_str = input(prompt).strip()
        try:
            parsed_date = datetime.strptime(date_str, "%d/%m/%Y").date()
            if parsed_date < datetime.today().date():
                print(
                    "Bot: You cannot book an appointment in the past. Try again."
                )
                continue
            return date_str
        except ValueError:
            print(
                "Bot: Invalid date format! Please use DD/MM/YYYY with a 4-digit year (e.g., 25/12/2026)."
            )


def generate_ics_file(
    booking_id: int,
    clinic: str,
    fname: str,
    lname: str,
    service: str,
    date_str: str,
    time_str: str,
) -> str:
    start_dt = datetime.strptime(
        f"{date_str} {time_str}", "%d/%m/%Y %I:%M %p"
    )
    end_dt = start_dt + timedelta(minutes=30)

    dt_format = "%Y%m%dT%H%M%S"
    start_iso = start_dt.strftime(dt_format)
    end_iso = end_dt.strftime(dt_format)
    now_iso = datetime.now().strftime(dt_format)

    ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Appointment Bot//EN
CALSCALE:GREGORIAN
METHOD:REQUEST
BEGIN:VEVENT
UID:appointment-{booking_id}@{clinic.lower().replace(' ', '')}.com
DTSTAMP:{now_iso}
DTSTART:{start_iso}
DTEND:{end_iso}
SUMMARY:{service} - {clinic}
DESCRIPTION:Appointment for {fname} {lname} for {service} at {clinic}.
STATUS:CONFIRMED
END:VEVENT
END:VCALENDAR"""

    filename = f"appointment_{booking_id}.ics"
    with open(filename, "w") as file:
        file.write(ics_content.strip())

    return filename


class AppointmentBot:

    def __init__(self, clinic_name):
        self.clinic = clinic_name
        self.appointments = []
        self.nxtid = 1
        self.timeslots = [
            "9:00 AM",
            "10:00 AM",
            "11:00 AM",
            "1:00 PM",
            "2:00 PM",
            "3:00 PM",
            "4:00 PM",
        ]

        self.load_appointments()

    def save_appointments(self):
        with open("appointments.json", "w") as file:
            json.dump(self.appointments, file, indent=4)

    def load_appointments(self):
        if os.path.exists("appointments.json"):
            with open("appointments.json", "r") as file:
                self.appointments = json.load(file)

        if self.appointments:
            self.nxtid = max(app["id"] for app in self.appointments) + 1

    def book_appointment(self):
        print(f"\n--- Book Appointment at {self.clinic}! ---")

        fname = input("Bot: Enter your first name: ").strip()
        while not fname:
            print("Bot: Kindly enter name. This field cannot be blank.")
            fname = input("Bot: Enter your first name: ").strip()

        lname = input("Bot: Enter your last name: ").strip()
        while not lname:
            print("Bot: Kindly enter last name. This field cannot be blank.")
            lname = input("Bot: Enter your last name: ").strip()

        service = input("Bot: Enter your service: ").strip()
        while not service:
            print("Bot: Service field cannot be blank.")
            service = input("Bot: Enter your service: ").strip()

        date = get_valid_date("Bot: Enter your preferred date (DD/MM/YYYY): ")

        while True:
            time = input(
                f"Bot: Enter your preferred time {self.timeslots}: "
            ).strip()

            valid_slot = next(
                (
                    slot
                    for slot in self.timeslots
                    if slot.lower() == time.lower()
                ),
                None,
            )
            if not valid_slot:
                print(
                    f"Bot: Invalid time slot! Please choose strictly from {self.timeslots}."
                )
                continue

            conflict = any(
                app["date"] == date and app["time"].lower() == valid_slot.lower()
                for app in self.appointments
            )

            if conflict:
                print(
                    f"\nBot: Sorry {fname}, slot '{valid_slot}' on {date} is already taken."
                )
                taken_slots = [
                    app["time"].lower()
                    for app in self.appointments
                    if app["date"] == date
                ]
                available_slots = [
                    slot
                    for slot in self.timeslots
                    if slot.lower() not in taken_slots
                ]

                if available_slots:
                    print(
                        f"Bot: Available slots for {date}: {', '.join(available_slots)}\n"
                    )
                else:
                    print(
                        f"Bot: No slots available on {date}. Please choose another date.\n"
                    )
                    date = get_valid_date(
                        "Bot: Enter a new preferred date (DD/MM/YYYY): "
                    )
            else:
                time = valid_slot
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

        self.save_appointments()

        ics_filename = generate_ics_file(
            self.nxtid, self.clinic, fname, lname, service, date, time
        )

        self.nxtid += 1

        print(
            f"\nBot: Confirmed! Appointment #{booking['id']} booked for {fname} {lname} on {date} at {time}."
        )
        print(
            f"Bot: Calendar invite generated -> Saved as '{ics_filename}' in your folder!\n"
        )

    def view_appointments(self):
        if not self.appointments:
            print("\nBot: No appointments on file yet.\n")
            return

        print(f"\n--- {self.clinic} Appointments ---")
        for app in self.appointments:
            print(
                f"ID #{app['id']} | {app['fname']} {app['lname']} | Service: {app['service']} | Date: {app['date']} @ {app['time']}"
            )
        print()

    def clear_all_data(self):
        confirm = (
            input(
                "\nBot: Are you sure you want to delete ALL appointments? (yes/no): "
            )
            .strip()
            .lower()
        )
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