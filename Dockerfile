FROM python:3.5
RUN useradd -ms /bin/bash admin
USER admin
WORKDIR /sharks
COPY . /sharks
RUN pip install --user -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
