from pathlib import Path

from fastapi.templating import Jinja2Templates

csrs_templates = Jinja2Templates(directory=str(Path(__file__).parent))
