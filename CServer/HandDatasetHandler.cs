using System;
using Grpc.Net.Client;
using GrpcHandGeneratorClient;
namespace CServer;

class HandDatasetHandler
{
    int count;
    Races race;
    Hand hand;
    private string GeneratedHandDataset = "";
    
    public HandDatasetHandler(int count, Races race, Hand hand)
    {
        this.count = count;
        this.race = race;
        this.hand = hand;
    }
    public async Task<string> GetGeneratedHandDataset()
        {
            await RequestHandDataset();
            return GeneratedHandDataset;
        }
    private async Task RequestHandDataset()
    {
        using var channel = GrpcChannel.ForAddress("http://localhost:50051");
        var client = new HandGenerator.HandGeneratorClient(channel);
        string filesPath = "C:\\Users\\STOLOWAR\\Desktop\\Git projects\\Synthetic-hand-generator\\CServer\\generated_hands/";
        var reply = client.GenerateHandDatasetStream(new HandRequest { Count = count, Race = race, Hand = hand });
        var responseStream = reply.ResponseStream;
        string logs = "";
        while (await responseStream.MoveNext(new CancellationToken()))
        {
            HandReply response = responseStream.Current;
            Console.WriteLine(response.FileName);
            Console.WriteLine(response.FileBytes.Length);
            Console.WriteLine();
            logs += response.FileName + "\n" + response.FileBytes.Length + "\n\n";
            File.WriteAllBytes(filesPath + response.FileName, response.FileBytes.ToArray());
        }
        GeneratedHandDataset = logs;
    }
}
