# Weather CLI

A cross-platform command-line tool for checking weather information.

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Get weather in text format
weather london

# Get weather in JSON format
weather paris --format json

# Get weather in table format
weather "new york" -f table
```

## Development

1. Create virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -e .
```

3. Run tests:
```bash
pytest -v
```
## Adding a new release

```bash
git tag v<release_number>.x.x
```
```bash
git push origin v<release_number>.x.x
```


## License

MIT