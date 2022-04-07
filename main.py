import threading
import time
import random
from db.database import Database
from helper.WriteAJson import writeAJson

db = Database(database="bancoiot", collection="sensores")
db.resetDatabase()


def create(nome_sensor, valor_sensor, unidade_medida, sensor_alarmado):
    return db.collection.insert_one({
        "nome_sensor": nome_sensor,
        "valor_sensor": valor_sensor,
        "unidade_medida": unidade_medida,
        "sensor_alarmado": sensor_alarmado
    })


def read():
    sensores = db.collection.find({})
    writeAJson(sensores, "allSensors")


def updateSensor(nome_sensor, sensor_alarmado):
    return db.collection.update_one(
        {"nome_sensor": nome_sensor},
        {
            "$set": {
                "sensor_alarmado": sensor_alarmado
            },
            "$currentDate": {"lastModified": True}
        }
    )


def updateTemp(nome_sensor, valor_sensor):
    return db.collection.update_one(
        {"nome_sensor": nome_sensor},
        {
            "$set": {
                "valor_sensor": valor_sensor
            },
            "$currentDate": {"lastModified": True}
        }
    )


def delete(nome_sensor):
    return db.collection.delete_one({"nome_sensor": nome_sensor})

create("Sensor1", 30, " ºC ", False)
create("Sensor2", 31, " ºC ", False)
create("Sensor3", 32, " ºC ", False)

def simulaTempSensor1(nome_sensor, sensor_alarmado, intervalo):
    flag = True
    while flag:
        temp = random.randrange(30, 41)
        if (30 <= temp <= 38 and sensor_alarmado == False):
            print(nome_sensor, " recebeu um valor de temperatura de: ", temp)
            updateTemp(nome_sensor, temp)
            read()
            time.sleep(intervalo)
        else:
            updateSensor(nome_sensor, True)
            updateTemp(nome_sensor, temp)
            read()
            flag = False
    print("Atenção! Temperatura muito alta! Verificar Sensor 1!")

def simulaTempSensor2(nome_sensor, sensor_alarmado, intervalo):
    flag = True
    while flag:
        temp = random.randrange(30, 41)
        if (30 <= temp <= 38 and sensor_alarmado == False):
            print(nome_sensor, " recebeu um valor de temperatura de: ", temp)
            updateTemp(nome_sensor, temp)
            read()
            time.sleep(intervalo)
        else:
            updateSensor(nome_sensor, True)
            updateTemp(nome_sensor, temp)
            read()
            flag = False
    print("Atenção! Temperatura muito alta! Verificar Sensor 2!")

def simulaTempSensor3(nome_sensor, sensor_alarmado, intervalo):
    flag = True
    while flag:
        temp = random.randrange(30, 41)
        if (30 <= temp <= 38 and sensor_alarmado == False):
            print(nome_sensor, " recebeu um valor de temperatura de: ", temp)
            updateTemp(nome_sensor, temp)
            read()
            time.sleep(intervalo)
        else:
            updateSensor(nome_sensor, True)
            updateTemp(nome_sensor, temp)
            read()
            flag = False
    print("Atenção! Temperatura muito alta! Verificar Sensor 3!")

thread_sensor1 = threading.Thread(target=simulaTempSensor1, args=("Sensor1",False, 2))
thread_sensor2 = threading.Thread(target=simulaTempSensor2, args=("Sensor2",False, 3))
thread_sensor3 = threading.Thread(target=simulaTempSensor3, args=("Sensor3",False, 4))
thread_sensor1.start()
thread_sensor2.start()
thread_sensor3.start()


