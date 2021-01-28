def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def rachet_vod(string):
    # Расчет с НДС
    sum_dogov = float(string)
    #Разбивка 60х40
    sum_holodvod = round((sum_dogov/100)*60,2)
    sum_otveden = round(sum_dogov - sum_holodvod,2)
    #Суммы Без НДС
    #sumh_beznds = round(sum_holodvod-(sum_holodvod*float(20))/120,4)
    #sumot_beznds = round(sum_otveden-(sum_otveden*float(20))/120,4)
    tarif_holodvod = 24.92
    tarif_otveden = 16.72
    v_holodvod = round(sum_holodvod/tarif_holodvod,4)
    v_otveden = round(sum_otveden/tarif_otveden,4)
    return (f"Тариф Водоснабжения С НДС {tarif_holodvod}'\n' Тариф Водоотведения С НДС {tarif_otveden} '\n'Сумма холодной воды: {sum_holodvod} '\n'  Сумма отведения: {sum_otveden}'\n'  кубы водоснабжение = {v_holodvod}'\n' кубы отведения = {v_otveden} ")
