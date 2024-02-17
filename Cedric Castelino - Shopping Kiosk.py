import PySimpleGUI as sg
import string, random

theme = 'DarkRed1'
Title_colour = '#800000'

#creates a random code for user
letter = string.ascii_letters
random_letter1 = random.choice(letter).lower()
random_letter2 = random.choice(letter).lower()
random_number1 = random.randint(1,9)
random_number2 = random.randint(1,9)
generated_code = (str(random_letter1) + str(random_number1) + str(random_letter2) + str(random_number2))

#sets theme to red and white (for coles)
sg.theme(theme)

#is an example of what the program would be like for an existing customer
saved_user = {'John Smith': 'a1b1'}

#creates welcome window
layout = [[sg.Text('Welcome to Coles', size=(17, 1), background_color='#800000', font=("Helvetica", 25), justification='center')],
          [sg.Text("Please Enter your Personal Shopper Code")],
          [sg.InputText()],
          [sg.Button("I'm Ready to Shop"), sg.Button("I don't have one"),sg.Button('Colour') ,sg.Button('Exit')]]
layout_2 = [[sg.Text("Please enter your name")],
            [sg.InputText()],
            [sg.Button("OK"), sg.Button("Cancel")]]
colour = [[sg.Text(' Colour Options', size=(20, 1), background_color=Title_colour, justification='center', font=("Helvetica", 25))],
         [sg.Text('-' * 100, size=(47, 1))],
         [sg.Button('Default View'),sg.Button('Light View'),sg.Button('Dark View'),sg.Button('Colour Blind Option')],
         [sg.Text('_' * 100, size=(47, 1))],
         [sg.Button('Done')]]
window1 = True
windowtwo = False
window = sg.Window("Welcome").Layout(layout)
namew = sg.Window("Input Name").Layout(layout_2)
Colour = sg.Window("Colour Configuration").Layout(colour)
#runs window 1
while window1 == True:
    event, values = window.Read()
    if event == 'Colour':
        Colour.un_hide()
        colour_window = True
        while colour_window == True:
            event2, values2 = Colour.read()
            colour_window = True
            if event2 == "Done":
                Colour.hide()
                break
            elif event2 == "Dark View":
                sg.theme('Black')
                Title_colour = '#4a4747'
                sg.popup_ok('Your colour configuration has been changed and ', 'will appear after continuing from the login screen')
            elif event2 == "Default View":
                sg.theme(theme)
                Title_colour = '#800000'
                sg.popup_ok('Your colour configuration has been changed and ', 'will appear after continuing from the login screen')
            elif event2 == "Light View":
                sg.theme('Default')
                Title_colour = '#9c9c9c'
                sg.popup_ok('Your colour configuration has been changed and ', 'will appear after continuing from the login screen')
            elif event2 == "Colour Blind Option":
                sg.theme('SystemDefault1')
                Title_colour = '#9c9c9c'
                sg.popup_ok('Your colour configuration has been changed and ', 'will appear after continuing from the login screen')

    elif event == 'Exit':
        answer = sg.popup_yes_no('Are you sure you want to exit?')
        if answer == "Yes":
            window.close()
            break
    elif event == "I don't have one":
        namew.un_hide()
        name_window = True
        while name_window == True:
            event2, values2 = namew.read()
            name_window = True
            if event2 == "OK":
                person_name = values2[0]
                namew.hide()
                if len(values2[0]) < 1:
                    sg.popup("Please enter a valid name")
                else:
                    sg.popup("Your unique code is: " + generated_code)
                break
            elif event2 == "Cancel":
                namew.hide()
                window.un_hide()
                break
    #code for personal passcode
    elif values[0] == generated_code:
                ok = sg.PopupOK("Welcome "+person_name)
                if ok == "OK":
                    window1 = False
                    windowtwo = True
                    new_customer = True
    elif values[0] == saved_user['John Smith']:
        person_name = 'John Smith'
        ok = sg.PopupOK("Welcome "+person_name)
        if ok == "OK":
            window1 = False
            windowtwo = True
            existing_customer = True
    else:
        sg.PopupOK("That code doesn't match any of our records, please try again")

fruits_section = [{"name":"Apple", "price":3.50, "info":'/kg',"current_stock":46, "max_stock":100},
{"name":"Kiwi", "price":0.40, "info":' each', "current_stock":12, "max_stock":70},
{"name":"Banana", "price":4.00, "info":'/kg', "current_stock":79, "max_stock":100},
{"name":"Apricot", "price":15, "info":'/kg', "current_stock":42, "max_stock":50},
{"name":"Avocado", "price":2.,  "info":' each', "current_stock":27, "max_stock":50},
{"name":"Blueberries", "price":4.90, "info":' each', "current_stock":20, "max_stock":60},
{"name":"Pear", "price":6.90,  "info":'/kg', "current_stock":38, "max_stock":55},
{"name":"Grapes", "price":4.80,  "info":'/kg', "current_stock":59, "max_stock":90},
{"name":"Orange", "price":5.90,  "info":' each', "current_stock":10, "max_stock":55},
{"name":"Mango", "price":2.90,  "info":' each', "current_stock":17, "max_stock":80}]
fruitproducts = {0:fruits_section[0],1:fruits_section[1],4:fruits_section[2],5:fruits_section[3],8:fruits_section[4],9:fruits_section[5],12:fruits_section[6],13:fruits_section[7],16:fruits_section[8],17:fruits_section[9],20:' '}
fruitcart = []

snacks_section = [{"name":"Oreo's", "price":2.50, "current_stock":68, "max_stock":90},
{"name":"Berry Roll-Up", "price":2.50, "current_stock":42, "max_stock":85},
{"name":"Pretzels", "price":2.50, "current_stock":38, "max_stock":64},
{"name":"Shapes", "price":2.50, "current_stock":46, "max_stock":75},
{"name":"Cookies", "price":2.50, "current_stock":32, "max_stock":90},
{"name":"Popcorn", "price":2.50, "current_stock":46, "max_stock":47},
{"name":"CC's", "price":2.50, "current_stock":26, "max_stock":38},
{"name":"Jelly Cup", "price":2.50, "current_stock":75, "max_stock":85},
{"name":"Tim Tam", "price":2.50, "current_stock":46, "max_stock":76},
{"name":"Doritos", "price":2.50, "current_stock":28, "max_stock":89}]
snackproducts = {0:snacks_section[0],1:snacks_section[1],4:snacks_section[2],5:snacks_section[3],8:snacks_section[4],9:snacks_section[5],12:snacks_section[6],13:snacks_section[7],16:snacks_section[8],17:snacks_section[9],20:' '}
snackcart = []

drinks_section = [{"name":"Creaming Soda", "price":1.80,'size':"1.25 L", "current_stock":42, "max_stock":80},
{"name":"Apple Juice", "price":3,'size':"2 L", "current_stock":51, "max_stock":90},
{"name":"Pepsi", "price":2.15,'size':"2 L", "current_stock":68, "max_stock":10},
{"name":"Coca-Cola", "price":1.60,'size':"2 L", "current_stock":48, "max_stock":100},
{"name":"Fanta", "price":1.40,'size':"1.25 L", "current_stock":72, "max_stock":100},
{"name":"Solo", "price":2.35,'size':"1.25 L", "current_stock":94, "max_stock":100},
{"name":"Lemonade", "price":1.85,'size':"1.25 L", "current_stock":32, "max_stock":70},
{"name":"Sarsparilla", "price":1.20,'size':"1.1 L", "current_stock":54, "max_stock":65},
{"name":"Iced Tea", "price":1.20,'size':"1.1 L", "current_stock":38, "max_stock":45},
{"name":"Iced Coffee", "price":1.97,'size':"1 L", "current_stock":27, "max_stock":80}]
drinkproducts = {0:drinks_section[0],1:drinks_section[1],4:drinks_section[2],5:drinks_section[3],8:drinks_section[4],9:drinks_section[5],12:drinks_section[6],13:drinks_section[7],16:drinks_section[8],17:drinks_section[9],20:' '}
drinkcart = []

toiletries_section = [{"name":"Paper Towels", "price":4.40, "current_stock":29, "max_stock":70},
{"name":"Stain Remover", "price":3, "current_stock":51, "max_stock":75},
{"name":"Toothbrush", "price":0.90, "current_stock":68, "max_stock":95},
{"name":"Disinfectant", "price":4.20, "current_stock":48, "max_stock":80},
{"name":"Bleach", "price":3.70, "current_stock":72, "max_stock":100},
{"name":"Soap", "price":1.35, "current_stock":35, "max_stock":68},
{"name":"Toothpaste", "price":1.85,"current_stock":32, "max_stock":70},
{"name":"Air Freshener", "price":4.90, "current_stock":65, "max_stock":84},
{"name":"Sponge", "price":0.70, "current_stock":12, "max_stock":55},
{"name":"Toilet Paper", "price":0.30, "current_stock":0, "max_stock":80}]
toiletriesproducts = {0:toiletries_section[0],1:toiletries_section[1],4:toiletries_section[2],5:toiletries_section[3],8:toiletries_section[4],9:toiletries_section[5],12:toiletries_section[6],13:toiletries_section[7],16:toiletries_section[8],17:toiletries_section[9],20:' '}
toiletriescart = []
finalcart = [' ',]
finalcart2 = []
editscart1 = []
editscart2 = []
editscart3 = []
editscart4 = []
editscart5 = []
pricecart = [' ',]
amountcart = [' ',]
cartnum = 0
cartnum2 = 0
number_for_cart = 1
total = 0
item_chosen = False
payed = 0
giftcartdone = False

#runs window 2
while window1 == False:
    window.close()
    layout2 = [[sg.Text(' Coles Self-Checkout', size=(20, 1), background_color=Title_colour, justification='center', font=("Helvetica", 25))],
                [sg.Text((person_name), font=("Arial", 12))],
                [sg.Text('_' * 100, size=(47, 1))],
                [sg.Button("Fruits"), sg.Button("Drinks"), sg.Button("Snacks"), sg.Button("Toiletries")],
                [sg.Text('_' * 100, size=(47, 1))],
                [sg.Button("Checkout"),sg.Button('Cart'),sg.Button('Exit')]
               ]
    #layout for fruits window
    fruits = [[sg.Text('Fruits', size=(25, 1), background_color=Title_colour, justification='center', font=("Helvetica", 25))],
              [sg.Text('_' * 100, size=(59, 1))],
              [sg.Checkbox(fruits_section[0]['name'] + ' | $' + str(fruits_section[0]['price']) + fruits_section[0]['info'] + ' | Stock:' + str(fruits_section[0]['current_stock']) + '/' + str(fruits_section[0]['max_stock']), size=(27, 1), default=False), sg.Checkbox(fruits_section[1]['name'] + ' | $' + str(fruits_section[1]['price']) + fruits_section[1]['info'] + ' | Stock:' + str(fruits_section[1]['current_stock']) + '/' + str(fruits_section[1]['max_stock']), size=(22, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                 '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(fruits_section[2]['name'] + ' | $' + str(fruits_section[2]['price']) + fruits_section[2]['info'] + ' | Stock:' + str(fruits_section[2]['current_stock']) + '/' + str(fruits_section[2]['max_stock']), size=(27, 1), default=False), sg.Checkbox(fruits_section[3]['name'] + ' | $' + str(fruits_section[3]['price']) + fruits_section[3]['info'] + ' | Stock:' + str(fruits_section[3]['current_stock']) + '/' + str(fruits_section[3]['max_stock']), size=(23, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                 '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(fruits_section[4]['name'] + ' | $' + str(fruits_section[4]['price']) + fruits_section[4]['info'] + ' | Stock:' + str(fruits_section[4]['current_stock']) + '/' + str(fruits_section[4]['max_stock']), size=(27, 1), default=False),sg.Checkbox(fruits_section[5]['name'] + ' | $' + str(fruits_section[5]['price']) + fruits_section[5]['info'] + ' | Stock:' + str(fruits_section[5]['current_stock']) + '/' + str(fruits_section[5]['max_stock']), size=(27, 1),default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                  '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(fruits_section[6]['name'] + ' | $' + str(fruits_section[6]['price']) + fruits_section[6]['info'] + ' | Stock:' + str(fruits_section[6]['current_stock']) + '/' + str(fruits_section[6]['max_stock']), size=(27, 1), default=False), sg.Checkbox(fruits_section[7]['name'] + ' | $' + str(fruits_section[7]['price']) + fruits_section[7]['info'] + ' | Stock:' + str(fruits_section[7]['current_stock']) + '/' + str(fruits_section[7]['max_stock']), size=(22, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                 '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(fruits_section[8]['name'] + ' | $' + str(fruits_section[8]['price']) + fruits_section[8]['info'] + ' | Stock:' + str(fruits_section[8]['current_stock']) + '/' + str(fruits_section[8]['max_stock']), size=(27, 1), default=False), sg.Checkbox(fruits_section[9]['name'] + ' | $' + str(fruits_section[9]['price']) + fruits_section[9]['info'] + ' | Stock:' + str(fruits_section[9]['current_stock']) + '/' + str(fruits_section[9]['max_stock']), size=(23, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                 '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text('_' * 100, size=(59, 1))],
              [sg.Button('Done'), sg.Button('Exit')]
              ]
    #layout for drinks window
    drinks = [[sg.Text('Drinks', size=(26, 1), background_color=Title_colour, justification='center', font=("Helvetica", 25))],
              [sg.Text('_' * 100, size=(61, 1))],
              [sg.Checkbox(drinks_section[0]['name'] + ' | $' + str(drinks_section[0]['price']) + ' | Stock:' + str(drinks_section[0]['current_stock']) + '/' + str(drinks_section[0]['max_stock']), size=(27, 1), default=False), sg.Checkbox(drinks_section[1]['name'] + ' | $' + str(drinks_section[1]['price']) + ' | Stock:' + str(drinks_section[1]['current_stock']) + '/' + str(drinks_section[1]['max_stock']), size=(25, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text(' '+drinks_section[0]['size']),sg.Text('                    '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text(' '+drinks_section[1]['size'])],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(drinks_section[2]['name'] + ' | $' + str(drinks_section[2]['price'])  + ' | Stock:' + str(drinks_section[2]['current_stock']) + '/' + str(drinks_section[2]['max_stock']),size=(27, 1), default=False), sg.Checkbox(drinks_section[3]['name'] + ' | $' + str(drinks_section[3]['price']) + ' | Stock:' + str(drinks_section[3]['current_stock']) + '/' + str(drinks_section[3]['max_stock']), size=(23, 1),default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text(' '+drinks_section[2]['size']),sg.Text('                        '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text(' '+drinks_section[3]['size'])],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(drinks_section[8]['name'] + ' | $' + str(drinks_section[8]['price']) + ' | Stock:' + str(drinks_section[8]['current_stock']) + '/' + str(drinks_section[8]['max_stock']), size=(27, 1), default=False), sg.Checkbox(drinks_section[5]['name'] + ' | $' + str(drinks_section[5]['price']) + ' | Stock:' + str(drinks_section[5]['current_stock']) + '/' + str(drinks_section[5]['max_stock']), size=(27, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text(' '+drinks_section[8]['size']),sg.Text('                      '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text(' '+drinks_section[5]['size'])],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(drinks_section[6]['name'] + ' | $' + str(drinks_section[6]['price']) + ' | Stock:' + str(drinks_section[6]['current_stock']) + '/' + str(drinks_section[6]['max_stock']), size=(27, 1), default=False), sg.Checkbox(drinks_section[7]['name'] + ' | $' + str(drinks_section[7]['price']) + ' | Stock:' + str(drinks_section[7]['current_stock']) + '/' + str(drinks_section[7]['max_stock']), size=(22, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text(' '+drinks_section[6]['size']),sg.Text('                    '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text(' '+drinks_section[7]['size'])],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(drinks_section[4]['name'] + ' | $' + str(drinks_section[4]['price']) + ' | Stock:' + str(drinks_section[4]['current_stock']) + '/' + str(drinks_section[4]['max_stock']), size=(27, 1), default=False), sg.Checkbox(drinks_section[9]['name'] + ' | $' + str(drinks_section[9]['price']) + ' | Stock:' + str(drinks_section[9]['current_stock']) + '/' + str(drinks_section[9]['max_stock']), size=(23, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text(' '+drinks_section[4]['size']),sg.Text('                    '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text(' '+drinks_section[9]['size'])],
              [sg.Text('_' * 100, size=(61, 1))],
              [sg.Button('Done'), sg.Button('Exit')]]

    #layout for snacks window
    snacks = [[sg.Text('Snacks', size=(25, 1), background_color=Title_colour, justification='center', font=("Helvetica", 25))],
              [sg.Text('_' * 100, size=(59, 1))],
              [sg.Checkbox(snacks_section[0]['name'] + ' | $' + str(snacks_section[0]['price']) + ' | Stock:' + str(snacks_section[0]['current_stock']) + '/' + str(snacks_section[0]['max_stock']), size=(27, 1), default=False), sg.Checkbox(snacks_section[2]['name'] + ' | $' + str(snacks_section[2]['price']) + ' | Stock:' + str(snacks_section[2]['current_stock']) + '/' + str(snacks_section[2]['max_stock']), size=(22, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                 '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(snacks_section[1]['name'] + ' | $' + str(snacks_section[1]['price']) + ' | Stock:' + str(snacks_section[1]['current_stock']) + '/' + str(snacks_section[1]['max_stock']), size=(27, 1), default=False), sg.Checkbox(snacks_section[3]['name'] + ' | $' + str(snacks_section[3]['price']) + ' | Stock:' + str(snacks_section[3]['current_stock']) + '/' + str(snacks_section[3]['max_stock']), size=(23, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                 '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(snacks_section[4]['name'] + ' | $' + str(snacks_section[4]['price']) +' | Stock:' + str(snacks_section[4]['current_stock']) + '/' + str(snacks_section[4]['max_stock']), size=(27, 1), default=False),sg.Checkbox(snacks_section[5]['name'] + ' | $' + str(snacks_section[5]['price']) + ' | Stock:' + str(snacks_section[5]['current_stock']) + '/' + str(snacks_section[5]['max_stock']), size=(27, 1),default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True, default_value=0),sg.Text('                                  '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(snacks_section[6]['name'] + ' | $' + str(snacks_section[6]['price']) + ' | Stock:' + str(snacks_section[6]['current_stock']) + '/' + str(snacks_section[6]['max_stock']), size=(27, 1), default=False), sg.Checkbox(snacks_section[7]['name'] + ' | $' + str(snacks_section[7]['price']) + ' | Stock:' + str(snacks_section[7]['current_stock']) + '/' + str(snacks_section[7]['max_stock']), size=(22, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                 '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(snacks_section[8]['name'] + ' | $' + str(snacks_section[8]['price']) + ' | Stock:' + str(snacks_section[8]['current_stock']) + '/' + str(snacks_section[8]['max_stock']), size=(27, 1), default=False), sg.Checkbox(snacks_section[9]['name'] + ' | $' + str(snacks_section[9]['price']) +  ' | Stock:' + str(snacks_section[9]['current_stock']) + '/' + str(snacks_section[9]['max_stock']), size=(23, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                 '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text('_' * 100, size=(59, 1))],
              [sg.Button('Done'), sg.Button('Exit')]]

    #layout for toiletry window
    toiletries = [[sg.Text('Toiletries', size=(25, 1), background_color=Title_colour, justification='center', font=("Helvetica", 25))],
              [sg.Text('_' * 100, size=(60, 1))],
              [sg.Checkbox(toiletries_section[0]['name'] + ' | $' + str(toiletries_section[0]['price']) + ' | Stock:' + str(toiletries_section[0]['current_stock']) + '/' + str(toiletries_section[0]['max_stock']), size=(27, 1), default=False), sg.Checkbox(toiletries_section[1]['name'] + ' | $' + str(toiletries_section[1]['price']) + ' | Stock:' + str(toiletries_section[1]['current_stock']) + '/' + str(toiletries_section[1]['max_stock']), size=(24, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                 '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(toiletries_section[2]['name'] + ' | $' + str(toiletries_section[2]['price']) + ' | Stock:' + str(toiletries_section[2]['current_stock']) + '/' + str(toiletries_section[2]['max_stock']), size=(27, 1), default=False), sg.Checkbox(toiletries_section[3]['name'] + ' | $' + str(toiletries_section[3]['price']) + ' | Stock:' + str(toiletries_section[3]['current_stock']) + '/' + str(toiletries_section[3]['max_stock']), size=(24, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                 '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(toiletries_section[4]['name'] + ' | $' + str(toiletries_section[4]['price']) +' | Stock:' + str(toiletries_section[4]['current_stock']) + '/' + str(toiletries_section[4]['max_stock']), size=(27, 1), default=False),sg.Checkbox(toiletries_section[5]['name'] + ' | $' + str(toiletries_section[5]['price']) + ' | Stock:' + str(toiletries_section[5]['current_stock']) + '/' + str(toiletries_section[5]['max_stock']), size=(27, 1),default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True, default_value=0),sg.Text('                                  '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(toiletries_section[6]['name'] + ' | $' + str(toiletries_section[6]['price']) + ' | Stock:' + str(toiletries_section[6]['current_stock']) + '/' + str(toiletries_section[6]['max_stock']), size=(27, 1), default=False), sg.Checkbox(toiletries_section[7]['name'] + ' | $' + str(toiletries_section[7]['price']) + ' | Stock:' + str(toiletries_section[7]['current_stock']) + '/' + str(toiletries_section[7]['max_stock']), size=(24, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                 '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text((" "), font=("Arial", 2))],
              [sg.Checkbox(toiletries_section[8]['name'] + ' | $' + str(toiletries_section[8]['price']) + ' | Stock:' + str(toiletries_section[8]['current_stock']) + '/' + str(toiletries_section[8]['max_stock']), size=(27, 1), default=False), sg.Checkbox(toiletries_section[9]['name'] + ' | $' + str(toiletries_section[9]['price']) +  ' | Stock:' + str(toiletries_section[9]['current_stock']) + '/' + str(toiletries_section[9]['max_stock']), size=(24, 1), default=False)],
              [sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0),sg.Text('                                 '), sg.Text('Amount:', size=(6, 1)),sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=0)],
              [sg.Text('_' * 100, size=(60, 1))],
              [sg.Button('Done'), sg.Button('Exit')]]


    cart_layout = [[sg.Text(' Shopping Cart', size=(20, 1), background_color=Title_colour, justification='center', font=("Helvetica", 25))],
                   [sg.Text((person_name), font=("Arial", 12)),sg.Text('                                                        '+str(cartnum)+' Items', font=("Helvetica", 12))],
                   [sg.Text('-' * 100, size=(47, 1))],
                   [sg.Text(finalcart2,size=(47,number_for_cart))],
                   [sg.Button('Edit Cart')],
                   [sg.Text('-' * 100, size=(47, 1))],
                   [sg.Text('Total: $'+str(round(total, 2)),font=("Helvetica", 12))],
                   [sg.Text('_' * 100, size=(47, 1))],
                   [sg.Button('Done'), sg.Button('Exit')]]

    window2 = sg.Window("Coles | Self-Checkout").Layout(layout2)
    window3 = sg.Window("Fruits").Layout(fruits)
    window4 = sg.Window("Drinks").Layout(drinks)
    window5 = sg.Window("Snacks").Layout(snacks)
    window6 = sg.Window("Toiletries").Layout(toiletries)
    shopping_cart = sg.Window("Shopping Cart").Layout(cart_layout)
    event, values = window2.Read()
    if event == 'Fruits':
        fruitsw = True
        window2.hide()
        event, values = window3.Read()
        while fruitsw == True:
            if event == 'Done':
                count = 0
                count2 = 2
                done = False
                finish = False
                while done == False:
                    if values[count] == True:
                        if int(values[count2]) > int(fruitproducts[count2 - 2]['current_stock']):
                            count = False
                            count2 = False
                            sg.popup_ok('Your current selection exceeds our stock, please revise your chosen items accordingly.')
                            finish = False
                            done = True
                        else:
                            if int(values[count2]) > 0:
                                fruitcart.append(fruitproducts[count]['name']+' x'+values[count2])
                                item_chosen = True
                                total = total + (float(fruitproducts[count]['price'])*float(values[count2]))
                                finalcart.append(fruitproducts[count]['name'])
                                finalcart2.append(fruitproducts[count]['name'] + ' x' + values[count2])
                                pricecart.append(fruitproducts[count]['price'])
                                editscart3.append(fruitproducts[count]['price'])
                                editscart2.append(values[count2])
                                editscart1.append(fruitproducts[count]['name'])
                                editscart5.append(fruitproducts[count]['current_stock'])
                                amountcart.append(values[count2])
                                fruitproducts[count]['current_stock'] = fruitproducts[count]['current_stock'] - int(values[count2])
                                cartnum = cartnum + 1
                                cartnum2 = cartnum2 + 1
                        if (count % 2) == 0:
                            count = count + 1
                        else:
                            count = count + 3
                        if count > 17:
                            done = True
                            finish = True
                        if (count2 % 2) == 0:
                            count2 = count2 + 1
                        else:
                            count2 = count2 + 3
                        if count2 > 19:
                            done = True
                            finish = True
                    elif values[count] == False:
                        if int(values[count2]) > int(fruitproducts[count2 - 2]['current_stock']):
                            count = False
                            count2 = False
                            sg.popup_ok('Your current selection exceeds our stock, please revise your chosen items accordingly.')
                            finish = False
                            done = True
                        if (count % 2) == 0:
                            count = count + 1
                        else:
                            count = count + 3
                        if count == 20:
                            done = True
                            finish = True
                        if (count2 % 2) == 0:
                            count2 = count2 + 1
                        else:
                            count2 = count2 + 3
                        if count2 > 19:
                            done = True
                            finish = True
                if finish == True:
                    if fruitcart == []:
                        sg.popup_ok('No Items have been added to the cart')
                    else:
                        sg.popup_ok('Items added to cart: ', fruitcart)
                        number_for_cart = number_for_cart + 1
                window3.hide()
                window2.un_hide()
                window2.hide()
                fruitsw = False
            elif event == 'Exit':
                answer = sg.popup_yes_no('Are you sure you want to exit?')
                if answer == "Yes":
                    window3.close()
                    window2.close()
                    window.close()
                    window1 = True
                    break
                if answer == "No":
                    event, values = window3.Read()
                    window2.hide()
    elif event == 'Drinks':
        drinksw = True
        window2.hide()
        event, values = window4.Read()
        while drinksw == True:
            if event == 'Done':
                count = 0
                count2 = 2
                done = False
                finish = False
                while done == False:
                    if values[count] == True:
                        if int(values[count2]) > int(drinkproducts[count2 - 2]['current_stock']):
                            count = False
                            count2 = False
                            sg.popup_ok('Your current selection exceeds our stock, please revise your chosen items accordingly.')
                            finish = False
                            done = True
                        else:
                            if int(values[count2]) > 0:
                                drinkcart.append(drinkproducts[count]['name'] + ' x' + values[count2])
                                item_chosen = True
                                total = total + (float(drinkproducts[count]['price']) * float(values[count2]))
                                finalcart.append(drinkproducts[count]['name'])
                                finalcart2.append(drinkproducts[count]['name'] + ' x' + values[count2])
                                pricecart.append(drinkproducts[count]['price'])
                                amountcart.append(values[count2])
                                editscart3.append(drinkproducts[count]['price'])
                                editscart2.append(values[count2])
                                editscart1.append(drinkproducts[count]['name'])
                                editscart5.append(drinkproducts[count]['current_stock'])
                                drinkproducts[count]['current_stock'] = drinkproducts[count]['current_stock'] - int(values[count2])
                                cartnum = cartnum + 1
                                cartnum2 = cartnum2 + 1
                        if (count % 2) == 0:
                            count = count + 1
                        else:
                            count = count + 3
                        if count > 17:
                            done = True
                            finish = True
                        if (count2 % 2) == 0:
                            count2 = count2 + 1
                        else:
                            count2 = count2 + 3
                        if count2 > 19:
                            done = True
                            finish = True
                    elif values[count] == False:
                        if int(values[count2]) > int(drinkproducts[count2 - 2]['current_stock']):
                            count = False
                            count2 = False
                            sg.popup_ok('Your current selection exceeds our stock, please revise your chosen items accordingly.')
                            finish = False
                            done = True
                        if (count % 2) == 0:
                            count = count + 1
                        else:
                            count = count + 3
                        if count == 20:
                            done = True
                            finish = True
                        if (count2 % 2) == 0:
                            count2 = count2 + 1
                        else:
                            count2 = count2 + 3
                        if count2 > 19:
                            done = True
                            finish = True
                if finish == True:
                    if drinkcart == []:
                        sg.popup_ok('No Items have been added to the cart')
                    else:
                        sg.popup_ok('Items added to cart: ', drinkcart)
                        number_for_cart = number_for_cart + 1
                window4.hide()
                window2.un_hide()
                window2.hide()
                drinksw = False
            elif event == 'Exit':
                answer = sg.popup_yes_no('Are you sure you want to exit?')
                if answer == "Yes":
                    window4.close()
                    window2.close()
                    window.close()
                    window1 = True
                    break
                if answer == "No":
                    event, values = window4.Read()
                    window2.hide()
    elif event == 'Snacks':
        snacksw = True
        window2.hide()
        event, values = window5.Read()
        while snacksw == True:
            if event == 'Done':
                count5 = 0
                count6 = 2
                done = False
                finish = False
                while done == False:
                    if values[count5] == True:
                        if int(values[count6]) > int(snackproducts[count6 - 2]['current_stock']):
                            count5 = False
                            count6 = False
                            sg.popup_ok(
                                'Your current selection exceeds our stock, please revise your chosen items accordingly.')
                            finish = False
                            done = True
                        else:
                            if int(values[count6]) > 0:
                                snackcart.append(snackproducts[count5]['name'] + ' x' + values[count6])
                                item_chosen = True
                                total = total + (int(snackproducts[count5]['price']) * int(values[count6]))
                                finalcart.append(snackproducts[count5]['name'])
                                finalcart2.append(snackproducts[count5]['name'] + ' x' + values[count6])
                                pricecart.append(snackproducts[count5]['price'])
                                amountcart.append(values[count6])
                                editscart3.append(snackproducts[count5]['price'])
                                editscart2.append(values[count6])
                                editscart1.append(snackproducts[count5]['name'])
                                editscart5.append(snackproducts[count5]['current_stock'])
                                snackproducts[count5]['current_stock'] = snackproducts[count5]['current_stock'] - int(values[count6])
                                cartnum = cartnum + 1
                                cartnum2 = cartnum2 + 1
                        if (count5 % 2) == 0:
                            count5 = count5 + 1
                        else:
                            count5 = count5 + 3
                        if count5 > 17:
                            done = True
                            finish = True
                        if (count6 % 2) == 0:
                            count6 = count6 + 1
                        else:
                            count6 = count6 + 3
                        if count6 > 19:
                            done = True
                            finish = True
                    elif values[count5] == False:
                        if int(values[count6]) > int(snackproducts[count6 - 2]['current_stock']):
                            count5 = False
                            count6 = False
                            sg.popup_ok('Your current selection exceeds our stock, please revise your chosen items accordingly.')
                            finish = False
                            done = True
                        if (count5 % 2) == 0:
                            count5 = count5 + 1
                        else:
                            count5 = count5 + 3
                        if count5 == 20:
                            done = True
                            finish = True
                        if (count6 % 2) == 0:
                            count6 = count6 + 1
                        else:
                            count6 = count6 + 3
                        if count6 > 19:
                            done = True
                            finish = True
                if finish == True:
                    if snackcart == []:
                        sg.popup_ok('No Items have been added to the cart')
                    else:
                        sg.popup_ok('Items added to cart: ', snackcart)
                        number_for_cart = number_for_cart + 1
                window5.hide()
                window2.un_hide()
                window2.hide()
                snacksw = False
            elif event == 'Exit':
                answer = sg.popup_yes_no('Are you sure you want to exit?')
                if answer == "Yes":
                    window5.close()
                    window2.close()
                    window.close()
                    window1 = True
                    break
                if answer == "No":
                    event, values = window5.Read()
                    window2.hide()
    elif event == 'Toiletries':
        toiletryw = True
        window2.hide()
        event, values = window6.Read()
        while toiletryw == True:
            if event == 'Done':
                count = 0
                count2 = 2
                done = False
                finish = False
                while done == False:
                    if values[count] == True:
                        if int(values[count2]) > int(toiletriesproducts[count2 - 2]['current_stock']):
                            count = False
                            count2 = False
                            sg.popup_ok('Your current selection exceeds our stock, please revise your chosen items accordingly.')
                            finish = False
                            done = True
                        else:
                            if int(values[count2]) > 0:
                                toiletriescart.append(toiletriesproducts[count]['name'] + ' x' + values[count2]+']')
                                item_chosen = True
                                total = total + (float(toiletriesproducts[count]['price']) * float(values[count2]))
                                finalcart.append(toiletriesproducts[count]['name'])
                                finalcart2.append(toiletriesproducts[count]['name'] + ' x' + values[count2])
                                pricecart.append(toiletriesproducts[count]['price'])
                                amountcart.append(values[count2])
                                editscart3.append(toiletriesproducts[count]['price'])
                                editscart2.append(values[count2])
                                editscart1.append(toiletriesproducts[count]['name'])
                                editscart5.append(toiletriesproducts[count]['current_stock'])
                                toiletriesproducts[count]['current_stock'] = toiletriesproducts[count]['current_stock'] - int(values[count2])
                                cartnum = cartnum + 1
                                cartnum2 = cartnum2 + 1
                        if (count % 2) == 0:
                            count = count + 1
                        else:
                            count = count + 3
                        if count > 17:
                            done = True
                            finish = True
                        if (count2 % 2) == 0:
                            count2 = count2 + 1
                        else:
                            count2 = count2 + 3
                        if count2 > 19:
                            done = True
                            finish = True
                    elif values[count] == False:
                        if int(values[count2]) > int(toiletriesproducts[count2 - 2]['current_stock']):
                            count = False
                            count2 = False
                            sg.popup_ok('Your current selection exceeds our stock, please revise your chosen items accordingly.')
                            finish = False
                            done = True
                        if (count % 2) == 0:
                            count = count + 1
                        else:
                            count = count + 3
                        if count == 20:
                            done = True
                            finish = True
                        if (count2 % 2) == 0:
                            count2 = count2 + 1
                        else:
                            count2 = count2 + 3
                        if count2 > 19:
                            done = True
                            finish = True
                if finish == True:
                    if toiletriescart == []:
                        sg.popup_ok('No Items have been added to the cart')
                    else:
                        sg.popup_ok('Items added to cart: ', toiletriescart)
                        number_for_cart = number_for_cart + 1
                window6.hide()
                window2.un_hide()
                window2.hide()
                toiletryw = False
            elif event == 'Exit':
                answer = sg.popup_yes_no('Are you sure you want to exit?')
                if answer == "Yes":
                    window6.close()
                    window2.close()
                    window.close()
                    window1 = True
                    break
                if answer == "No":
                    event, values = window6.Read()
                    window2.hide()
    elif event == 'Cart':
        if finalcart2 == []:
            sg.Popup('Sorry, your cart is currently empty')
            window2.hide()
        else:
            def cart(cartnum):
                return [sg.Text(f'{cartnum}. '), sg.Text(finalcart[cartnum]),sg.Text('| $' + str(round(float(pricecart[cartnum]) * float(amountcart[cartnum]), 2))),sg.Drop(values=(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')), auto_size_text=True,default_value=amountcart[cartnum])]

            edit_cart = [cart(x) for x in range(1, cartnum)] + [[sg.Text(f'{cartnum}. '), sg.Text(finalcart[cartnum]),sg.Text('| $' + str(round(float(pricecart[cartnum]) * float(amountcart[cartnum]), 2))), sg.Drop(values=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), auto_size_text=True,default_value=amountcart[cartnum])]] + [[sg.Button('Save')]]
            editcart = sg.Window("Edit Cart").Layout(edit_cart)
            event, values = shopping_cart.Read()
            if event == "Edit Cart":
                window2.hide()
                finalcart = [' ', ]
                pricecart = [' ', ]
                amountcart = [' ', ]
                finalcart2 = []
                event3, values3 = editcart.Read()
                if event3 == 'Save':
                    count = 0
                    count2 = 0
                    edits_done = False
                    while edits_done == False:
                        if int(values3[count]) < int(editscart5[count-count2]):
                            if int(values3[count]) > 0:
                                finalcart.append(editscart1[count - count2])
                                pricecart.append(editscart3[count - count2])
                                amountcart.append(editscart2[count - count2])
                                finalcart2.append(editscart1[count - count2]+ ' x'+str(values3[count]))
                                editscart1.pop(count - count2)
                                editscart2.pop(count - count2)
                                editscart3.pop(count - count2)
                                count = count + 1
                                count2 = count2 + 1
                            else:
                                sg.popup_ok("['"+editscart1[count - count2]+"']",'Item has been removed from the cart')
                                editscart1.pop(count - count2)
                                editscart2.pop(count - count2)
                                editscart3.pop(count - count2)
                                editscart5.pop(count - count2)
                                count = count + 1
                                count2 = count2 + 1
                                cartnum = cartnum - 1
                            if count == cartnum2:
                                edits_done = True
                                sg.popup_ok('Your cart has been revised')
                                for w in range(1,cartnum+1):
                                    editscart1.append(finalcart[w])
                                    editscart2.append(amountcart[w])
                                    editscart3.append(pricecart[w])
                                cartnum2 = cartnum
                                editcart.hide()
                                shopping_cart.hide()
                                break
                        else:
                            editscart1.pop(count - count2)
                            editscart2.pop(count - count2)
                            editscart3.pop(count - count2)
                            editscart5.pop(count - count2)
                            count = count + 1
                            count2 = count2 + 1
                            cartnum = cartnum - 1
                            sg.popup_ok('Your selection exceeds our current stock',
                                        'we have consequently removed the product from your cart')

                elif event3 == 'Exit':
                    answer = sg.popup_yes_no('Are you sure you want to exit?')
                    if answer == "Yes":
                        edit_cart.close()
                        shopping_cart.close()
                        window2.close()
                        window.close()
                        window1 = True
                        break
            elif event == 'Done':
                shopping_cart.hide()
                window2.un_hide()
                window2.hide()
            elif event == 'Exit':
                answer = sg.popup_yes_no('Are you sure you want to exit?')
                if answer == "Yes":
                    shopping_cart.close()
                    window2.close()
                    window.close()
                    window1 = True
                    break
    elif event == 'Exit':
        answer = sg.popup_yes_no('Are you sure you want to exit?')
        if answer == "Yes":
            window.close()
            break
        elif answer == 'No':
            window2.hide()
    elif event == 'Checkout':
        if item_chosen == False:
            sg.popup_ok('You cannot continue to checkout until', 'you have added items to your cart')
            window2.hide()
        else:
            window2.hide()
            payment = [[sg.Text(' Payment Methods', size=(17, 1), background_color=Title_colour, justification='center', font=("Helvetica", 25))],
                   [sg.Text('-' * 100, size=(42, 1))],
                   [sg.Button('Cash'),sg.Button('Card'),sg.Button('Gift Card')],
                   [sg.Text('-' * 100, size=(42, 1))],
                   [sg.Text('Total: $'+str(round(total, 2)),key='tota',font=("Helvetica", 12))],
                   [sg.Text('_' * 100, size=(42, 1))],
                   [sg.Button('Go Back')]]
            frame_layout = [
                [sg.Text('Shop Receipt', justification='center', size=(17, 1), font=("Helvetica", 25))],
                [sg.Text('.' * 100, size=(39, 1))],
                [sg.Text(finalcart2,size=(37,number_for_cart+1))],
                [sg.Text('.' * 100, size=(39, 1))],
                [sg.Text('Total: $' + str(round(total,2)), font=("Helvetica", 12))], ]
            finishing = [[sg.Text(' Payment Completed', size=(18, 1), background_color=Title_colour, justification='center', font=("Helvetica", 25))],
                   [sg.Text('-' * 100, size=(42, 1))],
                   [sg.Text('Your payment has been processed', font=("Helvetica", 12))],
                    [sg.Text(' ',font=("Helvetica", 2))],
                   [sg.Frame('Reciept ', frame_layout)],
                   [sg.Button('Exit')]]

            paying = True
            finished_window = sg.Window("Thank you for your Payment").Layout(finishing)
            paymentw = sg.Window("Payment Methods").Layout(payment)
            while paying == True:
                event3, values3 = paymentw.read()
                if event3 == 'Go Back':
                    paymentw.hide()
                    window2.un_hide()
                elif event3 == 'Cash':
                    paymentw.hide()
                    cash = [[sg.Text(' Pay with Cash', size=(17, 1), background_color=Title_colour,justification='center', font=("Helvetica", 25))],
                               [sg.Text('-' * 100, size=(40, 1))],
                               [sg.Button('$0.05'), sg.Button('$0.10'), sg.Button('$0.20'), sg.Button('$0.50'), sg.Button('$1.00')],
                               [sg.Button('$10.00'), sg.Button('$20.00'), sg.Button('$50.00'), sg.Button('$100.00')],
                               [sg.Text('-' * 100, size=(40, 1))],
                               [sg.Text('Amount Payed: $' + str(payed),key='pay',size=(30,1), font=("Helvetica", 12))],
                               [sg.Text('Total: $' + str(round(total, 2)), font=("Helvetica", 12))],
                               [sg.Text('_' * 100, size=(40, 1))],
                               [sg.Button('Go Back'),sg.Button('Done')]]
                    cashw = sg.Window("Pay with Cash").Layout(cash)
                    event2, values2 = cashw.read()
                    finished = False
                    while finished == False:
                        if event2 == 'Done':
                            if payed >= total:
                                finished = True
                                total_ = float(payed) - float(total)
                                sg.popup_ok('Please collect your change',"['$"+str(round(total_, 2))+"']")
                                cashw.hide()
                                event, values = finished_window.read()
                                if event == "Exit":
                                    sg.popup_ok('Thank you for shopping at Coles!')
                                    finished_window.close()
                                    shopping_cart.close()
                                    window2.close()
                                    window.close()
                                    window1 = True
                                    finished = True
                                    paying = False
                                    break
                            else:
                                sg.popup_ok('Your payment does not', 'suffice the total amount due!')
                                event2, values2 = cashw.read()
                        elif event2 == 'Go Back':
                            cashw.hide()
                            finished = True
                            paymentw.un_hide()
                            break
                        elif event2 == '$0.05':
                            payed = payed + 0.05
                            cashw['pay'].update('Amount Payed: $'+str(round(payed, 2)))
                            event2, values2 = cashw.read()
                        elif event2 == '$0.10':
                            payed = payed + 0.10
                            cashw['pay'].update('Amount Payed: $' + str(round(payed, 2)))
                            event2, values2 = cashw.read()
                        elif event2 == '$0.20':
                            payed = payed + 0.20
                            cashw['pay'].update('Amount Payed: $' + str(round(payed, 2)))
                            event2, values2 = cashw.read()
                        elif event2 == '$0.50':
                            payed = payed + 0.50
                            cashw['pay'].update('Amount Payed: $' + str(round(payed, 2)))
                            event2, values2 = cashw.read()
                        elif event2 == '$1.00':
                            payed = payed + 1
                            cashw['pay'].update('Amount Payed: $'+ str(round(payed, 2)))
                            event2, values2 = cashw.read()
                        elif event2 == '$10.00':
                            payed = payed + 10
                            cashw['pay'].update('Amount Payed: $'+ str(round(payed, 2)))
                            event2, values2 = cashw.read()
                        elif event2 == '$20.00':
                            payed = payed + 20
                            cashw['pay'].update('Amount Payed: $'+ str(round(payed, 2)))
                            event2, values2 = cashw.read()
                        elif event2 == '$50.00':
                            payed = payed + 50
                            cashw['pay'].update('Amount Payed: $'+ str(round(payed, 2)))
                            event2, values2 = cashw.read()
                        elif event2 == '$100.00':
                            payed = payed + 100
                            cashw['pay'].update('Amount Payed: $'+ str(round(payed, 2)))
                            event2, values2 = cashw.read()
                elif event3 == 'Card':
                    cardpay = True
                    paymentw.hide()
                    card = [[sg.Text(' Pay with Card', size=(20, 1), background_color=Title_colour,
                                     justification='center', font=("Helvetica", 25))],
                            [sg.Text('-' * 100, size=(48, 1))],
                            [sg.Text('Card Number: (16 Digits - 4 each)'),sg.Text('    Expiry Date: (MM/YY)')],
                            [sg.InputText(size=(5,1)),sg.InputText(size=(5,1)),sg.InputText(size=(5,1)),sg.InputText(size=(5,1)),sg.Text('  |  '),sg.InputText(size=(2,1)),sg.Text('/'),sg.InputText(size=(2,1))],
                            [sg.Text('CVV: (3 Digits)'),sg.Text('   Name on Card:')],
                            [sg.InputText(size=(4, 1)),sg.Text('       |       '),sg.InputText(size=(35, 1))],
                            [sg.Text('-' * 100, size=(48, 1))],
                            [sg.Text('Total: $' + str(round(total, 2)), font=("Helvetica", 12))],
                            [sg.Text('_' * 100, size=(48, 1))],
                            [sg.Button('Go Back'), sg.Button('Done')]]
                    cardw = sg.Window("Pay with Card").Layout(card)
                    while cardpay == True:
                        event2, values2 = cardw.read()
                        finished = False
                        while finished == False:
                            if event2 == 'Go Back':
                                cardw.hide()
                                finished = True
                                cardpay = False
                                paymentw.un_hide()
                                break
                            elif event2 == 'Done':
                                numberr = 0
                                for l in range(0,4):
                                    if len(values2[l]) == 4:
                                        numberr = numberr + 1
                                    else:
                                        numberr = numberr + 0
                                for l in range(4,6):
                                    if len(values2[l]) == 2:
                                        numberr = numberr + 1
                                    else:
                                        numberr = numberr + 0
                                if len(values2[6]) == 3:
                                    numberr = numberr + 1
                                else:
                                    numberr = numberr + 0
                                if len(values2[7]) > 0:
                                    numberr = numberr + 1
                                else:
                                    numberr = numberr + 0
                                if numberr < 8:
                                    sg.popup_ok('Sorry, your entered details are not valid.', 'Please try again')
                                    break
                                else:
                                    cardw.hide()
                                    event, values = finished_window.read()
                                    if event == "Exit":
                                        sg.popup_ok('Thank you for shopping at Coles!')
                                        finished_window.close()
                                        shopping_cart.close()
                                        window2.close()
                                        window.close()
                                        window1 = True
                                        finished = True
                                        paying = False
                                        cardpay = False
                                        break
                elif event3 == 'Gift Card':
                    if giftcartdone == True:
                        sg.popup_ok('You have already used a gift card')
                    else:
                        giftcardpay = True
                        paymentw.hide()
                        giftcard = [[sg.Text(' Pay with Gift Card', size=(20, 1), background_color=Title_colour,justification='center', font=("Helvetica", 25))],
                                [sg.Text('-' * 100, size=(48, 1))],
                                [sg.Text('Gift Card Code: (15 Digits - 4 / 6 / 5)')],
                                [sg.InputText(size=(5, 1)),sg.Text('-'), sg.InputText(size=(7, 1)),sg.Text('-'), sg.InputText(size=(6, 1))],
                                [sg.Text('Example: AB12 -- CD3EFG - H4IJ5', font=("Helvetica", 8))],
                                [sg.Text('-' * 100, size=(48, 1))],
                                [sg.Text('Total: $' + str(round(total, 2)), font=("Helvetica", 12))],
                                [sg.Text('_' * 100, size=(48, 1))],
                                [sg.Button('Go Back'), sg.Button('Done')]]
                        giftcardw = sg.Window("Pay with Gift Card").Layout(giftcard)
                        while giftcardpay == True:
                            event2, values2 = giftcardw.read()
                            finished = False
                            while finished == False:
                                if event2 == 'Go Back':
                                    giftcardw.hide()
                                    finished = True
                                    giftcardpay = False
                                    paymentw.un_hide()
                                    break
                                elif event2 == 'Done':
                                    numberr = 0
                                    if len(values2[0]) == 4:
                                        if str(values2[0]) == 'HE58':
                                            numberr = numberr + 1
                                    else:
                                        numberr = numberr + 0
                                    if len(values2[1]) == 6:
                                        if str(values2[1]) == 'HE4TSH':
                                            numberr = numberr + 1
                                    else:
                                        numberr = numberr + 0
                                    if len(values2[2]) == 5:
                                        if str(values2[2]) == 'J4JD8':
                                            numberr = numberr + 1
                                    else:
                                        numberr = numberr + 0
                                    if numberr < 3:
                                        sg.popup_ok('Sorry, your entered details are not valid.', 'Please try again')
                                        break
                                    else:
                                        giftcartdone = True
                                        if total <= 20:
                                            balance = 20 - float(total)
                                            sg.popup_ok('Your gift card balance is now',str(round(balance, 2)))
                                            giftcardw.hide()
                                            event, values = finished_window.read()
                                        else:
                                            total = total - 20
                                            sg.popup_ok('Your gift card balance is now $0', 'Your new total is: $'+str(round(total, 2)))
                                            paymentw['tota'].update('Total: $'+str(round(total, 2)),font=("Helvetica", 12))
                                            giftcardw.hide()
                                            finished = True
                                            giftcardpay = False
                                            paymentw.un_hide()
                                            break
                                        if event == "Exit":
                                            sg.popup_ok('Thank you for shopping at Coles!')
                                            finished_window.close()
                                            shopping_cart.close()
                                            window2.close()
                                            window.close()
                                            window1 = True
                                            finished = True
                                            paying = False
                                            cardpay = False
                                            break