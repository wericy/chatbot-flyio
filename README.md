
## 🚀 Deploying to Fly.io

You can easily deploy this chatbot API as a public endpoint using [Fly.io](https://fly.io), which offers fast, global hosting and a generous free tier.

### ✅ 1. Install Fly CLI

```bash
curl -L https://fly.io/install.sh | sh
```

Then either restart your terminal or add this to your shell config:

```bash
export PATH="$HOME/.fly/bin:$PATH"
```

---

### ✅ 2. Login to Fly.io

```bash
fly auth login
```

A browser window will open for authentication.

---

### ✅ 3. Launch the App

From the project root (where `Dockerfile` lives):

```bash
fly launch
```

- App name? → Choose one or press Enter for a random name
- Region? → Choose the closest region to your users
- Postgres? → No

Fly will generate a `fly.toml` and set up the app for deployment.

---

### ✅ 4. Update `Dockerfile`

Fly expects apps to listen on port **`8080`**, so make sure your `Dockerfile` has:

```dockerfile
EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

Then rebuild the app:

```bash
fly deploy
```

---

### ✅ 5. Test the Public API

After deployment, Fly gives you a public URL like:

```
https://your-app-name.fly.dev
```

You can test the chatbot with:

```bash
curl -X POST https://your-app-name.fly.dev/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Hello, how are you?"}'
```

---

### ✅ 6. Optional Configuration

Inside `fly.toml`:

- **Keep one machine always online** (to prevent cold starts):
  ```toml
  [http_service]
    min_machines_running = 1
  ```

- **Add health checks**:
  ```toml
  [checks]
    [checks.http]
      interval = "30s"
      timeout = "10s"
      method = "get"
      path = "/"
  ```

---

### ✅ Redeploy After Changes

Whenever you update your code:

```bash
fly deploy
```

That's it — you're running a production-ready Transformer chatbot on Fly.io with a public endpoint! 🎯

---

Let me know if you'd like to include a matching GitHub Actions deployment workflow or domain config next.
