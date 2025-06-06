# PyFCS GUI

**PyFCS GUI** is a graphical user interface developed as an extension of the open-source PyFCS library. It enables the creation, visualization, and application of fuzzy color spaces derived from either color palettes or image data. This tool combines interactive 3D exploration, advanced color mapping, and reusable export features, making it useful for perceptual analysis, artistic exploration, and scientific research.

The GUI enhances usability by offering a practical way to apply fuzzy color models, which are grounded in fuzzy logic and conceptual space theory, building upon previous developments like the JFCS Java library.

---

### 📁 Repository Structure and Component Distribution
The main components of this repository are organized as follows:

- **`PyFCS/`** – Core source code of the application, including all GUI logic and fuzzy color space handling.
- **`PyFCS_GUI_Manual/`** – User manual with detailed instructions, explanations of functionality, and usage examples.
- **`fuzzy_color_spaces/`** – Contains pre-generated fuzzy color spaces for testing and demonstration purposes.
- **`image_test/`** – Collection of sample images used for testing and evaluation.

---

### 🔧 How to Use

If no modifications to the source code are needed, follow these steps for a quick installation on **Windows**:

1. Access the project repository on GitHub and download the library using the **"Clone or Download"** button, or from the **Releases** section by downloading the `.zip` file.
2. Extract the contents of the `.zip` file to a preferred local folder.
3. Make sure you have **Python 3.9 or higher** installed, along with **pip** (or use an environment manager like [Anaconda](https://www.anaconda.com/)).
   - To install pip manually (if not already available), you can run:
     ```bash
     python -m ensurepip --upgrade
     ```
4. Open a terminal (CMD or PowerShell), navigate to the root directory of the project, and install the required dependencies:
   ```bash
   pip install -r PyFCS\external\requirements.txt
   ```
5. Once the dependencies are installed, launch the main interface structure by executing:
    ```bash
    python PyFCS\visualization\basic_structure.py
    ```

### 🐧 Additional Notes for Linux Users
If you're using Linux, make sure to install system-level dependencies required by the GUI before running the program. These are not Python packages and must be installed separately:
   ```bash
   sudo apt update
   sudo apt install python3.12-tk
   pip install PyQtWebEngine
   ```
These steps ensure full compatibility with features such as Tkinter-based dialogs and enhanced Qt-based rendering on Linux systems.

---

### 📖 Interface Manual

A complete manual explaining the use of the GUI, including examples and step-by-step guides, is available in the following folder of the repository:  
🔗 [PyFCS_GUI_Manual](https://github.com/RafaelConejo/PyFCS_GUI/tree/main/PyFCS_GUI_Manual)

---

### 📬 Contact & Support
For support or questions, feel free to contact: rafaconejo@ugr.es

