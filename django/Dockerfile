FROM simplestory:5000/mydjango:v5
ENV LANG C.UTF-8
COPY simplestory /simplestory/
WORKDIR /simplestory
EXPOSE 7529
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "--bind", ":7529", "--workers", "3", "simplestory.wsgi"]
