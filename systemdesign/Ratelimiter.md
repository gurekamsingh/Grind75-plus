# 🚦 System Design: Rate Limiter

## 📌 Problem Statement

Design a **Rate Limiter** that allows **each client** to make **up to 100 requests per minute** to your API Gateway.

The system must:
- Track requests per **user ID or IP address**
- Reject requests beyond the allowed rate with an appropriate error
- Be **low-latency**, **fault-tolerant**, and **scalable**
- Support **distributed deployment** across multiple nodes

---

## 🎯 Functional Requirements

- Limit each user to **100 requests per 60 seconds**
- Return **HTTP 429 (Too Many Requests)** if the limit is exceeded
- Reset the request count every minute (or use a smoother sliding window)

---

## 🧱 Components and Flow

### 1. **Incoming Request**

The flow begins when a **client** (e.g., web app or mobile device) makes a request to your backend.

Each request includes a **client identifier**, such as:
- User ID (for authenticated users)
- IP address (for anonymous users)

---

### 2. **Load Balancer**

- The **Load Balancer** receives the request and routes it to one of the available **Rate Limiter Nodes**.
- To maintain per-client state, use **sticky sessions** based on the client ID — this ensures all requests from the same user go to the same node.

---

### 3. **Rate Limiter Node + In-Memory Store**

Each node contains:

- **Local logic** to check rate limits
- A fast **in-memory data store** (e.g., **Redis** or Memcached) to persist counters

#### Request Handling:

- The Rate Limiter checks Redis for the current count of requests from the client.
- If the client is **not found**, initialize the counter to 1 and set an expiration (TTL) of 60 seconds.
- If found, **increment the counter**.

---

### 4. **Rate Check**

- If the updated count **exceeds 100**, the Rate Limiter immediately:
  - Returns HTTP **429 Too Many Requests**
- If the count is **≤ 100**, the request is forwarded to the **downstream service**.

---

### 5. **Forward to Service and Response Flow**

- Valid requests are passed to the backend service.
- The service processes the request and sends a response back to the Rate Limiter.
- The Rate Limiter forwards the response back to the Load Balancer, and then to the client.

---

## 🧠 Rate Limiting Algorithms

### ✅ Fixed Window Counter

- Track counts in buckets of time (e.g., per minute).
- Simple but may allow bursts at window boundaries.

### ✅ Sliding Window Log

- Store timestamps of all requests in a window.
- More accurate but memory-intensive at scale.
- On each request:
    Remove timestamps older than 60 seconds
    Check the list length
    If < 100 → allow and add current timestamp
    Else → reject

### ✅ Token Bucket (Recommended)

- Each client has a bucket with 100 tokens.
- One token is consumed per request.
- Tokens refill gradually (e.g., 1.66 tokens/sec).
- Allows smooth traffic and short bursts.

---

## 🗃️ Redis Schema Example (Fixed Window)

| Key             | Value | TTL     |
|-----------------|-------|---------|
| `rate:user123`  | 57    | 60 sec  |
| `rate:10.0.0.1` | 13    | 60 sec  |

Use atomic Redis commands like `INCR` + `EXPIRE` to ensure thread safety.

---

## ⚖️ Scaling the System

- Use **consistent hashing** for sticky session routing.
- Use **Redis Cluster** to scale horizontally.
- Add **rate limiter logic to API Gateway middleware** (e.g., NGINX, Envoy) for ultra-low latency.
- Use **circuit breakers** and fail-safes if Redis is unreachable.

---

## 🔁 HTTP Response Behavior

| Scenario                        | Status Code | Behavior                         |
|---------------------------------|-------------|----------------------------------|
| Under the limit (≤ 100/min)     | `200 OK`    | Forwarded to backend             |
| Over the limit (> 100/min)      | `429`       | Blocked by Rate Limiter          |
| Redis/cache down (fallback)     | `503`       | Optionally reject or degrade     |

---

## ✅ Summary

- The Rate Limiter guards your system against abuse.
- It must be **fast**, **per-client**, and **distributed-safe**.
- A combination of **load balancer**, **sticky routing**, and **in-memory storage** enables scale.
- Choose your algorithm based on precision vs. complexity trade-offs.

