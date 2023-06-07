from test import Patient, Queue


def create_patient():
    first_name = input("Введите ваше имя - ")
    last_name = input("Введите ваше фамилия - ")
    age = input("Ваш возраст - ")
    patient = Patient(first_name, last_name, age)
    return patient


queue = Queue()

while True:
    print('Добро пожаловать в нашу клинику')
    choice = input('Д/Н Вы хотите взять место?')
    if choice.lower() == 'д':
        patient = create_patient()
        queue.add_patient(patient)
        print(f'Вы успешно в очереди - ваш талон - {patient.id}')
    print('Просмотреть сколько осталось по времени - 1\nУзнать сколько времени я в очереди - 2\nСколько людей в очереди - 3\nПосмотреть инфу о талоне - 4\nЗакрыть талон - 5')
    choice = int(input('Ваш выбор - '))
    talon = int(input('Введите ваш талон - '))
    if choice == 1:
        print(queue.remain(talon))
    elif choice == 2:
        print(queue.get_time_info(talon))
    elif choice == 3:
        print(queue.get_active_patients())
    elif choice == 4:
        print(queue.close_talon(talon))