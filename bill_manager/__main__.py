import uvicorn

from bill_manager.settings import get_settings

settings = get_settings()


def main() -> None:
    uvicorn.run(
        "bill_manager.api.application:get_app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        factory=True,
    )


if __name__ == "__main__":
    main()
