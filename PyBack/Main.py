# recommendations/recommendations.py

from concurrent import futures
import random
import os

import grpc

from grpc_core.HandGenerator_pb2 import (
    Races, #enum BookCategory
    Hand, #еще enum
    #message BookRecommendation вложеный в ответ класс
    HandReply, #message RecommendationResponse это ответ
)

import grpc_core.HandGenerator_pb2_grpc as HG_grpc

hand_by_races = {Races.DARK:"DARK", Races.LIGHT:"LIGHT"} #books_by_category

hand_by_dir = {Hand.RIGHT:"RIGHT", Hand.LEFT:"LEFT"} #books_by_author

class HandGeneratorService(
    HG_grpc.HandGeneratorServicer
):
    #здесь отправляю на обработку в нейронку и отправляю ответ обратно
    def GenerateHandDataset(self, request, context):
        if request.race not in hand_by_races:
            context.abort(grpc.StatusCode.NOT_FOUND, "Race not found")
        if request.hand not in hand_by_dir:
            context.abort(grpc.StatusCode.NOT_FOUND, "Hand not found")

        hand_for_races = hand_by_races[request.race]
        hand_for_dir = hand_by_dir[request.hand]
        count = request.count
        
        print(f"race: {hand_for_races}, hand: {hand_for_dir}, count: {count}")
        #где-то тут все в нейронку
        
        #типо получаем ответ от нейронки
        
        file_name = "240_F_85786824_12Vh2Dj32dguiI3Dktb5MFc79pzVhtWZ.png"
        file_path = f"./hand-dataset\\{file_name}"
        with open(file_path, "rb") as image:
            f = image.read()
            b = bytes(f)
            print (b)

        return HandReply(FileName = str(file_name), FileBytes = b)
    
    def GenerateHandDatasetStream(self, request, context):
        if request.race not in hand_by_races:
            context.abort(grpc.StatusCode.NOT_FOUND, "Race not found")
        if request.hand not in hand_by_dir:
            context.abort(grpc.StatusCode.NOT_FOUND, "Race not found")

        hand_for_races = hand_by_races[request.race]
        hand_for_dir = hand_by_dir[request.hand]
        count = request.count
        
        print(f"race: {hand_for_races}, hand: {hand_for_dir}, count: {count}")
        #где-то тут все в нейронку
        
        #типо получаем ответ от нейронки
        files_dir = "./hand-dataset"
        files = os.listdir(files_dir)
        print("Дирректория с картинками: ", files_dir)
        print ("Названия всех файлов: ", files)
        for file_name in files:
            file_path = os.path.join(files_dir, file_name)
            with open(file_path, "rb") as image:
                f = image.read()
                b = bytes(f)
                print ("Файл считан")
            reply = HandReply(FileName = str(file_name), FileBytes = b)
            yield reply
        


def serve():
    print("Starting server on port 50051...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    HG_grpc.add_HandGeneratorServicer_to_server(
        HandGeneratorService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()