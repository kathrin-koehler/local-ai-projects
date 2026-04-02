import ollama
import PyPDF2

def summarize_text(text):
    response = ollama.chat(
        model="llama3.2",
        messages=[{
            "role": "user",
            "content": f"Bitte fasse folgenden Text kurz zusammen:\n\n{text}"
        }]
    )
    return response["message"]["content"]

def read_pdf(filepath):
    with open(filepath, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def read_txt(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

# --- Hier anpassen ---
filepath = "test.txt"  # oder "test.pdf"

if filepath.endswith(".pdf"):
    text = read_pdf(filepath)
else:
    text = read_txt(filepath)

summary = summarize_text(text)
print("\n📝 Zusammenfassung:\n")
print(summary)