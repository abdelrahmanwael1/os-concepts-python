import threading
import time

receptionist = threading.Semaphore(2)


def enterExamination(n):
    print(f"patient {n} is waiting for his turn ")
    receptionist.acquire(n)
    print(f"patient {n} is in thr examinationroom ")
    time.sleep(2)
    print(f"patient {n} is out of examinationroom ")
    receptionist.release()


patients = []
for i in range(10):
    patient = threading.Thread(target=enterExamination, args=(i,))
    patients.append(patient)
    patient.start()
