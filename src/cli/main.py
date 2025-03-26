import click
import requests
import json
from tabulate import tabulate

@click.command()
@click.argument('city')
@click.option('--format', '-f', type=click.Choice(['text', 'json', 'table']), default='text')
def cli(city: str, format: str):
    """Weather CLI - Get weather information for any city"""
    API_KEY = "cfc7671eb29314d7f164cc8dc40eb4c9"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        weather_info = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Condition": data["weather"][0]["description"],
            "Humidity": f"{data['main']['humidity']}%"
        }
        
        if format == 'json':
            click.echo(json.dumps(weather_info, indent=2))
        elif format == 'table':
            table = [[k, v] for k, v in weather_info.items()]
            click.echo(tabulate(table, headers=['Field', 'Value']))
        else:
            for key, value in weather_info.items():
                click.echo(f"{key}: {value}")
                
    except requests.exceptions.RequestException as e:
        click.echo(f"Error: Could not fetch weather for {city}")
        click.echo(str(e))

if __name__ == '__main__':
    cli()