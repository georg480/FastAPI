import fastapi

from models.location import Location
from models.umbrella_status import UmbrellaStatus
from services import live_weather_service

router = fastapi.APIRouter()


@router.get("/api/umbrella", response_model=UmbrellaStatus)
async def do_i_need_an_umbrella(location: Location = fastapi.Depends()):
    """Anfrage an weather händlen

    Return: Wetter
    -------
    object
    """
    #    https: // weather.talkpython.fm / api / weather?city = portland & state = OR & country = US & units = imperial
    # url = "https://weather.talkpython.fm/api/weather?city=portland&state=OR&country=US&units=imperial"
    data = await live_weather_service.get_live_report(location)

    weather = data.get("weather", {})
    category = weather.get("category", "UNKNOWN")

    forecast = data.get("forecast", {})
    temp = forecast.get("temp", 0.0)

    bring = category.lower().strip() in {"rain", "mist"}

    umbrella = UmbrellaStatus(bring_umbrella=bring, temp=temp, weather=category)
    return umbrella
