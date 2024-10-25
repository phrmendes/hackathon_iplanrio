FROM nginx:stable

RUN rm /etc/nginx/conf.d/default.conf
COPY ./licitacaorio/nginx.conf /etc/nginx/conf.d
