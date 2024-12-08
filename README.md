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


### 🥈 Flujo de la Versión 2 (v2)

```mermaid
flowchart TD
    A[📂 Select .py file] --> B[📂 Select .ico file (optional)]
    B --> C[⚙️ Generate .pyx and compile with Cython]
    C --> D[📝 Create main.py]
    D --> E[🛠️ Create executable with PyInstaller]
    E --> F[🛡️ Generate Go project]
    F --> G[💻 Compile Go project]
    G --> H[🚀 Final Executable with Go]
```
---

```mermaid
graph LR
    subgraph 🥇 v1
    A1[📂 Select .py] --> B1[📂 Select .ico]
    B1 --> C1[⚙️ Generate .pyx and compile]
    C1 --> D1[📝 Create main.py]
    D1 --> E1[🛠️ Create executable with PyInstaller]
    E1 --> F1[🚀 Final Executable]
    end

    subgraph 🥈 v2
    A2[📂 Select .py] --> B2[📂 Select .ico]
    B2 --> C2[⚙️ Generate .pyx and compile]
    C2 --> D2[📝 Create main.py]
    D2 --> E2[🛠️ Create executable with PyInstaller]
    E2 --> F2[🛡️ Generate Go project]
    F2 --> G2[💻 Compile Go project]
    G2 --> H2[🚀 Final Executable with Go]
    end
```
