# 🚀 EXE Generator with Cython, PyInstaller, and Go

## 📝 Description

This repository contains two versions of a tool to generate executable files (.exe) from Python scripts (.py).

- **Version 1 (v1)** uses **Cython** and **PyInstaller** to compile and package the executable.
- **Version 2 (v2)** adds integration with a **Go** project to provide advanced functionality and additional security measures.

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

```mermaid
flowchart TD
    A[📂 Select .py file] --> B[📂 Select .ico file (optional)]
    B --> C[⚙️ Generate .pyx and compile with Cython]
    C --> D[📝 Create main.py]
    D --> E[🛠️ Create executable with PyInstaller]
    E --> F[🚀 Final Executable]
```
