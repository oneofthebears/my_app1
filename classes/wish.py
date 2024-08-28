class Wish:
    def __init__(self, what_you_wish, how_much_cost, period_months):
        self.what_you_wish = what_you_wish
        self.how_much_cost = how_much_cost
        self.period_months = period_months
        save_for_month = how_much_cost / period_months
        print(f'You want {what_you_wish} in {period_months} months, it costs {how_much_cost} USD. You need to save {save_for_month} USD every month')
        

#класс Желание
#what_you_wish - пишем, то что желаешь
#how_much_cost - пишем, сколько это стоит
#period_months - пишем, за сколько месяцев мы хотим этого
#save_for_month - покажет сколько нужно откладывать каждый месяц
