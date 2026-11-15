def celsius_a_kelvin(temperatura):
    return temperatura + 273.15

def milivolts_a_volts(tensio):
    return tensio / 1000
if __name__ == '__main__':
    print(celsius_a_kelvin(25))
    print(milivolts_a_volts(3300))
