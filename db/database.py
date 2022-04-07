import pymongo

class Database:
    def __init__(self, database, collection, dataset=None):
        connectionString = "mongodb+srv://root:root@cluster0.30fhd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        if dataset:
            self.dataset = dataset

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        #self.collection.insert_many(self.dataset)

    def create(self, nome_sensor, valor_sensor, unidade_medida, sensor_alarmado):
        return self.collection.insert_one({
            "nome_sensor": nome_sensor,
            "valor_sensor": valor_sensor,
            "unidade_medida": unidade_medida,
            "sensor_alarmado": sensor_alarmado
        })

    def read(self):
        return self.collection.find({})

    def updateSensor(self, nome_sensor, sensor_alarmado):
        return self.collection.update_one(
            {"nome_sensor": nome_sensor},
            {
                "$set": {
                    "sensor_alarmado": sensor_alarmado
                },
                "$currentDate": {"lastModified": True}
            }
        )

    def updateTemp(self, nome_sensor, valor_sensor):
        return self.collection.update_one(
            {"nome_sensor": nome_sensor},
            {
                "$set": {
                    "valor_sensor": valor_sensor
                },
                "$currentDate": {"lastModified": True}
            }
        )

    def delete(self, nome_sensor):
        return self.collection.delete_one({"nome_sensor": nome_sensor})