---
name: cv-ats
description: "Audit, optimize, and score LaTeX and PDF CVs for ATS (Applicant Tracking System) compatibility, keyword density, and technical impact metrics. Use this skill when evaluating CV readability, tailoring CV to a specific job description, fixing typography/parseability issues, or verifying PDF text extraction."
user-invocable: true
license: MIT
metadata:
  version: "1.0.0"
  purpose: "ATS optimization, scoring, and formatting for Curriculum Vitae"
---

# Skill: CV ATS Optimization & Audit

Skill ini memandu agen AI dalam mengaudit, mengoptimalkan, dan memvalidasi file CV berbasis LaTeX (`cv/*.tex`) dan output PDF (`cv/*.pdf`) agar memiliki tingkat kelulusan tinggi pada sistem **ATS (Applicant Tracking System)** seperti Workday, Taleo, Greenhouse, Lever, dan SAP SuccessFactors.

---

## 1. Prinsip Utama ATS Optimization

1. **Clean Parseability & Text Extraction**:
   - Struktur dokumen harus dapat diurai menjadi teks murni (*plain text*) secara sekuensial tanpa kehilangan kata kunci atau teracak karena kolom/tabel yang rumit.
   - Hindari unicode dashes (`–`, `—`) pada LaTeX standar non-fontspec; gunakan `--` atau `---`.
   - Pastikan semua karakter khusus (`&`, `%`, `$`, `_`) di-escape dengan benar.

2. **Standard Section Headers**:
   - Gunakan judul section baku yang mudah dikenali mesin ATS:
     - **Bahasa Indonesia**: `TENTANG SAYA` / `RINGKASAN`, `KEAHLIAN`, `PENGALAMAN KERJA`, `PROJECTS` / `PROYEK`, `PENDIDIKAN`.
     - **Bahasa Inggris**: `SUMMARY` / `ABOUT ME`, `SKILLS`, `WORK EXPERIENCE`, `PROJECTS`, `EDUCATION`.

3. **Formula Penulisan Berdampak (Google XYZ Formula)**:
   - Tulis setiap pencapaian dalam formula:
     > *"Accomplished [X], as measured by [Y], by doing [Z]"* / *"Mencapai [X], yang diukur dengan [Y], dengan melakukan [Z]"*
   - Mulai setiap bullet point dengan *action verb* yang kuat (*Merancang, Memodernisasi, Mengarsiteksi, Mengembangkan, Mengoptimalkan*).

4. **Keyword Matching & Hard Skills Grouping**:
   - Kelompokkan keahlian teknis secara sistematis:
     - Bahasa & Framework Backend
     - Messaging / Streaming / Event-Driven
     - Orkestrasi Proses Bisnis (BPMN / Kogito)
     - Cloud, Container & GitOps (Kubernetes, Docker, ArgoCD)
     - Basis Data & Caching (PostgreSQL, MySQL, Redis)
     - API & Security (REST Client, Kong API Gateway)

---

## 2. Rubrik Evaluasi Skor ATS (Skala 0-100)

| Pilar Evaluasi | Bobot | Aspek yang Dinilai |
| :--- | :---: | :--- |
| **Parseability & Struktur** | 25% | Keterbacaan teks murni PDF, header baku, format tanggal konsisten, tidak ada karakter rusak (*garbled*). |
| **Hard Skills & Keywords** | 25% | Kepadatan kata kunci teknis, relevansi ke industri target (Fintech, Telco, Enterprise Backend), pengelompokan rapi. |
| **Impact & Action Verbs** | 25% | Penggunaan formula XYZ, metrik kuantitatif (TPS, latensi, zero-downtime, jumlah terminal/fitur/tiket), penghapusan frasa pasif/generik. |
| **Konteks Kontak & Metadata** | 15% | Nomor telepon berformat internasional (+62), email profesional, link GitHub/LinkedIn/Portfolio yang dapat diklik (*clickable*). |
| **Tipografi & Desain Bersih** | 10% | Margin seimbang, penataan ruang vertikal (*spacing*), konsistensi huruf dan pemenggalan kata. |

---

## 3. Alur Kerja Evaluasi & Optimasi

### Langkah 1: Audit Sumber LaTeX & Ekstraksi Teks
Jalankan script verifikasi ATS:
```bash
python3 .agents/skills/cv-ats/scripts/verify_ats.py cv/CV-Kelvin_Anggara-ID.tex cv/CV-Kelvin_Anggara-ID.pdf
```

### Langkah 2: Evaluasi Terhadap Job Description (Jika Diberikan)
- Bandingkan kata kunci yang diminta dalam Job Description (JD) dengan section Keahlian dan Pengalaman Kerja.
- Sesuaikan terminologi teknis tanpa melebih-lebihkan fakta riil (*no hallucinations*).

### Langkah 3: Optimasi Konten
- Terapkan perbaikan kata kunci, perbaiki tata bahasa/typo, dan hilangkan duplikasi baris.
- Pastikan seluruh link menggunakan HTTPS dan teks tautan yang deskriptif.

### Langkah 4: Kompilasi & Verifikasi Akhir
Kompilasi dokumen ke PDF menggunakan Tectonic:
```bash
tectonic cv/CV-Kelvin_Anggara-ID.tex --outdir cv
```
Buka dan periksa hasil PDF:
```bash
open -a "/Applications/Microsoft Edge.app" cv/CV-Kelvin_Anggara-ID.pdf || open -a Safari cv/CV-Kelvin_Anggara-ID.pdf
```

---

## 4. Referensi Tambahan
- [Panduan Lengkap ATS](./references/ats_guidelines.md)
