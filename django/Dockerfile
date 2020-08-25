FROM simplestory:5000/mydjango:latest
ENV LANG C.UTF-8
EXPOSE 8000
COPY simplestory /simplestory/
WORKDIR /simplestory
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
