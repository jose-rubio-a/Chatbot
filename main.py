import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        a =False
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola, se comunica al Buffet de CUCEI.\n¿En que le puedo ayudar?', ['hola', 'hey', 'buenos', 'buenas', 'tardes', 'dias', 'saludos', 'onda'], single_response = True)
        response('Con mucha hambre, y tu?', ['estas', 'va', 'vas', 'sientes', 'como'], required_words=['como'])
        response('Estamos ubicados en Blvd. Gral. Marcelino García Barragán 1421, Olímpica, 44430 Guadalajara, Jal.', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        response('El horario del Buffet es de lunes a domingo de 11:00 a.m a 10:00 p.m', ['horario', 'hora', 'abren', 'cierran', 'apertura', 'cierre', 'horas'], single_response=True)
        response('Nuestros precios son $150 adultos y $80 niños', ['precio', 'dinero', 'cuanto', 'cuesta', 'precios'], single_response=True)
        response('Nuestro menu incluye una gran variedad de comida:\n- Mexicana: tacos, sopes, burritos, quesadillas, etc.\n-Italiana: risotto, lasaña, spaghetti, pizza, carpaccio, etc.\n-Asiatica: sushi, yakimeshi, teppanyaki, ramen,etc.\n-Postres: flan, pan dulce, nieve, crepas, pay, jericallas, etc :)', ['comida', 'platillos', 'platos', 'menu', 'alimentos', 'incluye', 'incluido', 'comidas', 'incluidos', 'venden', 'vende', 'vendes', 'postre', 'postres'], single_response=True)
        response('Las bebidas vienen incluidas, entre ellas se encuentran refrescos, jugos, cerveza y aguas frescas', ['bebidas', 'beber', 'refrescos', 'tomar', 'agua', 'jugo', 'cerveza'], single_response=True)
        response('Entre semana tenemos 2x1 en buffet de adulto', ['promocion', 'promociones', 'descuento', 'descuentos', 'oferta', 'ofertas', '2x1', '3x2'], single_response=True)
        response('Nuestro restaurante no maneja la opcion de reservar :(', ['reservar', 'reservaciones', 'apartar', 'reservacion', 'mesa'], single_response=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'adios', 'ya', 'vidrios'], single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'No te entendi ¿Puedes repetirlo?'][random.randrange(3)]
    return response

while True:
    print("Buffet CUCEI: " + get_response(input('Cliente: ')))