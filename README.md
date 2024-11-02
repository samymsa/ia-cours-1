# Image Processor

This project holds a simple image processing pipeline that can be used to resize and add padding to images.

## Setup

This project uses `pip-tools` to manage dependencies. To install the dependencies, run:

```bash
pip install pip-tools
pip-compile # Generate requirements.txt
pip-sync    # Install dependencies
```

## Usage

```bash
python main.py
```

## Contributing

Install the pre-commit hooks by running:

```bash
pre-commit install
```

If you use VSCode, please install the recommended extensions (see `.vscode/extensions.json`).
