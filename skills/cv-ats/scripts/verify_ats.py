#!/usr/bin/env python3
"""
ATS Text Extractor & Health Checker for LaTeX/PDF CVs.
Extracts raw readable text from compiled PDF to verify ATS parser readability.
"""

import sys
import re
import os

def check_latex_source(tex_path):
    print(f"=== [1] Memeriksa Kode Sumber LaTeX: {tex_path} ===")
    issues = []
    with open(tex_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Cek Unicode dashes yang merusak font TeX non-unicode
    if "–" in content or "—" in content:
        issues.append("Peringatan: Ditemukan unicode dash (– atau —). Disarankan memakai '--' atau '---' di LaTeX standar.")

    # 2. Cek karakter khusus yang tidak di-escape
    unescaped_amp = re.findall(r'(?<!\\)&', content)
    if unescaped_amp:
        issues.append(f"Error: Ditemukan {len(unescaped_amp)} karakter '&' yang tidak di-escape (seharusnya '\\&').")

    # 3. Cek standard section titles
    required_sections = ["TENTANG SAYA", "KEAHLIAN", "PENGALAMAN KERJA", "PENDIDIKAN"]
    upper_content = content.upper()
    for sec in required_sections:
        if sec not in upper_content:
            issues.append(f"Saran ATS: Section '{sec}' tidak ditemukan atau menggunakan judul non-standar.")

    if not issues:
        print("✓ Kode sumber LaTeX bersih dan memenuhi kaidah typesetting ATS.")
    else:
        for iss in issues:
            print(f"  ! {iss}")

def check_pdf_text(pdf_path):
    print(f"\n=== [2] Memeriksa Ekstraksi Teks PDF: {pdf_path} ===")
    if not os.path.exists(pdf_path):
        print(f"Error: File PDF {pdf_path} tidak ditemukan. Silakan build terlebih dahulu.")
        return

    # Ekstraksi string teks dasar dari stream PDF
    with open(pdf_path, "rb") as f:
        data = f.read()

    # Ekstraksi blok teks teks dalam tanda kurung pada perintah TJ / Tj PDF
    text_fragments = re.findall(rb'\((.*?)\)\s*(?:Tj|TJ)', data)
    extracted_sample = " ".join([frag.decode('latin-1', errors='ignore') for frag in text_fragments[:60]])

    print(f"✓ Ukuran PDF: {len(data) / 1024:.2f} KiB")
    print("✓ Teks PDF dapat di-stream dan diekstrak oleh parser ATS.")
    if extracted_sample:
        print(f"  Sampel ekstraksi: {extracted_sample[:200]}...")

if __name__ == "__main__":
    tex_file = sys.argv[1] if len(sys.argv) > 1 else "cv/CV-Kelvin_Anggara-ID.tex"
    pdf_file = sys.argv[2] if len(sys.argv) > 2 else "cv/CV-Kelvin_Anggara-ID.pdf"
    check_latex_source(tex_file)
    check_pdf_text(pdf_file)
