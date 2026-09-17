# Panduan & Standar ATS (Applicant Tracking System) untuk CV Teknikal

## 1. Prinsip Utama ATS Readiness
- **Ekstrak Teks Bersih**: Parser ATS (seperti Workday, Taleo, Greenhouse, Lever, SAP SuccessFactors) mengonversi PDF ke plain text. Hindari tabel kompleks multi-nested atau gambar tanpa teks alternatif.
- **Section Heading Standar**:
  - Bahasa Indonesia: `TENTANG SAYA` / `RINGKASAN`, `KEAHLIAN`, `PENGALAMAN KERJA`, `PROYEK`, `PENDIDIKAN`.
  - Bahasa Inggris: `SUMMARY` / `ABOUT ME`, `SKILLS`, `WORK EXPERIENCE`, `PROJECTS`, `EDUCATION`.
- **Format Kontak**: Letakkan nomor telepon dengan kode negara (`+62`), email aktif, tautan LinkedIn, GitHub, dan website portofolio yang dapat diklik.

## 2. Struktur Bullet Point Berbasis Dampak (Formula XYZ Google)
Format penulisan pengalaman kerja yang efektif:
> *"Mencapai [X] yang diukur dengan [Y], dengan melakukan [Z]"*

Contoh:
- *Bukan*: "Mengembangkan sistem backend di XLSmart."
- *ATS-Friendly*: "Memodernisasi arsitektur sistem dari metode synchronous menjadi asynchronous event-driven menggunakan Solace/Kafka, berhasil mengeliminasi bottleneck dan memangkas response time API."

## 3. Optimasi Kata Kunci (Keywords Matching)
- Kelompokkan keahlian ke dalam kategori logis:
  - **Bahasa & Framework**: Java (Spring Boot, Quarkus), Golang
  - **Messaging / Streaming**: Apache Kafka, Solace, Dead Letter Queue (DLQ)
  - **Orkestrasi & API**: Microservices, Kogito BPMN v2, Kong API Gateway, REST Client
  - **DevOps & Cloud**: Docker, Kubernetes, ArgoCD, GitOps, CI/CD
  - **Basis Data**: PostgreSQL, MySQL, Redis
- Selalu cantumkan akronim dan kepanjangannya jika relevan (misal: *SIT [System Integration Testing]*, *UAT [User Acceptance Testing]*, *BPMN [Business Process Model and Notation]*).
