from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request): return templates.TemplateResponse(request=request, name="index.html", context={})
@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request): return templates.TemplateResponse(request=request, name="login.html", context={})
@app.post("/login-action")
async def login_action(): return RedirectResponse(url="/", status_code=302)
@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request): return templates.TemplateResponse(request=request, name="register.html", context={})
@app.post("/register-action")
async def reg_action(): return RedirectResponse(url="/login", status_code=302)

@app.get("/home-budget", response_class=HTMLResponse)
async def hb(request: Request): return templates.TemplateResponse(request=request, name="home_budget.html", context={})
@app.get("/home-result", response_class=HTMLResponse)
async def hr(request: Request): return templates.TemplateResponse(request=request, name="home_result.html", context={})

@app.get("/party-budget", response_class=HTMLResponse)
async def pb(request: Request): return templates.TemplateResponse(request=request, name="party_budget.html", context={})
@app.get("/party-result", response_class=HTMLResponse)
async def pr(request: Request): return templates.TemplateResponse(request=request, name="party_result.html", context={})

@app.get("/jewelry-budget", response_class=HTMLResponse)
async def jb(request: Request): return templates.TemplateResponse(request=request, name="jewelry_budget.html", context={})
@app.get("/jewelry-result", response_class=HTMLResponse)
async def jr(request: Request): return templates.TemplateResponse(request=request, name="jewelry_result.html", context={})

@app.get("/history", response_class=HTMLResponse)
async def history(request: Request): return templates.TemplateResponse(request=request, name="history.html", context={})