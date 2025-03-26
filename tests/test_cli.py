import pytest # type: ignore
from click.testing import CliRunner # type: ignore
from cli.main import cli # type: ignore

def test_weather_command_basic():
    runner = CliRunner()
    result = runner.invoke(cli, ['london'])
    assert result.exit_code == 0
    assert 'City: ' in result.output

def test_weather_command_json_format():
    runner = CliRunner()
    result = runner.invoke(cli, ['london', '--format', 'json'])
    assert result.exit_code == 0
    assert '"City":' in result.output

def test_weather_command_table_format():
    runner = CliRunner()
    result = runner.invoke(cli, ['london', '--format', 'table'])
    assert result.exit_code == 0
    assert 'Field' in result.output