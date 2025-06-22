import os
from dotenv import load_dotenv
import tinytuya

load_dotenv()

DEVICE_ID = os.getenv("DEVICE_ID")
IP_ADDRESS = os.getenv("IP_ADDRESS")
LOCAL_KEY = os.getenv("LOCAL_KEY")
DPS_CODE = 1

plug = tinytuya.OutletDevice(DEVICE_ID, IP_ADDRESS, LOCAL_KEY)
plug.set_version(3.5)

status = plug.status()
current_state = status.get("dps", {}).get(str(DPS_CODE), None)

if current_state is not None:
    new_state = not current_state
    plug.set_status(new_state, DPS_CODE)
    action = "ENCENDIDO" if new_state else "APAGADO"
    print(f"✅ Enchufe {action}")
else:
    print("⚠️ No se pudo obtener el estado del enchufe.")