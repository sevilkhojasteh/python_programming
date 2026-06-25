# Concurrency & Parallelism in Python — A Complete Guide

This guide teaches you **Concurrency**, **Parallelism**, and the four core subjects you requested:

1. The **GIL** (Global Interpreter Lock)
2. **Threading**
3. **Multiprocessing**
4. **Asynchrony** (`asyncio`)

For each subject you get: **what it is → its use → two examples → one real-world exercise with a full answer.**

---

## Part 0 — The Big Picture: Concurrency vs Parallelism

These two words are constantly confused. Get them straight first.

### Concurrency
> **Dealing with** many things at once.

Concurrency is about **structure** — designing a program as independent tasks that *can* make progress in overlapping time. A concurrent program may run those tasks one-at-a-time, switching rapidly between them.

**Analogy:** One cook preparing a whole dinner. They put the soup on to simmer, *while* it simmers they chop vegetables, *while* those aren't being touched they set the table. One cook, many tasks in flight.

### Parallelism
> **Doing** many things at once.

Parallelism is about **execution** — actually running tasks at the exact same moment, which requires multiple hardware workers (CPU cores).

**Analogy:** Three cooks, each cooking a different dish simultaneously in real time.

### The famous one-liner (Rob Pike)
> *Concurrency is about dealing with lots of things at once. Parallelism is about doing lots of things at once.*

| | Concurrency | Parallelism |
|---|---|---|
| Concern | Structure / design | Execution |
| Needs many cores? | No | Yes |
| Example in Python | `asyncio`, `threading` | `multiprocessing` |

### The decision matrix (memorize this!)

| Task type | Example | Best tool |
|---|---|---|
| **CPU-bound** (heavy math) | Image processing, ML training | `multiprocessing` (parallelism) |
| **I/O-bound** (lots of waiting) | Web scraping, DB queries | `asyncio` or `threading` (concurrency) |
| **Few I/O tasks** | A handful of API calls | `threading` (simple) |
| **Thousands of I/O tasks** | Web crawler, chat server | `asyncio` (scales best) |

The reason these choices matter so much in Python is the **GIL**, which we cover next.

---

## Subject 1 — The GIL (Global Interpreter Lock)

### What it is
The GIL is a **mutex** (a lock) used by **CPython** (the standard Python interpreter). It ensures that **only one thread executes Python bytecode at any given moment**, even on a multi-core machine.

### Why it exists
CPython manages memory with **reference counting**. If multiple threads modified reference counts at the same time, counts could get corrupted, leading to leaked memory or premature deallocation. The GIL is the simplest way to make this safe. So:

> **The GIL makes CPython thread-safe at the cost of preventing true multi-core parallelism for pure-Python threads.**

### Its use (why you must understand it)
1. **It dictates your concurrency strategy.** Because of the GIL, CPU-bound threads do *not* run in parallel → you must use `multiprocessing` for heavy computation.
2. **It does NOT block I/O.** The GIL is released during I/O operations (network, disk, sleep), so threads remain great for I/O-bound work.
3. **It explains "weird" slowdowns.** Naively adding threads to a CPU-heavy task can make it *slower* due to lock contention.

> Note: PEP 703 is making CPython optionally GIL-free (no-GIL / free-threaded builds), but for most current production code the GIL is still the default reality.

---

### GIL — Example 1: Two CPU-bound threads do NOT speed up

This proves the GIL blocks parallel CPU work. A single thread and two threads take about the **same** time (two threads may even be slightly slower).

```python
import time
import threading

def count_down(n):
    while n > 0:
        n -= 1

COUNT = 50_000_000

# --- Single-threaded ---
start = time.perf_counter()
count_down(COUNT)
print(f"Single thread : {time.perf_counter() - start:.2f}s")

# --- Two threads sharing the work ---
start = time.perf_counter()
t1 = threading.Thread(target=count_down, args=(COUNT // 2,))
t2 = threading.Thread(target=count_down, args=(COUNT // 2,))
t1.start(); t2.start()
t1.join();  t2.join()
print(f"Two threads   : {time.perf_counter() - start:.2f}s")
```

**Expected output (your numbers vary):**
```
Single thread : 1.92s
Two threads   : 2.05s   # NOT faster — the GIL serializes the work
```

---

### GIL — Example 2: The GIL is released during I/O, so threads DO help

Here threads finish far faster because both sleep (I/O-like wait) simultaneously — the GIL is released during `time.sleep`.

```python
import time
import threading

def do_wait(seconds, label):
    print(f"{label} start")
    time.sleep(seconds)            # GIL released here
    print(f"{label} done")

start = time.perf_counter()

# Sequential: 1 + 1 + 1 = 3 seconds
# do_wait(1, "A"); do_wait(1, "B"); do_wait(1, "C")

# Threaded: all run at once -> ~1 second total
threads = [threading.Thread(target=do_wait, args=(1, label))
           for label in ("A", "B", "C")]
for t in threads: t.start()
for t in threads: t.join()

print(f"Total: {time.perf_counter() - start:.2f}s")
```

**Takeaway:** GIL + CPU-bound = no parallel speedup. GIL + I/O-bound = full concurrency speedup.

---

### GIL — Exercise (real world)

**Scenario:** You work on a data team. A colleague "optimized" a CPU-heavy image-filter pipeline by running it across **8 threads**, expecting an 8× speedup, but it got **slower**. 

**Task:** Write a short script that *demonstrates and explains* the problem: take a CPU-bound function and show that (a) running it with 4 threads is **not** faster than running it once, and (b) running it with `multiprocessing` **is** faster. Print a one-line conclusion.

#### Answer

```python
import time
import threading
from multiprocessing import Pool

def cpu_heavy(n):
    """A pure-Python CPU-bound workload."""
    total = 0
    for i in range(n):
        total += i * i
    return total

N = 20_000_000

# (a) ONE call (single thread)
start = time.perf_counter()
cpu_heavy(N)
single = time.perf_counter() - start

# (b) FOUR threads — GIL blocks parallelism, so ~ same or slower
start = time.perf_counter()
threads = [threading.Thread(target=cpu_heavy, args=(N,)) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
threaded = time.perf_counter() - start

# (c) FOUR processes — true parallelism across cores
start = time.perf_counter()
with Pool(4) as pool:
    pool.map(cpu_heavy, [N, N, N, N])
processed = time.perf_counter() - start

print(f"1 call / single thread : {single:6.2f}s")
print(f"4 threads              : {threaded:6.2f}s   <- GIL blocks this")
print(f"4 processes            : {processed:6.2f}s   <- real parallelism")
print("CONCLUSION: For CPU-bound work, threads don't help (GIL); use multiprocessing.")
```

**Why it's real world:** This exact mistake — "just throw threads at it" — is one of the most common Python performance bugs in data and ML teams.

---
---

## Subject 2 — Threading

### What it is
**Threading** lets you run multiple threads (lightweight units of execution) *within the same process*. They share the same memory space. In Python, because of the GIL, threads **concurrently** handle I/O but do not run CPU-bound code in parallel.

### Its use
- **I/O-bound work:** network requests, file reads/writes, database queries — anything where the program spends time *waiting*.
- **Keeping a UI / service responsive** while a background task runs.
- **Simple concurrency** when you only need a handful of parallel tasks and want minimal code.
- **Shared state is easy** (same memory) — but that also makes synchronization bugs easy, so protect shared data with `Lock`.

---

### Threading — Example 1: Concurrent file downloads

Downloading one file at a time is slow because you wait on the network. Threads let all downloads overlap.

```python
import threading
import urllib.request
import time

URLS = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
]

def download(url):
    with urllib.request.urlopen(url) as resp:
        data = resp.read()
    print(f"Downloaded {len(data)} bytes from {url}")

start = time.perf_counter()

# Sequential would take ~8s (4 x 2s). Threads finish in ~2s:
threads = [threading.Thread(target=download, args=(url,)) for url in URLS]
for t in threads: t.start()
for t in threads: t.join()

print(f"Done in {time.perf_counter() - start:.2f}s")
```

---

### Threading — Example 2: A thread-safe counter with a `Lock`

Multiple threads writing to a shared variable without protection causes **lost updates**. A `Lock` serializes the critical section.

```python
import threading

counter = 0
lock = threading.Lock()          # protects `counter`

def increment(n_times):
    global counter
    for _ in range(n_times):
        with lock:               # only one thread here at a time
            counter += 1

threads = [threading.Thread(target=increment, args=(100_000,)) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print(f"Final counter: {counter}")   # -> 500000 (correct; without lock it'd be random)
```

> Remove the `with lock:` lines and you'll usually get a wrong, lower number — the classic race condition.

---

### Threading — Exercise (real world)

**Scenario:** You're a DevOps/SRE engineer. You must check whether **many servers** (or APIs) are reachable before a deploy. Checking them one-by-one takes too long when you have 20+ hosts.

**Task:** Write a threaded **health-check** tool that pings a list of URLs concurrently, prints `OK <url>` or `FAIL <url>` for each, and prints how long it all took. Limit concurrency so you don't open hundreds of connections at once.

#### Answer (using a `ThreadPoolExecutor` — the modern, clean way)

```python
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

TARGETS = [f"https://httpbin.org/status/{code}"
           for code in [200, 200, 500, 404, 200, 200, 200, 503]]

def check(url):
    """Return (url, ok). ok is True for HTTP 2xx."""
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            return url, 200 <= r.status < 300
    except Exception:
        return url, False

def run_health_check(urls, max_workers=8):
    start = time.perf_counter()
    results = []
    # ThreadPoolExecutor keeps the worker count bounded.
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(check, url): url for url in urls}
        for fut in as_completed(futures):
            url, ok = fut.result()
            status = "OK  " if ok else "FAIL"
            print(f"[{status}] {url}")
            results.append((url, ok))
    elapsed = time.perf_counter() - start
    healthy = sum(1 for _, ok in results if ok)
    print(f"\n{healthy}/{len(results)} healthy in {elapsed:.2f}s")
    return results

run_health_check(TARGETS, max_workers=4)
```

**Why it's real world:** Concurrent health checks, smoke tests, and deploy-time verification scripts are everyday SRE tools. `ThreadPoolExecutor` is exactly how production code does bounded concurrency.

---
---

## Subject 3 — Multiprocessing

### What it is
**Multiprocessing** runs work in **separate OS processes**, each with its **own Python interpreter and memory space** and its **own GIL**. This is the only built-in way to get **true parallel CPU execution** in standard CPython.

### Its use
- **CPU-bound work:** number crunching, image/audio processing, data transformations, compression, hashing.
- **Bypassing the GIL** — multiple cores truly compute in parallel.
- **Embarrassingly parallel** jobs (map/reduce over a dataset).
- **Trade-offs:** processes are heavier than threads (startup cost + memory), and sharing data between them requires queues, pipes, or shared memory (objects must be **picklable**).

---

### Multiprocessing — Example 1: Parallel square of a big list with `Pool`

```python
from multiprocessing import Pool
import time

def square(x):
    return x * x          # CPU work (trivial here, scale up for real load)

data = list(range(1_000_000))

start = time.perf_counter()
with Pool(processes=4) as pool:          # 4 worker processes
    result = pool.map(square, data)
print(f"Parallel: {time.perf_counter() - start:.2f}s, sum={sum(result)}")
```

The `Pool` distributes `data` across 4 processes. On a multi-core machine this is markedly faster than a plain loop for heavy `square`-like work.

---

### Multiprocessing — Example 2: Worker pool communicating through a `Queue`

Producers and consumers in separate processes, safely exchanging picklable messages.

```python
from multiprocessing import Process, Queue

def producer(q):
    for item in ["job-1", "job-2", "job-3", "STOP"]:
        q.put(item)

def consumer(q):
    while True:
        item = q.get()
        if item == "STOP":
            break
        print(f"Processed {item}")

if __name__ == "__main__":
    q = Queue()
    p = Process(target=producer, args=(q,))
    c = Process(target=consumer, args=(q,))
    p.start(); c.start()
    p.join();  c.join()
    print("All done")
```

> **Always** guard process-launching code with `if __name__ == "__main__":` (especially on Windows) to avoid infinite recursive child spawning.

---

### Multiprocessing — Exercise (real world)

**Scenario:** You're a backend engineer. Users upload large CSV files; you must count the rows in each file across **many files** as fast as possible. Counting rows is CPU/disk-bound, so you parallelize across cores.

**Task:** Write a program that counts the total number of data rows (excluding the header) across a folder of CSV files, using a `ProcessPoolExecutor`. Print each file's count and the grand total, and the elapsed time.

#### Answer

```python
import csv
import glob
import time
from concurrent.futures import ProcessPoolExecutor

def count_rows(path):
    """Count data rows (skip header) in one CSV file. Must be picklable + top-level."""
    with open(path, newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)      # skip header
        return path, sum(1 for _ in reader)

def count_all(csv_pattern, workers=4):
    files = glob.glob(csv_pattern)
    grand_total = 0
    start = time.perf_counter()
    # Each process has its own GIL -> real parallel row counting.
    with ProcessPoolExecutor(max_workers=workers) as pool:
        for path, n in pool.map(count_rows, files):
            print(f"{path}: {n} rows")
            grand_total += n
    print(f"\nTOTAL rows: {grand_total}  ({len(files)} files)")
    print(f"Elapsed: {time.perf_counter() - start:.2f}s")
    return grand_total

if __name__ == "__main__":
    # Point this at your folder, e.g. "uploads/*.csv"
    count_all("*.csv", workers=4)
```

**Why it's real world:** Batch-processing uploaded files, log analysis, and ETL row-counting are textbook parallel-CPU jobs. `ProcessPoolExecutor` is the idiomatic, production-friendly way to parallelize them.

---
---

## Subject 4 — Asynchrony (`asyncio`)

### What it is
**Asynchrony** is a concurrency model where tasks **cooperatively** suspend themselves while waiting (`await`) instead of blocking. Python's `asyncio` library provides an **event loop** that switches between tasks whenever one awaits I/O. It is **single-threaded** and uses **no extra threads/processes** — one thread juggles thousands of tasks.

### Its use
- **Massive I/O concurrency:** web crawlers, chat servers, API gateways, real-time feeds.
- **Network I/O where you'd otherwise need thousands of threads.** One async task ≈ negligible memory; one thread ≈ several MB.
- **Cooperative multitasking:** tasks must `await`; a task that never awaits blocks the whole loop.
- **Not for CPU-bound work** (the loop is single-threaded; for CPU work, combine `asyncio` with `multiprocessing` via `run_in_executor`).

---

### Asynchrony — Example 1: Fetch many URLs concurrently with `aiohttp`

```python
import asyncio
import time
import aiohttp            # pip install aiohttp

URLS = ["https://httpbin.org/delay/2"] * 6

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def main():
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        # All requests start at once and overlap while waiting on the network.
        tasks = [fetch(session, url) for url in URLS]
        results = await asyncio.gather(*tasks)
    print(f"Fetched {len(results)} pages in {time.perf_counter() - start:.2f}s")

asyncio.run(main())      # ~2s total, not 12s
```

---

### Asynchrony — Example 2: Cooperative tasks with `asyncio.gather`

Two coroutines take turns — each `await asyncio.sleep` yields control to the other.

```python
import asyncio

async def task(name, delay):
    for i in range(3):
        await asyncio.sleep(delay)      # yields to the event loop
        print(f"{name}: step {i}")

async def main():
    # Both run concurrently on ONE thread.
    await asyncio.gather(
        task("A", 0.5),
        task("B", 0.3),
    )

asyncio.run(main())
```

**Output (interleaved):**
```
B: step 0
A: step 0
B: step 1
B: step 2
A: step 1
A: step 2
```

---

### Asynchrony — Exercise (real world)

**Scenario:** You're building a **monitoring/observability tool** that periodically checks the health of dozens of microservices and reports which ones are up/down. Synchronous checks are too slow; threads don't scale cleanly to 50+ endpoints.

**Task:** Write an async health checker that:
1. Fetches a list of service URLs **concurrently** (with a concurrency limit, e.g. 10 at a time).
2. Records response time and status (OK/FAIL) for each.
3. Prints a summary table.

#### Answer

```python
import asyncio
import time
import aiohttp          # pip install aiohttp

SERVICES = {
    "auth":      "https://httpbin.org/status/200",
    "billing":   "https://httpbin.org/status/500",
    "search":    "https://httpbin.org/status/200",
    "inventory": "https://httpbin.org/status/503",
    "notify":    "https://httpbin.org/status/200",
}

async def check(session, name, url, timeout=5):
    """Check one service; return (name, ok, elapsed_ms)."""
    start = time.perf_counter()
    try:
        async with session.get(url, timeout=timeout) as resp:
            ok = 200 <= resp.status < 300
    except Exception:
        ok = False
    elapsed_ms = (time.perf_counter() - start) * 1000
    return name, ok, elapsed_ms

async def main(max_concurrency=10):
    start = time.perf_counter()
    # Semaphore caps how many checks run at once -> bounded concurrency.
    sem = asyncio.Semaphore(max_concurrency)

    async def bounded(name, url):
        async with sem:
            return await check(name=name, url=url, session=session)

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *(bounded(n, u) for n, u in SERVICES.items())
        )

    print(f"{'SERVICE':<12}{'STATUS':<8}{'LATENCY':<10}")
    print("-" * 30)
    up = 0
    for name, ok, ms in results:
        up += ok
        print(f"{name:<12}{'OK' if ok else 'DOWN':<8}{ms:>7.0f}ms")
    print("-" * 30)
    print(f"{up}/{len(results)} healthy | total {time.perf_counter()-start:.2f}s")

if __name__ == "__main__":
    asyncio.run(main(max_concurrency=10))
```

**Why it's real world:** Async health monitors, uptime checkers (like a mini UptimeRobot), and service-mesh probes are archetypal asyncio apps — thousands of endpoints, all I/O, on a single thread.

---
---

## Quick-Reference Cheat Sheet

```
┌──────────────────────┬─────────────────┬──────────────────────────────────┐
│ Tool                 │ Best for        │ Parallel?  │ Memory per unit     │
├──────────────────────┼─────────────────┼──────────────────────────────────┤
│ threading            │ I/O-bound (few)  │ No (GIL)  │ low (~MB)           │
│ multiprocessing      │ CPU-bound        │ Yes       │ high (own process)  │
│ asyncio              │ I/O-bound (many) │ No*       │ very low            │
│ (GIL)                │ — (a constraint) │ —         │ —                   │
└──────────────────────┴─────────────────┴──────────────────────────────────┘
* asyncio is single-threaded; use run_in_executor + multiprocessing for CPU work.
```

### Golden rules
1. **CPU-bound?** → `multiprocessing` (the GIL blocks threading parallelism).
2. **I/O-bound, a few tasks?** → `threading` / `ThreadPoolExecutor`.
3. **I/O-bound, thousands of tasks?** → `asyncio`.
4. **Shared mutable state across threads?** → always use a `Lock`.
5. **Launching processes?** → always guard with `if __name__ == "__main__":`.
6. **Async code?** → never block the loop with long sync/CPU work; offload it.

---

### How to practice next
- Run each example and the exercises (install `aiohttp` for the async ones: `pip install aiohttp`).
- Modify the exercises: add retry logic, timeouts, logging, and result persistence to a file/DB.
- Combine tools: e.g., an async server that offloads CPU work to a `ProcessPoolExecutor` via `loop.run_in_executor`.

**You now understand: concurrency vs parallelism, the GIL, threading, multiprocessing, and async — with real-world examples and exercises for each.**
