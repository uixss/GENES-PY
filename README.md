# 🎫 Coding Services SEND DM v2 🎫

---


### 🥈 **Version 2 (v2) Features**:

- **Go Integration**: Integrates Go for enhanced security. This includes advanced checks for virtual environments and protections against detection techniques such as AMSI and ScriptBlockLogging.
- **Go Project Generation**: The tool generates a Go project that includes the necessary security checks and ensures that the Python executable is embedded securely within the Go project.
- **Final Compilation with Go**: The final output is a Go-compiled executable, which embeds the Python script along with the security protections.
- **Security Features**: 
  - **VM Detection**: Detects if the executable is running inside a virtual machine or sandbox environment.
  - **AMSI & ScriptBlockLogging Disablement**: Disables Microsoft’s AMSI and PowerShell ScriptBlockLogging, preventing antivirus software from detecting malicious code.

---

# 🚀 **GENES-PY** - Python Cython Executable Generator

## 📦 **Versions**

### 🥇 **Version 1 (v1)**

#### **Technologies Used**:
- Python, Cython, PyInstaller, CustomTkinter.

#### **Key Features**:
- **📂 File Selection**: Choose a Python file (.py) and an optional icon file (.ico) to use for the executable.
- **🔍 Import Extraction**: Automatically extracts all import statements from the selected Python script.
- **⚙️ Compilation with Cython**: Converts the selected Python script (.py) into a `.pyx` file, then compiles it using Cython.
- **🛠️ Executable Creation with PyInstaller**: Packages the compiled Python code into a standalone `.exe` using PyInstaller.
- **🖥️ Graphical User Interface (GUI)**: A simple and intuitive GUI built with CustomTkinter for easy interaction.

---

### 🥈 **Version 2 (v2)**

#### **Technologies Used**:
- Python, Cython, PyInstaller, Go, CustomTkinter.

#### **Key Features**:
- **✅ All features from v1**.
- **🛡️ Go Integration**: Adds advanced security checks with Go for enhanced protection.
- **📁 Go Project Generation**: Generates a Go project that includes security features to protect the executable.
- **🔒 Security Features**: Detects virtual environments, disables AMSI, prevents script logging, and more.
- **💻 Final Compilation with Go**: Embeds the compiled Python executable into the Go project and generates a final .exe with added security.

---

## 📊 **Comparison Table**

| 🔧 **Feature**                             | 🥇 **Version 1 (v1)**                  | 🥈 **Version 2 (v2)**                       |
|------------------------------------------|----------------------------------------|---------------------------------------------|
| **📚 Main Technologies**                 | Python, Cython, PyInstaller            | Python, Cython, PyInstaller, Go             |
| **🖥️ Graphical Interface**               | Yes                                    | Yes                                          |
| **📂 File Selection**                    | .py and .ico                           | .py and .ico                                |
| **🔍 Import Extraction**                 | Yes                                    | Yes                                          |
| **⚙️ Compilation with Cython**           | Yes                                    | Yes                                          |
| **🛠️ Executable Creation with PyInstaller** | Yes                                | Yes                                          |
| **🛡️ Go Integration**                    | No                                     | Yes                                          |
| **🔒 Security Features in Go**           | No                                     | Yes                                          |
| **📁 Go Project Generation**             | No                                     | Yes                                          |
| **💻 Final Compilation with Go**         | No                                     | Yes                                          |

---

## 🔄 **Workflow**

### 🥇 **Version 1 (v1) Workflow**:

1. **📂 Select .py file**: Choose the Python script (.py) to compile.
2. **📂 Select .ico file (optional)**: Optionally, select an icon file (.ico) for the executable.
3. **⚙️ Generate .pyx and compile with Cython**: Convert the Python script to `.pyx` and compile it using Cython.
4. **📝 Create main.py**: A `main.py` file is generated.
5. **🛠️ Create executable with PyInstaller**: Use PyInstaller to generate an executable from `main.py`.
6. **🚀 Final Executable**: The final `.exe` file is ready.

### 🥈 **Version 2 (v2) Workflow**:

1. **📂 Select .py file**: Choose the Python script (.py) to compile.
2. **📂 Select .ico file (optional)**: Optionally, select an icon file (.ico) for the executable.
3. **⚙️ Generate .pyx and compile with Cython**: Convert the Python script to `.pyx` and compile it using Cython.
4. **📝 Create main.py**: A `main.py` file is generated.
5. **🛠️ Create executable with PyInstaller**: Use PyInstaller to generate an executable from `main.py`.
6. **🛡️ Generate Go project**: A Go project is created to integrate security features.
7. **💻 Compile Go project**: The Go project is compiled, embedding the Python executable.
8. **🚀 Final Executable with Go**: The final `.exe` is generated with enhanced security features.

---

### 🥇 **Version 1 (v1) Features**:

- **File Selection**: Users can choose the Python script they want to compile and optionally select an icon for the executable.
- **Import Extraction**: The tool will automatically extract and display all the import statements in the Python script to ensure that all dependencies are included in the final executable.
- **Cython Compilation**: Converts the Python script into a `.pyx` file, and then compiles it with Cython, improving performance and obfuscating the source code.
- **Executable Creation with PyInstaller**: The final `.exe` is created using PyInstaller, ensuring compatibility with Windows systems.
- **Graphical Interface**: CustomTkinter provides a simple and effective GUI to guide users through the entire process.

