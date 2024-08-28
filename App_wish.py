from classes.wish import Wish
from classes.money import Money

MyFirstWish = Wish('PS', 500, 6)
#MySecondWish = Wish('Kindle', 100, 2)

zp1 = Money('ZP', 1000)
#нужно продумать логику где save_for_month из класса Wish перекидывается в money_to_save в классе Money.

zp1.upgrade(83)
