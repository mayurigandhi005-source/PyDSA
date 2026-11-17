class Hospital:
    def __init__(self):
        self.queue = []
# 1. Add Patient (enqueue)

    def enqueue(self):
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if priority not in [1, 2, 3]:
            print("Invalid Priority")
            return

        patient = (priority, pid, name)
        self.queue.append(patient)

        self.queue.sort()

        print("Patient added successfully")

 # 2. Display the next patient to be treated. (display_next)

    def display_next(self):
        if not self.queue:
            print("No patients in queue")
        else:
            p = self.queue[0]
            print("Next Patient:")
            print("Patient ID:", p[1])
            print("Patient Name:", p[2])
            print("Priority:", p[0])

    # 3. Remove a patient from the queue after treatment. (dequeue)
    def dequeue(self):
        if not self.queue:
            print("No patients to remove!")
        else:
            p = self.queue.pop(0)
            print("Treated Patient:", p[2])

    # 4. Display all waiting patients in priority order(display_all)
    def display_all(self):
        if not self.queue:
            print("No waiting patients")
        else:
            print("\nWaiting Patients:")
            for p in self.queue:
                print("ID:", p[1],
                      "Name:", p[2],
                      "Priority:", p[0])

h = Hospital()

while True:
    print("\n HOSPITAL EMERGENCY MANAGEMENT")
    print("1. Add Patient (Enqueue)")
    print("2. Display Next Patient")
    print("3. Remove Patient (Dequeue)")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        h.enqueue()

    elif choice == 2:
        h.display_next()

    elif choice == 3:
        h.dequeue()

    elif choice == 4:
        h.display_all()

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")