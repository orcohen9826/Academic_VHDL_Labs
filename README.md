# Image Filtering Project


---

## Project Structure
The repository is organized as follows:

```
├── README.md              # Main project documentation (this file)
├── Lab1_ImageFilters/     # Contains lab-specific resources
│   ├── utilities/         # Contains Python utility scripts and related resources
│   │   ├── raw_image_to_mif.py    # Converts RAW image files into MIF files for Quartus
│   │   ├── filters.py             # Applies and compares image filters on RAW images
│   │   ├── README_HE.md           # Detailed explanation in Hebrew about the filtering algorithms
│   ├── VHDL/              # Folder for VHDL source code and MIF files
│   │   ├── *.vhd          # VHDL files for implementation
│   │   ├── *.mif          # MIF files generated for Quartus
```

---

## Files in `utilities/` Folder

### 1. `raw_image_to_mif.py`
- **Description**:
  This script reads a RAW image file (e.g., `256x256` with RGB channels), processes the pixel data, and generates three separate MIF files for the **R**, **G**, and **B** channels. The MIF files can be used to initialize ROM blocks in Quartus for hardware simulations.

- **How to Use**:
  1. Place your RAW image file (e.g., `lena_005noise_256x256.raw`) in the same directory as the script.
  2. Update the RAW file path in the script if necessary.
  3. Run the script:
     ```bash
     python raw_image_to_mif.py
     ```
  4. The generated MIF files (`r_channel.mif`, `g_channel.mif`, and `b_channel.mif`) will be saved in the `utilities/` folder.
  5. Copy the MIF files to the appropriate location (e.g., `Lab1_ImageFilters/VHDL/`) for Quartus usage.

---

### 2. `filters.py`
- **Description**:
  This script applies three types of filters (**Median**, **Median of Medians**, and **Conditional Median of Medians**) on a RAW image. It reads the RAW file, processes each RGB channel individually, and displays the original and filtered images side-by-side for comparison.

- **How to Use**:
  1. Place your RAW image file (e.g., `lena_005noise_256x256.raw`) in the same directory as the script.
  2. Update the RAW file path in the `main` function if necessary.
  3. Run the script:
     ```bash
     python filters.py
     ```
  4. The script will display the original image and the results of each filter, allowing for easy visual comparison.

---

## Hebrew Explanation
For a detailed explanation in Hebrew about the different filtering algorithms and their uses, refer to the **README_HE.md** file in the `utilities/` folder. This document provides an in-depth overview of each filter type, including **Median**, **Median of Medians**, and **Conditional Median of Medians**.

---

## Notes
- The `filters.py` script includes visual output to help you evaluate the effectiveness of each filter on the image.
- Ensure you have the necessary Python packages installed before running the scripts (e.g., `numpy`, `scipy`, `PIL`, `matplotlib`).

To install the required packages, you can use:
```bash
pip install numpy scipy pillow matplotlib
```

---

## Getting Started with VS Code
To get started with this project using **VS Code**, follow these steps. Please follow each step carefully and type the exact commands into your terminal.

1. **Clone the Repository or Download the Files to Your Computer**:
   - If you choose to clone the repository, open your terminal (command line) and type the following commands. If you downloaded the files, you can skip to the next step.
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
   - This command will download the entire project to your computer and move into the project's main directory.

2. **Create a Virtual Environment**:
   - A virtual environment is a separate Python setup for this project. This keeps all installed packages isolated for just this project.
   - In VS Code, right-click on one of the files, and select 'Open in Integrated Terminal'. This will open a terminal inside VS Code.
   - Then type the following commands in the terminal:
   ```bash
   python -m venv venv
   ```
   - This command will create a folder named `venv` that contains the virtual environment.

3. **Activate the Virtual Environment**:
   - You need to activate the virtual environment to use it. Follow the instructions based on your operating system:
   - **Windows**: In your terminal, type:
     ```bash
     venv\Scripts\activate
     ```
     - After typing this command, you should see `(venv)` at the beginning of the command line, indicating the virtual environment is active.
   - **macOS/Linux**: In your terminal, type:
     ```bash
     source venv/bin/activate
     ```
     - You should also see `(venv)` at the beginning of your command line.

4. **Install Required Packages**:
   - We need to install some packages to help run our scripts, like handling images and numerical calculations.
   - With the virtual environment activated, type the following command:
   ```bash
   pip install numpy scipy pillow matplotlib
   ```
   - This command will download and install all the necessary libraries for the project. Make sure you see a successful installation message for each package.

5. **Run the Scripts**:
   - You have two options to run the scripts:
     1. **Option 1: Using the Terminal**
        - Make sure your terminal is open within VS Code and type:
        ```bash
        python filters.py
        ```
        - This will execute the script and display the results on your screen.
     2. **Option 2: Using the Run Button**
        - Alternatively, you can click the **Run** button located in the top right corner of VS Code to run the script directly.
   - Follow similar steps for running other scripts like `raw_image_to_mif.py`.

