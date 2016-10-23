from aiohttp import web

async def endpoint(request):
    return web.Response(text="I'm listening")

app = web.Application()
app.router.add_get('/endpoint', endpoint)

web.run_app(app)
