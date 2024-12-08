# 🚀 GENES-PY

## 📦 Versions

### 🥇 Version 1 (v1)

- **Technologies Used**: Python, Cython, PyInstaller, CustomTkinter.
- **Features**:
  - 📂 **File Selection**: Select the Python file (.py) and the icon file (.ico).
  - 🔍 **Import Extraction**: Extracts imports from the Python script.
  - ⚙️ **Compilation with Cython**: Converts the .py file to .pyx.
  - 🛠️ **Executable Creation**: Uses PyInstaller to package the executable.
  - 🖥️ **Graphical User Interface**: Provides an easy-to-use GUI for the compilation process.

### 🥈 Version 2 (v2)

- **Technologies Used**: Python, Cython, PyInstaller, Go, CustomTkinter.
- **Features**:
  - ✅ **All features from v1**.
  - 🛡️ **Go Integration**: Adds advanced security layers.
  - 📁 **Go Project Generation**: Creates a Go project that includes security checks.
  - 🔒 **Security Features**: Detects virtual environments, disables AMSI, and more.
  - 💻 **Final Compilation with Go**: Generates a final executable that embeds the compiled Python executable.

## 📊 Comparison Table

| 🔧 **Feature**                           | 🥇 **Version 1 (v1)**                  | 🥈 **Version 2 (v2)**                       |
|----------------------------------------|----------------------------------------|---------------------------------------------|
| **📚 Main Technologies**               | Python, Cython, PyInstaller            | Python, Cython, PyInstaller, Go             |
| **🖥️ Graphical Interface**             | Yes                                    | Yes                                          |
| **📂 File Selection**                  | .py and .ico                           | .py and .ico                                |
| **🔍 Import Extraction**               | Yes                                    | Yes                                          |
| **⚙️ Compilation with Cython**         | Yes                                    | Yes                                          |
| **🛠️ Executable Creation with PyInstaller** | Yes                                | Yes                                          |
| **🛡️ Go Integration**                  | No                                     | Yes                                          |
| **🔒 Security Features in Go**         | No                                     | Yes                                          |
| **📁 Go Project Generation**           | No                                     | Yes                                          |
| **💻 Final Compilation with Go**       | No                                     | Yes                                          |

## 🔄 Workflow

### 🥇 Version 1 (v1) Workflow

1. **📂 Select .py file**: Choose the Python script (.py) you want to compile.
2. **📂 Select .ico file (optional)**: Optionally, choose an icon file (.ico) for the executable.
3. **⚙️ Generate .pyx and compile with Cython**: Cython will convert the `.py` script into a `.pyx` file and compile it.
4. **📝 Create main.py**: A `main.py` file will be generated.
5. **🛠️ Create executable with PyInstaller**: PyInstaller will create an executable file (.exe) from the `main.py` file.
6. **🚀 Final Executable**: The final `.exe` file is ready to run.

### 🥈 Version 2 (v2) Workflow

1. **📂 Select .py file**: Choose the Python script (.py) you want to compile.
2. **📂 Select .ico file (optional)**: Optionally, choose an icon file (.ico) for the executable.
3. **⚙️ Generate .pyx and compile with Cython**: Cython will convert the `.py` script into a `.pyx` file and compile it.
4. **📝 Create main.py**: A `main.py` file will be generated.
5. **🛠️ Create executable with PyInstaller**: PyInstaller will create an executable file (.exe) from the `main.py` file.
6. **🛡️ Generate Go project**: A Go project will be generated, adding advanced security features.
7. **💻 Compile Go project**: The Go project will be compiled, embedding the compiled Python executable.
8. **🚀 Final Executable with Go**: The final `.exe` file is ready with the added security and functionality from Go.

---

## Workflow Summary

### 🥇 Version 1 (v1)

- **Select .py file** → **Optional: Select .ico file** → **Generate .pyx and compile with Cython** → **Create main.py** → **Create executable with PyInstaller** → **Final Executable**.

### 🥈 Version 2 (v2)

- **Select .py file** → **Optional: Select .ico file** → **Generate .pyx and compile with Cython** → **Create main.py** → **Create executable with PyInstaller** → **Generate Go project** → **Compile Go project** → **Final Executable with Go**.

