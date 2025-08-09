# 🤖 Aiogram Moduled Structure Bot Template

---

## English

### 📋 Overview

A modern, production-ready Telegram bot template built with Python using aiogram 3.x, Tortoise ORM, and structured logging. This template provides a solid foundation for building scalable Telegram bots with clean architecture and best practices.

### ✨ Features

- **Modern Framework**: Built with aiogram 3.x for async Telegram bot development
- **Database Integration**: Tortoise ORM with automatic schema generation
- **Structured Logging**: Advanced logging with Loguru including file rotation and compression
- **Middleware System**: User management middleware for automatic user creation
- **Modular Architecture**: Clean separation of concerns with routers and models
- **Environment Configuration**: Secure configuration management with Pydantic
- **Error Handling**: Comprehensive error handling and graceful shutdown

### 🏗️ Project Structure

```
project/
├── main.py                     # Application entry point
├── src/
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py          # Configuration settings
│   ├── middlewares/
│   │   ├── __init__.py
│   │   └── user_middleware.py # User management middleware
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py           # Database models
│   ├── routers/
│   │   ├── __init__.py
│   │   └── user.py           # Route handlers
│   └── utils/
│       └── logging.py        # Logging configuration
├── logs/                     # Log files directory
└── .env                     # Environment variables
```

### 🚀 Quick Start

#### Prerequisites

- Python 3.8+
- pip or poetry

#### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd telegram-bot-template
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   ```bash
   cp .env.example .env
   ```

   Edit `.env` file:

   ```env
   BOT_TOKEN=your_bot_token_here
   DB_URL=sqlite://db.sqlite3
   ```

4. **Run the bot**
   ```bash
   python main.py
   ```

### 🔧 Configuration

The bot uses environment variables for configuration:

| Variable    | Description             | Example               |
| ----------- | ----------------------- | --------------------- |
| `BOT_TOKEN` | Telegram Bot API token  | `123456:ABC-DEF...`   |
| `DB_URL`    | Database connection URL | `sqlite://db.sqlite3` |

### 📝 Usage Examples

#### Adding New Commands

1. Create a new router or add to existing one:

```python
@router.message(Command("help"))
async def help_command(message: Message, user: User):
    await message.reply("Help message here!")
```

2. Register the router in `src/routers/__init__.py`

#### Adding New Models

```python
# src/models/example.py
from tortoise import fields
from tortoise.models import Model

class Example(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "examples"
```

### 🎯 Key Components

#### Middleware System

- **UserMessageMiddleware**: Automatically creates/retrieves users for messages
- **UserCallbackQueryMiddleware**: Handles user context for callback queries

#### Logging System

- Console output with colored formatting
- File logging with daily rotation
- Automatic log compression and retention
- Integration with aiogram and tortoise loggers

#### Database Layer

- Tortoise ORM for async database operations
- Automatic schema generation
- Pydantic model integration for serialization

### 🛠️ Development

#### Adding New Features

1. **Models**: Add new database models in `src/models/`
2. **Routers**: Create route handlers in `src/routers/`
3. **Middleware**: Add custom middleware in `src/middlewares/`
4. **Configuration**: Extend settings in `src/config/config.py`

#### Best Practices

- Use type hints throughout the codebase
- Follow async/await patterns
- Implement proper error handling
- Use structured logging
- Keep routes focused and lightweight

### 📊 Logging

The template includes comprehensive logging:

- **Console**: Colored output for development
- **Files**: Daily rotated log files in `logs/` directory
- **Compression**: Automatic log compression after rotation
- **Retention**: 31-day log retention policy

### 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request
