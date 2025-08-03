# PyFCS GUI

**PyFCS GUI** is a graphical user interface developed as an extension of the open-source PyFCS library. It enables the creation, visualization, and application of fuzzy color spaces derived from either color palettes or image data. This tool combines interactive 3D exploration, advanced color mapping, and reusable export features, making it useful for perceptual analysis, artistic exploration, and scientific research.

The GUI enhances usability by offering a practical way to apply fuzzy color models, which are grounded in fuzzy logic and conceptual space theory, building upon previous developments like the JFCS Java library.

A complete manual explaining the use of the GUI, including several real-world application examples and step-by-step guides, is available in the following folder of the repository:  
🔗 [PyFCS_GUI_Manual](https://github.com/RafaelConejo/PyFCS_GUI/tree/main/PyFCS_GUI_Manual)

---

## User Experience Evaluation

To assess the usability and perceived quality of the PyFCS GUI, a user study was conducted using the standardized User Experience Questionnaire (UEQ), which evaluates aspects such as **attractiveness**, **efficiency**, **dependability**, and **clarity**. A group of representative users completed the questionnaire after interacting with the software.

The results were **overall positive**, indicating a high level of user satisfaction and providing empirical support for the system’s usability.

- 📄 The full questionnaire used is available [here](https://forms.gle/pngDqJdYyYyZTRas8).
- 📊 The collected responses and results can be found [here (CSV format)](https://github.com/RafaelConejo/PyFCS_GUI/tree/main/PyFCS/test/User%20Experience%20Questionnaire%20(UEQ)).

---

### 📁 Repository Structure and Component Distribution
The main components of this repository are organized as follows:

- **`PyFCS/`** – Core source code of the application, including all GUI logic and fuzzy color space handling.
- **`PyFCS_GUI_Manual/`** – User manual with detailed instructions, explanations of functionality, and usage examples.
- **`fuzzy_color_spaces/`** – Contains pre-generated fuzzy color spaces for testing and demonstration purposes.
- **`image_test/`** – Collection of sample images used for testing and evaluation.

---

### 🔧 How to Use

If you don't need to modify the source code, follow the steps below for a quick installation based on your operating system.

---

#### 📥 1. Download the Project

Download the repository from GitHub using the **"Clone or Download"** button or from the **Releases** section as a `.zip` file.  
Extract the contents to a local folder of your choice.

### 💻 Installation by Operating System

#### 🪟 Windows

Make sure you have **Python 3.9 or higher** installed, along with **pip**.

If `pip` is missing, you can install it with:

```bash
python -m ensurepip --upgrade
```

Then, install the required Python dependencies and launch the interface:

```bash
pip install -r PyFCS\external\requirements.txt

python PyFCS\visualization\main_structure.py
```

---

#### 🐧 Linux

```bash
# Make the setup script executable (only once)
chmod +x ./PyFCS/external/setup_pyfcs_linux.sh

# Run the setup script and launch the interface with:
./PyFCS/external/setup_pyfcs_linux.sh
```

> 💡 The script creates a virtual environment, installs Python dependencies, and handles system packages like `tkinter`.

---

#### 🍎 macOS

```bash
# Make the setup script executable (only once)
chmod +x ./PyFCS/external/setup_pyfcs_mac.sh

# Run the setup script and launch the interface with:
./PyFCS/external/setup_pyfcs_mac.sh
```

> 💡 This script uses Homebrew to install Python (if needed), ensures `tkinter` works, and configures everything automatically.

---

### 📬 Contact & Support
For support or questions, feel free to contact: rafaconejo@ugr.es

