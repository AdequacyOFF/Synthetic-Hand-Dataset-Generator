# recommendations/recommendations.py

from concurrent import futures

import grpc

import matplotlib.pyplot as plt
from PalmGenerator.generation import load_model, generate
import os
import io
import gdown
import shutil

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
    HG_grpc.HandGeneratorServicer,
):
    def __init__(self, G):
        self.G = G
    def GenerateHandDataset(self, request, context):
        if request.race not in hand_by_races:
            context.abort(grpc.StatusCode.NOT_FOUND, "Race not found")
        if request.hand not in hand_by_dir:
            context.abort(grpc.StatusCode.NOT_FOUND, "Hand not found")

        hand_for_races = hand_by_races[request.race]
        hand_for_dir = hand_by_dir[request.hand]
        count = request.count
        
        print(f"race: {hand_for_races}, hand: {hand_for_dir}, count: {count}")
        
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
        for i in range(count):
            image = generate(self.G, def_class(data_name=[ hand_for_dir, hand_for_races]), 'cpu')
            buffer = io.BytesIO()
            plt.imsave(buffer, image, format='jpg')
            reply = HandReply(FileName = f'image_{i+1}.jpg', FileBytes = buffer.getvalue())
            yield reply
        
def pthLoad(model_folder_id, local_model_path):
    output = f'{local_model_path}'
    if os.path.exists(output):
        shutil.rmtree(output)
    if not os.path.exists(local_model_path):
        os.makedirs(local_model_path)
    url = f'https://drive.google.com/drive/folders/{model_folder_id}'
    output = f'{local_model_path}'
    gdown.download_folder(url = url,output = output)
    print(f"Downloaded {local_model_path}")
    for file_name in os.listdir(local_model_path):
        if file_name.endswith(".pt"):
            return os.path.join(local_model_path, file_name)

def def_class(data_name):
        ori = data_name[0]
        race = data_name[1]
        
        if ori == 'LEFT' and race == 'LIGHT':
            return 0
        elif ori == 'LEFT' and race == 'DARK':
            return 1
        elif ori == 'RIGHT' and race == 'LIGHT':
            return 2
        else:
            return 3

def serve():
    networkFolderId = "1EREyM3710blxewVpnZulmmZP8EwCX-IS"
    networkModelFolderPath = 'PyBack/PalmGenerator/model'
    G = load_model(pthLoad(networkFolderId, networkModelFolderPath))
    print("Network loaded")
    print("Starting server on port 50051...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    HG_grpc.add_HandGeneratorServicer_to_server(
        HandGeneratorService(G), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started")
    print("Press CTRL+C to stop the server")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()