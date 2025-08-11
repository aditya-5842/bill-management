import uvicorn


def main() -> None:
    uvicorn.run(
        "bill_manager.api.application:get_app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        factory=True,
    )


if __name__ == "__main__":
    main()
