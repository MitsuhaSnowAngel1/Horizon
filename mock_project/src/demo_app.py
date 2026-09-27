def status_message(service: str, healthy: bool) -> str:
    if not service.strip():
        raise ValueError("service must not be empty")
    state = "healthy" if healthy else "degraded"
    return f"{service}: {state}"