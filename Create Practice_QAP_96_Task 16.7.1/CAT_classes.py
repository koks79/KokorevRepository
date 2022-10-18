class CatPetFriends:
    def __init__(self, name, breed, gender, age, reg_num, status):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.age = age
        self.reg_num = reg_num
        self.status = status

    def get_name(self):
        return self.name
    def get_breed(self):
        return self.breed
    def get_gender(self):
        return self.gender
    def get_age(self):
        return self.age
    def get_reg_num(self):
        return self.reg_num
    def get_status(self):
        return self.status

    def output_info_pet(self):
        print(f'Имя животного: {self.name},\n Порода животного: {self.breed},\n Пол животного: {self.gender},\n Возраст животного: {self.age}, \n Регистрационный номер животного: {self.reg_num},\n Статус животного: {self.status}')

