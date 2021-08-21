from twilio.rest import Client


def send_sms(message, numbers_to_message):
    try:
        client = Client("ACa50c81216ffe7d6167dadc3c7c0fecd3",
                        "f8809fb1dfb6b9c46ab479f218775f00")

        for number in numbers_to_message:
            client.api.account.messages.create(to="+65" + str(number), from_="+19544510518", body=message)
        return True
    except:
        return False

numbers_to_message = [94884381]
send_sms("Drying process done. Syringes are ready to collect.", numbers_to_message)