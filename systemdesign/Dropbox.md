# 📁 System Design: File Upload Service (Dropbox-Style)

A scalable and reliable system to upload, store, share, and download files—like Dropbox or Google Drive.

---

## ✅ Functional Requirements

- Upload files of various formats (images, PDFs, videos, etc.)
- Support large files (up to GBs)
- Resume broken uploads (chunked upload)
- File versioning and history
- Generate shareable links with permissions
- Fast downloads via CDN

---

## 🚫 Non-Functional Requirements

- High availability and fault tolerance
- Horizontally scalable storage
- Secure file access and authentication
- Efficient metadata and version tracking
- Monitoring and logging

---

## 🧱 High-Level Architecture

+----------------------+
| Client (Web/Mobile) |
+----------------------+
|
v
+----------------------+
| API Gateway | <- /upload, /download, /share
+----------------------+
|
+------+------+-----------+
| | |
v v v
+--------+ +----------------+ +--------------------+
| Auth | | File Metadata | | Chunk Tracker DB |
|Service | | DB | | (for resumable |
| (JWT) | | (Postgres) | | uploads) |
+--------+ +----------------+ +--------------------+
|
v
+----------------------+
| File Upload Service |
+----------------------+
|
v
+----------------------+
| Object Storage (S3) |
+----------------------+
|
v
+----------------------+
| CDN (Downloads) |
+----------------------+


---

## ⚙️ Components Explained

### 📡 API Gateway
- Exposes REST endpoints:
  - `POST /upload/initiate`
  - `POST /upload/:id/chunk`
  - `POST /upload/:id/complete`
  - `GET /file/:id/download`
  - `POST /file/:id/share`
- Validates requests, enforces rate limits, passes to backend

---

### 🔐 Auth Service
- Authenticates via JWT/OAuth
- Verifies user identity and permissions
- Generates signed URLs for secure file access

---

### 🧠 Metadata DB
- Stores:
  - `filename`, `user_id`, `file_size`
  - `timestamp`, `version`, `share_links`
- Handles folder structure, trash bin, etc.

---

### 🧩 Chunk Tracker DB
- Tracks which chunks have been uploaded
- Supports resumable uploads (each chunk is ~5MB)
- Maps `upload_id` ➝ [chunk 1: done, chunk 2: pending, ...]

---

### 📦 File Upload Service
- Accepts file chunks via API
- Validates and stores in temp location
- Once complete, merges and uploads to object storage
- Generates final file entry in metadata DB

---

### ☁️ Object Storage (S3 / GCS / Azure Blob)
- Actual file contents are stored here
- Supports scalable, replicated storage
- Files stored as UUIDs or content-hashes

---

### 🌐 CDN (Content Delivery Network)
- Speeds up download using edge caching
- Example: CloudFront or Cloudflare
- Protects access using signed URLs

---

## 🔁 Chunked Upload Flow

1. `POST /upload/initiate` → returns `upload_id`
2. Client splits file into chunks
3. `POST /upload/:upload_id/chunk` → send each chunk
4. Chunks are stored and tracked
5. `POST /upload/:upload_id/complete` → backend merges chunks
6. Final file is stored, and metadata is saved

---

## 🧰 Security Measures

- Use JWT or OAuth for API access
- Signed URLs for file downloads (expiring + permission bound)
- Encrypted file storage (AES-256)
- Virus scanning in background job
- Audit logs for upload/download access

---

## 🔄 Versioning Example

File: `report.pdf`

| Version | Path                            | Timestamp           |
|---------|----------------------------------|----------------------|
| v1      | `/user123/report/v1.pdf`        | 2024-01-10 12:30 UTC |
| v2      | `/user123/report/v2.pdf`        | 2024-03-20 09:02 UTC |

---

## 📊 Monitoring & Logging

- Track:
  - Upload failures
  - Chunk retries
  - Merge errors
- Tools:
  - Prometheus for metrics
  - Grafana dashboards
  - ELK stack for logs

---

## 💬 Interview-Friendly Questions

### Q: How would you handle 5GB uploads over unstable connections?
- Split into chunks (5MB each)
- Client retries only failed chunks
- Track chunk status in DB

### Q: How do you scale the storage layer?
- Use cloud-based object storage (S3/GCS)
- Horizontally scalable
- Files stored as blobs, metadata stored separately

### Q: How do you deduplicate files?
- Generate SHA-256 hash of file
- If hash already exists → link metadata instead of storing again

---

Let me know if you also want:

- 🧱 Low-level class diagram
- 🧠 DB schema (ERD)
- 🧑‍💻 Upload flow with code examples (Python/Node)

