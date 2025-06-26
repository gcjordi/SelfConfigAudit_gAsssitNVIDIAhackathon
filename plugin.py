import sys
import json
from pynvml import nvmlInit, nvmlShutdown, nvmlDeviceGetHandleByIndex, nvmlDeviceGetTemperature, nvmlDeviceGetMemoryInfo, NVML_TEMPERATURE_GPU

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def check_question(question, config):
    question = question.lower()
    for key, value in config["modifiables"].items():
        if key in question:
            if value:
                return f"Yes, I am allowed to modify '{key}'. However, I will only simulate this action."
            else:
                return f"No, I am not permitted to modify '{key}' directly."
    return "I cannot determine the answer based on current capabilities."

def get_gpu_info():
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)
    temp = nvmlDeviceGetTemperature(handle, NVML_TEMPERATURE_GPU)
    mem_info = nvmlDeviceGetMemoryInfo(handle)
    nvmlShutdown()
    return temp, mem_info.used / 1024**2

def main():
    if len(sys.argv) < 2:
        print("Usage: python plugin.py "Your question here"")
        return

    question = sys.argv[1]
    config = load_config()
    temp, used_mem = get_gpu_info()

    print(f"Current GPU temperature: {temp} °C")
    print(f"Current VRAM usage: {used_mem:.2f} MB")

    answer = check_question(question, config)
    print("Response:", answer)

if __name__ == "__main__":
    main()
