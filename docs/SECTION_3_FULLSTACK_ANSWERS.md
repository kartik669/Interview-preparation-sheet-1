# Section 3: Full-Stack Technical Interview Answers

This document contains deep, interview-tested answers for the cumulative Full-Stack Technical round in **Sheet 01** of Sheryians Coding School Weekly Preparation.

---

## Question 1: JavaScript — Async Flow
**Prompt**: *You call an API using `fetch()`, update the UI after the response, and also have a `setTimeout()` in the same flow. Explain how JavaScript's event loop affects the order of execution.*

### Core Explanation & Mental Model
JavaScript is **single-threaded** and executes code synchronously on the **Call Stack**. Long-running asynchronous operations (like network requests via `fetch()` and timers via `setTimeout()`) are offloaded to browser Web APIs / Node.js C++ bindings.

When asynchronous operations complete, their callbacks are queued into two separate queues:
1. **Microtask Queue**: Promises (`.then()`, `.catch()`, `.finally()`), `async/await` continuation points, `queueMicrotask()`, and `process.nextTick()` in Node.
2. **Macrotask (Task) Queue**: `setTimeout()`, `setInterval()`, `setImmediate()`, I/O callbacks, and DOM UI events.

### Step-by-Step Execution Sequence
Consider the code:
```javascript
console.log("1. Start");

setTimeout(() => {
    console.log("2. setTimeout Callback");
}, 0);

fetch("https://api.example.com/data")
    .then(res => res.json())
    .then(data => {
        console.log("3. Fetch Promise Callback (UI Update)");
    });

console.log("4. End");
```

1. `console.log("1. Start")` runs immediately on the Call Stack.
2. `setTimeout(..., 0)` registers a timer with the Web API. Even with 0ms, its callback is scheduled in the **Macrotask Queue**.
3. `fetch(...)` registers an HTTP request with the network thread.
4. `console.log("4. End")` executes on the Call Stack.
5. The Call Stack is now empty. The Event Loop checks the **Microtask Queue** first.
6. When the network response returns, its `.then()` callback is pushed to the **Microtask Queue**.
7. **Rule of the Event Loop**: All microtasks must be completely drained before the next macrotask is picked up!
8. Therefore, the Promise callback (updating UI) executes before `setTimeout` callback.

### Follow-Ups
- **What is the difference between a microtask and a macrotask?**
  - **Microtasks** have higher priority. After every synchronous turn of the call stack, the Event Loop executes *all* queued microtasks until the microtask queue is completely empty (including any microtasks queued by other microtasks) before re-rendering the DOM or executing a macrotask.
  - **Macrotasks** are executed one per event loop cycle. After executing one macrotask, the browser can perform style recalculation, layout, and paint before moving to the next task.
- **Where do Promise callbacks fit?**
  - All Promise resolutions (`.then()`, `.catch()`, `.finally()`) and code after an `await` expression run as **Microtasks**.
- **Why can blocking synchronous JavaScript make the UI feel frozen?**
  - The browser's layout engine, user interaction handlers (clicks, scrolling), and screen repainting (targeting 60fps / 16.6ms intervals) run on the **same main thread** as JavaScript execution. If a heavy synchronous loop (`while(true)`, CPU-heavy cryptographic hashing, or large array manipulation) occupies the Call Stack, the Event Loop cannot yield to the rendering pipeline, causing the browser tab to freeze ("Page Unresponsive").

---

## Question 2: React — Unnecessary Re-render
**Prompt**: *A React page becomes slow because a parent component re-renders frequently and several child components also re-render. How would you investigate and improve it?*

### 1. Investigation Workflow
1. **React Developer Tools Profiler**:
   - Open Chrome DevTools -> Profiler tab -> Check *"Record why each component rendered"*.
   - Start recording, trigger the action, stop recording. Inspect flame graph color coding (yellow/orange = long render time, gray = did not render).
2. **Visual Inspection via "Highlight updates when components render"**:
   - Check this box in React DevTools settings. Any component repainting will flash green/yellow/red borders.
3. **Automated Tools**:
   - Integrate `@welldone-software/why-did-you-render` to log exact props or state references triggering unnecessary renders in console.

### 2. Improvement Strategies
1. **Push State Down**: If state is only used in a small subtree, avoid keeping it in the top parent. Move state to the local child.
2. **Lift Content Up / Component Composition**: Pass children as props (`children`), so when parent re-renders, React reuses the existing child VDOM tree without re-rendering children.
3. **`React.memo`**: Wrap pure child components so they only re-render if their props change by shallow comparison (`Object.is`).
4. **Stable Prop References**:
   - Wrap handler functions passed to memoized children in `useCallback`.
   - Wrap complex objects or arrays passed to children in `useMemo`.

### Follow-Ups
- **When would React.memo help?**
  - `React.memo` helps when:
    1. The child component renders often with identical props.
    2. The child component has an expensive render tree (many DOM nodes, complex SVGs, data grids).
    3. The parent re-renders due to independent state that does not affect the child.
- **What are useMemo and useCallback actually solving?**
  - In JavaScript, `{}` !== `{}` and `(() => {}) !== (() => {})` (referential inequality).
  - Every time a parent renders, new object/function instances are created in memory with new memory addresses.
  - Passing unmemoized functions or objects to a `React.memo` child breaks the shallow equality check every time.
  - `useCallback(fn, deps)` preserves the **function memory reference** across renders.
  - `useMemo(() => val, deps)` caches the **computed value** across renders so expensive calculations are skipped.
- **Why should you avoid adding memoization everywhere?**
  1. **Memory & CPU Overhead**: Every `useMemo`, `useCallback`, and `React.memo` creates additional closures, dependency array allocations, and shallow comparison checks on every single render.
  2. **Premature Optimization**: Re-rendering in React is virtual DOM diffing in JavaScript memory, which is usually blazing fast (sub-millisecond). Memoization is only useful when actual render bottleneck exists.
  3. **Code Complexity & Stale Closures**: Forgetting a dependency in `useCallback` causes subtle bugs with stale state.

---

## Question 3: REST API + Express — Request Flow
**Prompt**: *A protected `GET /api/profile` endpoint is returning 401 for a logged-in user. Explain the complete request flow and how you would debug it.*

### 1. Complete Request Flow
```
Client (Browser) 
   │  Sends HTTP GET /api/profile with Header: [Authorization: Bearer <token>]
   ▼
Express Server (Node.js HTTP Server)
   │
   ├─► Global Middleware 1: cors() (Validates origin & headers)
   ├─► Global Middleware 2: express.json() / cookieParser()
   ├─► Router: Matches route '/api/profile'
   │
   ├─► Route Middleware: authMiddleware(req, res, next)
   │     ├─► Extracts token from Authorization header or cookies
   │     ├─► Verifies JWT signature using jwt.verify(token, JWT_SECRET)
   │     ├─► Fetches user payload & attaches to req.user
   │     └─► Calls next() -> Passes control to controller
   ▼
Profile Controller: (req, res) => res.json({ profile: req.user })
```

### 2. Step-by-Step Debugging
1. **Inspect Client Request Headers**:
   - Open Network Tab -> Click `GET /api/profile` -> Check `Request Headers`.
   - Is `Authorization: Bearer <jwt>` present? If cookies are used, is `Credentials: 'include'` set in `fetch`?
2. **Inspect Server Logs**:
   - Log `req.headers.authorization` in `authMiddleware`.
3. **Common Root Causes**:
   - **Missing Bearer prefix**: Sending `token` instead of `Bearer token`, causing `req.headers.authorization.split(" ")[1]` to be undefined.
   - **Token Expiry**: JWT payload `exp` expired. `jwt.verify` throws `TokenExpiredError`.
   - **JWT Secret Mismatch**: Server environment variable `process.env.JWT_SECRET` is undefined or differs between instances.
   - **CORS / Preflight Issue**: If CORS does not allow `Authorization` in `allowedHeaders`, browser drops it.

### Follow-Ups
- **Where should authentication middleware run?**
  - It must run **after** body parsing and cookie parsing middlewares, but **before** the protected route controller handlers. It can be applied selectively to specific routers (`app.use('/api/protected', authMiddleware, protectedRouter)`) or directly in the route declaration (`router.get('/profile', authMiddleware, getProfile)`).
- **How would you distinguish an authentication failure from an authorization failure?**
  - **Authentication Failure ("Who are you?")**: The user failed to prove their identity (missing/invalid/expired token or incorrect credentials).
  - **Authorization Failure ("What can you do?")**: The user's identity is verified, but they lack permission to access the requested resource (e.g., a student trying to access an instructor admin panel).
- **Which HTTP status codes would you use for 401 and 403?**
  - **`401 Unauthorized`**: Used when authentication is missing or invalid. Client must provide valid credentials.
  - **`403 Forbidden`**: Used when authenticated user is recognized, but access to this specific endpoint/resource is denied regardless of credentials.

---

## Question 4: MongoDB + Mongoose — Duplicate Data
**Prompt**: *Your registration API is allowing two users to register with the same email under a race condition. How would you prevent and handle duplicate records?*

### 1. Why Race Conditions Occur
In traditional application-level checking:
```javascript
// Flawed approach:
const existing = await User.findOne({ email });
if (!existing) {
    await User.create({ email, password });
}
```
If two registration requests for `test@example.com` arrive simultaneously at $t_0$, both requests execute `findOne` concurrently. Neither finds a document in the database yet. Both receive `null`, proceed to `User.create()`, and both write duplicate records. This is a classic **Time-of-Check to Time-of-Use (TOCTOU)** race condition.

### 2. How to Prevent It
1. **Enforce Database-Level Unique Index**:
   ```javascript
   const userSchema = new mongoose.Schema({
       email: {
           type: String,
           required: true,
           unique: true, // Creates a unique B-Tree index in MongoDB
           lowercase: true,
           trim: true,
           index: true
       }
   });
   ```
2. **Ensure Index is Actually Built in MongoDB**:
   In production, ensure `User.createIndexes()` runs or create index directly in MongoDB:
   `db.users.createIndex({ email: 1 }, { unique: true })`.

### 3. Handling the Duplicate-Key Error in Express
When MongoDB detects a duplicate key violation, it throws an error with code **`11000`**. We must catch this in our error handler:
```javascript
const registerUser = async (req, res, next) => {
    try {
        const { email, password } = req.body;
        const user = await User.create({ email, password });
        res.status(201).json({ success: true, user });
    } catch (error) {
        if (error.code === 11000) {
            // E11000 duplicate key error collection
            return res.status(409).json({
                success: false,
                message: "An account with this email already exists."
            });
        }
        next(error);
    }
};
```

### Follow-Ups
- **Would application-level checking alone be sufficient?**
  - **No.** Application-level checking (`findOne` followed by `save`) is non-atomic. In distributed environments with multiple server instances or cluster threads, concurrent requests can always bypass memory-level checks. Only the database storage engine can guarantee atomicity across concurrent writes.
- **How can a unique index help?**
  - MongoDB maintains a B-Tree index structure. Before committing a write to the WiredTiger storage engine, MongoDB checks the index leaf node. If the index key already exists, MongoDB aborts the write operation with code `11000`, ensuring zero duplicate records can ever be persisted.
- **How should the API respond when a duplicate-key error occurs?**
  - The API should respond with **`409 Conflict`** (or `400 Bad Request`) with a clean, user-friendly JSON message: `{"error": "Email is already registered"}`. Never return a `500 Internal Server Error` or expose raw database error stack traces.

---

## Question 5: Authentication + Authorization + ImageKit
**Prompt**: *A student is authenticated but should not be allowed to access another student's private resource or upload area. Design the checks you would apply before allowing the request, and explain where ImageKit fits into the upload flow.*

### 1. Access Control Design (Preventing IDOR)
**IDOR (Insecure Direct Object Reference)** occurs when an application trusts user input (like a URL param `/api/submissions/:submissionId`) without verifying ownership.

#### Request Verification Pattern:
1. Extract user identity strictly from verified session/JWT: `req.user.id`.
2. When querying a private resource, combine the resource ID with the owner ID:
   ```javascript
   // Secure check:
   const submission = await Submission.findOne({
       _id: req.params.id,
       studentId: req.user.id // Enforces resource ownership
   });
   
   if (!submission) {
       return res.status(404).json({ message: "Resource not found or access denied" });
   }
   ```
3. For role-based actions (e.g. instructors grading all submissions), use an authorization middleware:
   ```javascript
   const requireRole = (...roles) => (req, res, next) => {
       if (!roles.includes(req.user.role)) {
           return res.status(403).json({ message: "Forbidden: Insufficient privileges" });
       }
       next();
   };
   ```

### 2. ImageKit Integration Architecture
Direct client uploads to ImageKit prevent student uploads from choking the Express server's memory and CPU:

```
[Student Client]                [Express Backend]              [ImageKit CDN]
      │                                 │                             │
      │ 1. GET /api/imagekit/auth ─────►│                             │
      │    (with user JWT)              │                             │
      │                                 ├─► Generates HMAC signature  │
      │                                 │   token, expire, signature  │
      │ 2. Returns auth parameters ◄────┘                             │
      │                                                               │
      │ 3. Direct POST image + signature + student folder ───────────►│
      │    folder: `/students/${req.user.id}/`                        │
      │                                                               ├─► Stores file
      │ 4. Returns { fileId, url, thumbnail } ◄───────────────────────┘
      │                                 │
      │ 5. POST /api/submissions ──────►│
      │    { imageId, imageUrl }        ├─► Stores imageUrl in MongoDB
      │                                 │   linked to req.user.id
```

### Follow-Ups
- **What is the difference between authentication and authorization?**
  - **Authentication (AuthN)**: Identifies who the user is (e.g., verifying student email and password or JWT).
  - **Authorization (AuthZ)**: Determines what resources and operations that authenticated identity is allowed to perform (e.g., viewing only their own private submissions vs editing all submissions).
- **What information should the server trust from the client?**
  - The server should **NEVER** trust client-provided IDs for authorization (e.g., `req.body.userId`, URL parameters, or client headers).
  - The server should only trust cryptographically verified claims signed by the server itself (e.g., the decoded JWT payload stored securely in `req.user` by the `authMiddleware`).
- **How would you prevent a user from changing an ID in the URL and accessing someone else's data?**
  1. Never perform `Model.findById(req.params.id)` without checking `doc.studentId.equals(req.user.id)`.
  2. Better yet, scope queries directly: `Model.findOne({ _id: req.params.id, studentId: req.user.id })`.
  3. Return `404 Not Found` (or `403 Forbidden`) so attackers cannot enumerate valid IDs of other students.
