FROM python:3

WORKDIR /app/lights_in_space

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD [ "python", "./coordinate_prep_1.py" ]