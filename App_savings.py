from classes.money import Money

July=Money('July', 1000)
#пока функция выводит сумму, которую нужно сохранить, я ее вижу и вбиваю
#в функцию upgrade вручную
July.upgrade(200)

# August = Money('August', 1700)
# #пока должен сохранить название July.upgrade чтобы складывала дальше, 
# #подумать над названием
# July.upgrade(340)

# September = Money('September', 1600)
# July.upgrade(320)

October = Money('October', 2000)
July.upgrade(400)
