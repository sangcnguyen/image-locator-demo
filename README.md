# Canvas Automation Demo

This project automates interactions with an HTML5 canvas-based online calculator using Python, Playwright for browser control, and OpenCV for template matching to locate and click buttons.


## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/canvas-automation-demo.git
    cd canvas-automation-demo
    ```

2. **Install dependencies:**

3. **Run the automation script:**
    ```bash
    python calculator_test.py
    ```

## Requirements

- Python 3.13+
- [Playwright](https://playwright.dev/python/)
- [OpenCV](https://opencv.org/)

## Usage

- Place template images for calculator buttons in the `input/` directory.
- Modify [`calculator_test.py`](calculator_test.py) to change the automation sequence.

## Project Structure

- `calculator_test.py` — Main automation script
- `input/` — Template images for button matching
- `pyproject.toml` — Project dependencies and metadata