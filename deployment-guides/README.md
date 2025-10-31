# Deployment Guides

## Render (Backend)
1. Create a new Web Service on Render.
2. Connect your GitHub repo and select the `backend` folder as the root.
3. Build command: `pip install -r requirements.txt && python train.py || true`
   - The `train.py` may run on Render but could be skipped if you upload pre-trained model files.
4. Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`
5. Add environment variables if needed. Deploy.

## Render (Frontend)
1. Create a Static Site on Render.
2. Connect the repo and set the build command: `npm install && npm run build`
3. Publish directory: `frontend/dist`
4. Set environment to point API requests to your backend URL (or configure CORS).

## Vercel (Frontend)
1. In Vercel, import project and set the root directory to `/frontend`.
2. Framework: Vite (or other).
3. Build Command: `npm install && npm run build`
4. Output Directory: `dist`
5. After deploy, set an environment variable or use `fetch` URL to call the backend.

## Heroku (Backend)
1. `heroku create your-app-name`
2. Add a Procfile: `web: gunicorn app:app`
3. Push the backend folder: `git subtree push --prefix backend heroku main`
4. Set buildpacks if necessary, and add config vars.
5. Ensure `backend/model/` contains model files or run `train.py` in build step.

## Notes on CORS and Proxy
- The frontend Vite config proxies `/api` to the Flask backend in development.
- In production, either:
  - Serve the built frontend from the same domain as the backend, OR
  - Enable CORS on the backend (`flask-cors` is already included), and set the frontend to call the full backend URL.

## Using Docker
- Build: `docker-compose -f docker/docker-compose.yml up --build`
- This runs both services locally on ports 5000 and 5173.

