# Image Processor

This project holds a simple image processing pipeline that can be used to resize and add padding to images.

## Setup

### Python version

This project uses Python 3.11.10. Make sure you have the correct version installed.

### Virtual environment

Create a virtual environment using your preferred tool. For example, using `venv`:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Dependencies

This project uses `pip-tools` to manage dependencies. To install the dependencies, run:

```bash
pip install pip-tools
pip-sync
```

Alternatively, you can install the dependencies directly:

```bash
pip install -r requirements.txt
```

## Usage

Run the following command and follow the instructions:

```bash
python main.py
```

## Contributing

### Pre-commit hooks

Install the pre-commit hooks by running:

```bash
pre-commit install
```

### Dependencies

To add or update dependencies, edit the `requirements.in` file and run:

```bash
pip-compile
pip-sync
```

### VSCode

If you use VSCode, please install the recommended extensions (see `.vscode/extensions.json`).
