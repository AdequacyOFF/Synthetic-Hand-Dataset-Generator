
using GrpcHandGeneratorClient;
using CServer;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddCors(options =>
        {
            // this defines a CORS policy called "default"
            options.AddPolicy("default", policy =>
            {
                policy.WithOrigins("http://localhost:5173")
                    .AllowAnyHeader()
                    .AllowAnyMethod();
            });
        });  
// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();


var app = builder.Build();
app.UseCors("default");
// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.MapPost("/generate-hand-dataset", async (HttpRequest request) =>
{
    var json = await request.ReadFromJsonAsync<WebHandRequest>();
    Console.WriteLine($"Generating {json.count} hands for race {json.race} and hand {json.hand}");
    bool raceIsValid = Enum.IsDefined(typeof(Races), json.race);
    bool handIsValid = Enum.IsDefined(typeof(Hand), json.hand);
    if (json.count > 0 && handIsValid && raceIsValid)
    {
        HandDatasetHandler handler = new(json.count, (Races)Enum.Parse(typeof(Races), json.race), (Hand)Enum.Parse(typeof(Hand), json.hand));
            string datasetPath = await handler.RequestHandDataset();
            await Task.Delay(5000);
            return Results.File(datasetPath);
    }
    else
    {
        return Results.BadRequest("Invalid request parameters");
    }
})
.WithName("PostGenerateHandDataset")
.WithOpenApi();


app.Run("http://0.0.0.0:5020");

record WebHandRequest(int count, string race, string hand);


