# =====================================================
# Stage 1: Generate the static HTML using Python
# =====================================================
FROM python:3.12-slim AS generator

WORKDIR /app

# Copy the Python generator script
COPY generate.py .

# Run the generator to produce index.html
RUN python generate.py

# =====================================================
# Stage 2: Serve the static site with Nginx
# =====================================================
FROM nginx:1.27-alpine

# Copy the generated HTML from the previous stage
COPY --from=generator /app/index.html /usr/share/nginx/html/index.html

# Copy all static assets (CSS, JS, fonts, images, video)
COPY css/          /usr/share/nginx/html/css/
COPY js/           /usr/share/nginx/html/js/
COPY img/          /usr/share/nginx/html/img/
COPY video/        /usr/share/nginx/html/video/
COPY fontawesome/  /usr/share/nginx/html/fontawesome/

# Expose port 80
EXPOSE 80

# Nginx runs in the foreground by default via its base image CMD
