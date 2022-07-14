
import datetime

class Record:
    def __init__(self, amount, comment, date=None):       
        self.amount = amount                                
        self.comment = comment                            
        if date is None:                                  
            self.date = datetime.date.today()           
        else:
            self.date = datetime.datetime.strptime(date, '%Y-%m-%d').date()    
                                                                              
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = datetime.date.today()
        self.week_ago = datetime.date.today() - datetime.timedelta(days=7)    
                                                                              
    def add_record(self, record):
        self.records.append(record)                                            
                                                                              
    def get_today_status(self):                                                
        day_cash = []                                                          
        for record in self.records:
            if record.date == self.today:                                     
                day_cash.append(record.amount)
        return sum(day_cash)                                                    
    
    def get_week_status(self):
        week_cash = []
        for record in self.records:                                           
            if self.week_ago <= record.date <= self.today:                     
                week_cash.append(record.amount)                               
        return sum(week_cash)                                                  
    
    def today_limit_status(self):
        limit_status = self.limit - self.get_today_status()
        return limit_status
            
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories = self.today_limit_status()
        if calories > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories} кКал"
        else: 
            return f"Хватит есть!"

class CashCalculator(Calculator):
    USD_RATE = 65                                 
    EURO_RATE = 70                                   
    def get_today_cash_remained(self, currency="rub"):
        cash = self.today_limit_status()
        usd_rate = round(cash / CashCalculator.USD_RATE, 2)              
        eur_rate = round(cash / CashCalculator.EURO_RATE, 2)             
        rub_rate = round(cash, 2)
        if cash > 0:
            if currency == "rub":
                return f"На сегодня осталось {rub_rate} руб"            
            elif currency == "usd":                                     
                return f"На сегодня осталось {usd_rate} USD"             
            elif currency == "eur":
                return f"На сегодня осталось {eur_rate} Euro"
            else:
                return f"Валюта не поддерживается."
        elif cash == 0:
            return "Денег нет, держись"
        else:
            if currency == "rub":
                return f"Денег нет, держись: твой долг - {rub_rate} руб"
            elif currency == "usd":
                return f"Денег нет, держись: твой долг - {usd_rate} USD"
            elif currency == "eur":
                return f"Денег нет, держись: твой долг - {eur_rate} Euro"
            else:
                return f"Валюта не поддерживается."

class OutputResult:
    def output_result_cash(rate):
        print(f"Лимит денежных средств на сегодня: {cash_calculator.limit}")
        print("Потрачено: ")
        for rec in cash_calculator.records:
            print(f" - {rec.comment} за {rec.amount} {rate}")
        return cash_calculator.get_today_cash_remained(rate)

    def output_result_cal():
        print(f"Лимит калорий на сегодня: {cal_calculator.limit}")
        print("Потреблено: ")
        for rec in cal_calculator.records:
            print(f" - {rec.comment} на {rec.amount} cal")
        return cal_calculator.get_calories_remained()

if __name__ == '__main__':
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment="кофе")) 
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="2022-07-13"))
    #print(cash_calculator.get_today_cash_remained("rub"))
    print(OutputResult.output_result_cash("rub"), "\n")

    cal_calculator = CaloriesCalculator(2200)
    cal_calculator.add_record(Record(amount=230, comment="кофе")) 
    cal_calculator.add_record(Record(amount=480, comment="обед"))
    cal_calculator.add_record(Record(amount=125, comment="перекус"))
    cal_calculator.add_record(Record(amount=990, comment="ужин", date="2022-07-13"))   
    print(OutputResult.output_result_cal(), "\n")






# Класс для ввода значений
'''
capital = 1000
numeric = 145
description = "На обед"

class InputData(Calculator):
    def input(capital, numeric, description):
        cash_calculator = CashCalculator(capital)
        cash_calculator.add_record(Record(amount=numeric, comment=description)) 
        cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
        cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="2022-07-13"))
'''



'''
output = [
('бабки', [720, 1, 80, 25, 40]),
('какЭшки', [15000, 1, 75]),
('че-то еще', [9000, 1, 75, 180]),
]

def result(output):
    for money in output[0][1]:
        print(money)
print(result(output))

class InfoMessage:
    def result()
    print("Информационное сообщение")

    def get_message(self) -> str:
        return self.MESSAGE.format(**asdict(self))
'''