import click
import requests
import json
from tabulate import tabulate
from dotenv import load_dotenv
import os

load_dotenv()

@click.command()
@click.argument('city')
@click.option('--format', '-f', type=click.Choice(['text', 'json', 'table']), default='text')
def cli(city: str, format: str):
    """Weather CLI - Get weather information for any city"""
    API_KEY = os.getenv('WEATHER_API_KEY')
    if not API_KEY:
        click.echo("Error: API key not found")
        return 1
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
        return 1
    
    return 0

if __name__ == '__main__':
    cli()