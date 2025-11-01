# DJShop

A Django REST API e-commerce platform.

## Tech Stack

- **Django** 5.1.4
- **Django REST Framework** 3.15.2
- **PostgreSQL** 17.6
- **Redis** (for caching & Celery)
- **Docker & Docker Compose**
- **Celery** (async tasks)
- **Channels** (WebSocket support)

## Prerequisites

- Docker & Docker Compose

## Configuration

Create a `.env` file in the project root. The following variables are available (all have defaults if omitted):

```env
# Django Core Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Database Configuration
DB_NAME=djshop
DB_USER=djshop
DB_PASSWORD=your-db-password
DB_HOST=db
DB_PORT=5432
```

**Quick setup:**
```bash
cp .env.example .env
# Edit .env with your values
```


## Quick Start

```bash
# Start services
docker-compose up --build

# The API will be available at http://localhost:8000
```

## Development

The project uses Docker for local development. The app automatically runs migrations on startup.

### API Endpoints

- **Admin API**: `/api/admin/`
- **Frontend API**: `/api/front/`
- **Django Admin**: `/admin/`

### Project Structure

## Apps

### Catalog

Manages product categories with hierarchical structure using `django-treebeard`.

**Models:**
- `Category` - Hierarchical category tree

---

*This README will be updated as the project evolves.*