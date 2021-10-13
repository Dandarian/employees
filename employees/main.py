from aiohttp import web
from routes import setup_routes
from db import pg_context

app = web.Application()
setup_routes(app)
app.cleanup_ctx.append(pg_context)
web.run_app(app)
