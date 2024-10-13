using System;
using Grpc.Net.Client;
using GrpcHandGeneratorClient;
using System.IO.Compression;
namespace CServer;

public class HandDatasetHandler
{
    int count;
    Races race;
    Hand hand;
    
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
    public async Task<string> RequestHandDataset(string grcpAdress = "http://localhost:50051",bool CreateZip = true, string filesPath = "./generated_hands/")
    {
        using var channel = GrpcChannel.ForAddress(grcpAdress);
        var client = new HandGenerator.HandGeneratorClient(channel);
        var reply = client.GenerateHandDatasetStream(new HandRequest { Count = count, Race = race, Hand = hand });
        var responseStream = reply.ResponseStream;
        while (await responseStream.MoveNext(new CancellationToken()))
        {
            HandReply response = responseStream.Current;
            Console.WriteLine(response.FileName);
            Console.WriteLine(response.FileBytes.Length);
            File.WriteAllBytes(filesPath + "\\" + response.FileName, response.FileBytes.ToArray());
        }
        if (CreateZip)
        {
            string targetPath = "./archive/";
            string datasetPath = targetPath + "handDataset.zip";
            ZipFile.CreateFromDirectory(filesPath, datasetPath, CompressionLevel.Optimal, false);
            DirectoryInfo folder = new DirectoryInfo(filesPath);
            foreach (FileInfo file in folder.GetFiles())
            {
                file.Delete(); 
            }
            return Path.GetFullPath(datasetPath);
        }
        else
        {
            return filesPath;
        }
    }
}
