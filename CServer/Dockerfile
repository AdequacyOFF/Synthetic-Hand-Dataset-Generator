# Dockerfile for CServer

# Use the base image for .NET 8.0 SDK
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build

# Set the working directory to /src
WORKDIR /src

# Copy the project file and restore dependencies
COPY ["CServer/CServer.csproj", "CServer/"]
RUN dotnet restore "CServer/CServer.csproj"

# Copy the rest of the project files
COPY . .

# Build the project in release mode and output to /app/build
WORKDIR "/src/CServer"
RUN dotnet build "CServer.csproj" -c Release -o /app/build

# Create a new image for the final stage
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final

# Set the working directory to /app
WORKDIR /app

# Copy the published files from the build stage
COPY --from=build /app/build .

# Expose port 5020
EXPOSE 5020

# Set the environment variable for the ASP.NET Core URL
ENV ASPNETCORE_URLS=http://+:5020

# Set the user to 'app'
USER root
RUN chmod -R 777 ./
USER app
# Set the entry point to run the application
ENTRYPOINT ["dotnet", "CServer.dll"]

