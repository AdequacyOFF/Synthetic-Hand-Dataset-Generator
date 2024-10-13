using CServer;
using GrpcHandGeneratorClient;

Console.WriteLine("SHD was started");
    string grcpAdress = "http://localhost:50051"; // replace with your gRPC server address
    Console.WriteLine("Please enter path to save dataset, if not exist, it will be created:");
    string datasetPath = Console.ReadLine();
    if (!Directory.Exists(datasetPath) && datasetPath != "")
    {
        Directory.CreateDirectory(datasetPath);
    }
while (true)
{
    Console.WriteLine("What count of hands do you want to generate?");
    int inCount = int.Parse(Console.ReadLine());

    Console.WriteLine("What race do you want to generate hands for? (0-Dark, 1-Light)");
    int inRace = int.Parse(Console.ReadLine());

    Console.WriteLine("What hand do you want to generate hands for? (0-Right, 1-Left)");
    int inHand = int.Parse(Console.ReadLine());

    if (inCount > 0 && Enum.IsDefined(typeof(Hand), inHand) && Enum.IsDefined(typeof(Races), inRace))
    {
        Races race = (Races)inRace;
        Hand hand = (Hand)inHand;
        Console.WriteLine($"Generating {inCount} hands for race {race} and {hand} hand ...");
        HandDatasetHandler handler = new(inCount, race, hand);
        await handler.RequestHandDataset(grcpAdress, false, datasetPath);
        Console.WriteLine("Dataset saved, path: " + datasetPath);
    }
    else
    {
        Console.WriteLine("Invalid request parameters, try again");
        
    }
}
