
# Grayscale Task Automation Tool

## Overview

This tool was developed to automate daily tasks . It interacts with a custom portal, automating form completions by identifying on-screen elements using OpenCV for image recognition in grayscale mode and performing predefined actions such as clicking buttons, entering data, and navigating through tasks. This Python script leverages automation libraries like `pyautogui` and `opencv` to streamline repetitive tasks, significantly improving efficiency and reducing manual input.

## Features

- **Image Recognition with Grayscale:** Uses OpenCV to match elements on the screen with pre-saved images, allowing for reliable identification and interaction with UI components.
- **Automated Click and Form Entry:** Automatically clicks on form fields, buttons, and enters predefined text into input boxes.
- **Task Completion:** Automates daily tasks by navigating through multiple tabs, completing checklists, and finalizing forms.
- **Page Navigation:** Utilizes scrolling and tab switching to interact with different elements spread across the page or multiple browser tabs.
- **Chrome Automation:** Opens Chrome, navigates to specific URLs, and handles tasks across tabs.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Apogee2024/grayscale-task-automation.git
    ```

2. Install dependencies:
    ```bash
    pip install opencv-python pyautogui numpy
    ```

## Usage

1. Define your custom portal URL:
    ```python
    PORTAL = 'insertYourPortalHere'
    ```

2. Place reference images (e.g., `start_button.png`, `complete.png`) in the working directory.

3. Run the script:
    python3 main.py

## Example Functions

- **`find_and_click_grayscale(filename)`**: Finds an on-screen element based on a grayscale image and clicks it.
- **`autopm()`**: Automates filling out and completing forms based on specific image matches.
- **`mouse_click_UPM()`**: Completes tasks using predefined mouse coordinates.
- **`in_tabs_any()`**: Handles tasks across multiple open tabs in a browser.

## Contributing

If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

By automating these repetitive tasks, I was able to streamline my workflow, reducing manual input and ensuring consistency in task completion. This tool serves as a foundation for automating browser-based tasks using image recognition and grayscale matching.
