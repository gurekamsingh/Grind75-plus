# 📣 Real-Time Notification System (Design + Explanation)

A system that sends real-time notifications (e.g., “Your order has shipped”) through Email, SMS, or Push. Built to be scalable, reliable, and resilient.

---

## 🔄 End-to-End System Architecture (ASCII Diagram)

```text
         +---------------------+          
         |  Upstream Services |  (Order Service, Chat, etc)
         +---------------------+          
                    |
                    v
         +----------------------+         
         |   📡 Ingest Layer       |  <- REST API Gateway
         |   (/send-notification) |
         +----------------------+         
                    |
                    v
         +----------------------+         
         |   📨 Queue Layer        |  <- Kafka / AWS SQS / Redis Streams
         +----------------------+         
                    |
                    v
         +----------------------+         
         |   🤖 Worker Layer       |  <- Background job processors
         +----------------------+         
             /           |           \
            v            v            v
       +---------+  +----------+  +-----------+
       |  Email  |  |   SMS    |  |   Push    |
       | Sender  |  |  Sender  |  |  Sender   |
       +---------+  +----------+  +-----------+
            |            |            |
            v            v            v
      +----------+  +----------+  +----------+
      | Retry Q  |  | Retry Q  |  | Retry Q  |
      +----------+  +----------+  +----------+
                    |
                    v
         +----------------------+         
         | 🔐 User Preferences DB |  <- Channels, Opt-ins/outs, Quiet Hours
         +----------------------+         
                    |
                    v
         +----------------------+         
         | 🔍 Monitoring Layer   |  <- Prometheus, Grafana, CloudWatch
         +----------------------+         

## How It Works (Step-by-Step)

### 1. Ingest Layer (Producer)
- Accepts HTTP API calls from internal services  
  **Example:** `POST /send-notification`
- Validates request, enriches payload
- Pushes it to a message queue

### 2. Queue Layer (Kafka/SQS)
- Decouples the ingest from processing
- Guarantees durability and order (**Kafka**)
- Supports retries, backoff, and scale-out

### 3. Worker Layer (Consumer)
- Consumes messages from the queue
- Checks **User Preferences DB** for:
  - Allowed channels  
  - Time-of-day restrictions  
  - Opt-outs
- Chooses the channel (Email, SMS, Push) and sends

### 4. Retry Logic
- If a channel fails (e.g., SMS provider down), message goes to a **Retry Queue**
- Retries with **exponential backoff**
- After _N_ retries, moves to **Dead Letter Queue (DLQ)**

### 5. User Preferences DB
- Stores user notification settings  

**Examples:**
- User `123`: wants "order updates" via **Email only**
- User `456`: no **Push** notifications between **10 PM and 7 AM**

### 6. Monitoring Layer
- Tracks errors, latencies, retries
- Triggers alerts if failure rate spikes
- Helps monitor queue lag and service health
