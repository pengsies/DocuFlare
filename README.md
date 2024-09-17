
# <p align="center">DocuFlare - Document to PDF Converter</p>


<p align="center"> Born out of boredom and a weird urgent need to convert documents after getting a new machine, DocuFlare is a not-so-powerful and not-so-versatile document converter that transforms a variety of file formats, including `.docx`, `.pptx`, `.xlsx`, `.txt`, `.md`, and images, into PDF documents.
It’s meant to be an offline, <b>FREE!!!</b> tool designed for simplicity, speed, and ease of use, featuring a clean user interface and batch processing capabilities...but there are many issues that remain to be resolved.</p>

---

## <p align="Centre">🚀 Features</p>

- **Multi-format support**: Convert Word, Excel, PowerPoint, Markdown, plain text files, and images (`.jpg`, `.png`) to PDF.
- **Batch processing**: Convert multiple files at once, or even entire ZIP files.
- **Custom output file names**: Choose your desired file names and output directory.
- **Progress bar**: Visual feedback on conversion progress.
- **Cross-platform**: Compatible with Windows, macOS, and Linux.
- **Standalone & Offline**: No need for third-party software like LibreOffice or Microsoft Word.

---

## <p align="centre">🛠 Installation</p>

### <p align="left">Prerequisites</p>

Ensure you have **Python 3.8+** installed on your machine. Then, clone the repository and install the required dependencies.

### <p align="left">Steps</p>

1. **Clone the Repository**

    ```bash
    git clone https://github.com/pengsies/DocuFlare.git
    cd docuflare
    ```

2. **Install Dependencies**

    Install the required Python libraries via `pip`:

    ```bash
    pip install -r requirements.txt
    ```

### Dependencies List
**Last Updated:** 17th September 2024

- `python-docx==1.1.2`
- `python-pptx==1.0.2`
- `pandas==2.2.2`
- `reportlab==4.2.2`
- `openpyxl==3.1.5`
- `pyside6==6.7.2`
- `pillow==10.4.0`
- `markdown2==2.5.0`


---

## <p align="centre">🚦 Usage</p>

1. **Run the application**:

    ```bash
    python main.py
    ```

2. **Select files to convert**:
   - You can select any supported file type: `.docx`, `.pptx`, `.xlsx`, `.txt`, `.md`, `.jpg`, `.png`, or `.zip` for batch conversion via the GUI.

3. **Choose the output folder**:
   - Pick where you’d like to save your converted PDFs.

4. **Convert**:
   - Click **Convert to PDF** to begin. The progress bar will show the conversion status.

---

## <p align="Centre">📁 Supported Formats</p>

| File Type      | Supported for Conversion | Notes                                    |
|----------------|--------------------------|------------------------------------------|
| **.docx**      | Yes                      | Text, tables, images, headers, footers   |
| **.pptx**      | Yes                      | PowerPoint slides                        |
| **.xlsx**      | Yes                      | Excel spreadsheets (text and tables)     |
| **.txt**       | Yes                      | Plain text files                         |
| **.md**        | Yes                      | Markdown files                          |
| **.jpg/.png**  | Yes                      | Image files                             |
| **.zip**       | Yes                      | Batch conversion of multiple files       |

---

## <p align="left">💡 Example Usage</p>

- To convert a single Word file (`.docx`) to PDF:

    ```bash
    python main.py
    ```

    Use the UI to select the file and desired output directory.

- **Batch processing**: To convert multiple files (via ZIP), simply select a `.zip` archive containing supported file types, and DocuFlare will handle the conversion for each file.

---
## <p align="center">ඞඞඞ Known Issues ඞඞඞ</p>

### Text/Docx/Markdown Conversion
- **Issue:** Converted Documents (all extensions) has overflow.
    - **Description:** The converted document may extend beyond page margins, causing text or content to be cut off.


- **Issue**: Converted Documents (.docx) do not retain images and formatting.
    - **Description:** The converted document won't retain any original formatting nor images.


### Excel Conversion
- **Issue:** Tables do not get formatted.
    - **Description:** The converted document fails to retain table styles and cell formatting.

### PowerPoint Conversion
- **Issue:** No formatting.
    - **Description:** Converted presentations lose their original formatting, including layout and design elements.

### Image Conversion
- **Issue:** No images.
    - **Description:** Images are missing or not included in the converted file.

---

This project is still a work-in progress, so please do provide feedback or report any further issues to [pengsatwork@gmail.com](mailto:pengsatwork@gmail.com).

---

## <p align="left">🧩 Contributing</p>


We welcome contributions! To get started:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/AmazingFeature`.
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`.
4. Push to the branch: `git push origin feature/AmazingFeature`.
5. Open a pull request.

Feel free to open issues for bug reports, feature requests, or general questions.

---

## <p align="left">📝 License</p>

**DocuFlare** is licensed under the **GPLv3 License**. Please see the `LICENSE` file for more information.

---

## <p align="left">📞 Contact</p>

If you have any questions or need further assistance, or would like to start a project with me :3

- [**Email**](pengsatwork@gmail.com.com)
- [**GitHub**](https://github.com/pengsies)
- [**LinkedIn**](https://www.linkedin.com/in/chua-yu-xuan/)
---

