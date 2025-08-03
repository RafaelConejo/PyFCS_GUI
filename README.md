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

## 🔍 Use Cases and Additional Examples

To highlight the flexibility and practical applications of **PyFCS GUI**, the project repository includes a series of **additional case studies** that go beyond the main example featured in the documentation. These examples demonstrate how the tool can be applied in real-world scenarios involving color analysis and perceptual modeling.

While the core functionality is illustrated through a focused scenario, the modular design of PyFCS GUI supports broader applications in areas where nuanced color perception is critical. Key use cases include:

- 🎨 **Digital Art & Palette Design**  
  Extract dominant tones from artworks or visual prototypes to construct fuzzy color spaces that reflect perceptual transitions between hues.

- 💡 **User Interface Design**  
  Create adaptive and accessible color themes—such as color-blind-friendly palettes—based on perceptual clustering.

- 🏛️ **Cultural Heritage Restoration**  
  Compare faded pigments with hypothesized original colors, incorporating uncertainty in chromatic reconstruction through fuzzy modeling.

---

### 🎨 Case Study: *Starry Night Over the Rhône*

This case study demonstrates how PyFCS GUI can be used to extract and analyze the dominant chromatic components of Vincent van Gogh's *Starry Night Over the Rhône*.

By adjusting the extraction threshold in the fuzzy color space module, users can control the level of color granularity:

- **Low threshold:** Identifies the most dominant tones — e.g., 9 representative colors.  
- **High threshold:** Captures subtle transitions and finer chromatic variations — up to 64 tones.

This allows users to navigate between abstraction and detailed chromatic analysis with ease.

<img src="https://github.com/RafaelConejo/PyFCS_GUI/raw/main/PyFCS/external/images/Starry%20Night%20Over%20the%20Rhône.jpg" width="70%" />

<p float="left">
  <img src="https://github.com/RafaelConejo/PyFCS_GUI/blob/main/PyFCS/external/images/colors_Starry_Night_2.png" width="45%" />
  <img src="https://github.com/RafaelConejo/PyFCS_GUI/blob/main/PyFCS/external/images/colors_Starry_Night_1.png" width="45%" />
</p>

In addition, a color map focused exclusively on **yellow tones** was generated to isolate regions of the painting where yellow appears. This highlights features like lamppost reflections and luminous areas.

<img src="https://github.com/RafaelConejo/PyFCS_GUI/blob/main/PyFCS/external/images/Starry_Night_Yellow.png" width="70%" />

---

### 🟢 Case Study: *Un dimanche après-midi à l'Ile de la Grande Jatte*

This case study explores Georges Seurat's pointillist painting, composed of fine color dots that create rich chromatic complexity. Using PyFCS GUI with a **high extraction threshold**, a detailed fuzzy color space is generated that captures the artwork’s full color range.

This supports deeper analysis in areas like digital art research, color theory, and palette exploration.

<img src="https://github.com/RafaelConejo/PyFCS_GUI/blob/main/PyFCS/external/images/Un%20dimanche%20apr%C3%A8s-midi%20%C3%A0%20l'Ile%20de%20la%20Grande%20Jatte.jpg" width="70%" />

<img src="https://github.com/RafaelConejo/PyFCS_GUI/blob/main/PyFCS/external/images/colors_Un_Dimanche.png" width="50%" />

These examples demonstrate the power of PyFCS GUI in enabling detailed color exploration, perceptual clustering, and thematic filtering of image content.


---

### 📬 Contact & Support
For support or questions, feel free to contact: rafaconejo@ugr.es

