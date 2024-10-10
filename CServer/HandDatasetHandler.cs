using System;
using Grpc.Net.Client;
using GrpcHandGeneratorClient;
using System.IO.Compression;
namespace CServer;

class HandDatasetHandler
{
    int count;
    Races race;
    Hand hand;
    private string GeneratedHandDatasetPath = "";
    
    public HandDatasetHandler(int count, Races race, Hand hand)
    {
        if (File.Exists("./archive/handDataset.zip"))
        {
            File.Delete("./archive/handDataset.zip");
        }
        if (!Path.Exists("./generated_hands"))
        {
            Directory.CreateDirectory("./generated_hands");
        }
        if (!Path.Exists("./archive"))
        {
            Directory.CreateDirectory("./archive");
        }
        this.count = count;
        this.race = race;
        this.hand = hand;
    }
    public async Task<string> GetGeneratedHandDataset()
        {
            await RequestHandDataset();
            return GeneratedHandDatasetPath;
        }
    private async Task RequestHandDataset()
    {
        using var channel = GrpcChannel.ForAddress("http://172.18.0.2:50051");
        var client = new HandGenerator.HandGeneratorClient(channel);
        string filesPath = "./generated_hands/";
        var reply = client.GenerateHandDatasetStream(new HandRequest { Count = count, Race = race, Hand = hand });
        var responseStream = reply.ResponseStream;
        while (await responseStream.MoveNext(new CancellationToken()))
        {
            HandReply response = responseStream.Current;
            Console.WriteLine(response.FileName);
            Console.WriteLine(response.FileBytes.Length);
            Console.WriteLine();
            File.WriteAllBytes(filesPath + response.FileName, response.FileBytes.ToArray());
        }
        string targetPath = "./archive/";
        string datasetPath = targetPath + "handDataset.zip";
        ZipFile.CreateFromDirectory(filesPath, datasetPath, CompressionLevel.Optimal, false);
        DirectoryInfo folder = new DirectoryInfo(filesPath);
        foreach (FileInfo file in folder.GetFiles())
        {
            file.Delete(); 
        }
        GeneratedHandDatasetPath = Path.GetFullPath(datasetPath);
    }
}
