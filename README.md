# Open Gemini

Open Gemini is an open-source tool that lets Gemini language models run code on your computer.

It is a fork of [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter), specifically streamlined to support **Google's Gemini** models.

## Installation

```bash
pip install open-gemini
```

## Usage

### Terminal

After installation, run:

```bash
open-gemini
```

Or:

```bash
gemini
```

### Python

```python
from interpreter import interpreter

interpreter.chat("Plot AAPL and MSFT stock prices")
```

## Features

- **Gemini-First**: Optimized for Gemini 1.5 Pro and Flash.
- **Multimodal**: Native support for images and vision.
- **Code Execution**: capable of running Python, Javascript, Shell, and more.

## License

MIT
