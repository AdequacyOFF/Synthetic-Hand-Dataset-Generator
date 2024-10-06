
using Grpc.Net.Client;
using GrpcHandGeneratorClient;
using CServer;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.MapPost("/generate-hand-dataset", async (HttpRequest request) =>
{
    var json = await request.ReadFromJsonAsync<WebHandRequest>();
    bool raceIsValid = Enum.IsDefined(typeof(Races), json.race);
    bool handIsValid = Enum.IsDefined(typeof(Hand), json.hand);
    if (json.count > 0 && handIsValid && raceIsValid)
    {
        HandDatasetHandler handler = new(json.count, (Races)Enum.Parse(typeof(Races), json.race), (Hand)Enum.Parse(typeof(Hand), json.hand));
        return Results.Ok(await handler.GetGeneratedHandDataset());
    }
    else
    {
        return Results.BadRequest("Invalid request parameters");
    }
}).WithName("PostGenerateHandDataset")
.WithOpenApi();

app.Run("http://localhost:5020");

record WebHandRequest(int count, string race, string hand);


