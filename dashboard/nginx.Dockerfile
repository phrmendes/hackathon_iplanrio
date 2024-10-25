FROM nginx:stable

RUN rm /etc/nginx/conf.d/default.conf
COPY ./dashboard/nginx.conf /etc/nginx/conf.d
